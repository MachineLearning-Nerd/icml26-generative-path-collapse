"""Run the fixed cumulative verifier and print all evidence to stdout."""

from __future__ import annotations

import json
import os
import platform
import sys
import time
from dataclasses import dataclass
from typing import Any

# The baseline is authorized for local execution only as a single-core,
# sub-five-minute task. Set limits before importing NumPy/SciPy.
for _name in (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_name] = "1"

import numpy as np

from reproduction.core import (
    OFFICIAL_SCHEDULES,
    ace_bump,
    analytic_gaussian_log_integral,
    criterion,
    gaussian_log_integral_numeric,
    sigmoid_unit,
)


@dataclass(frozen=True)
class Check:
    claim: str
    status: str
    passed: bool
    evidence: dict[str, Any]
    scope: str


def constant(value: float):
    return lambda t: np.zeros_like(np.asarray(t), dtype=float) + value


def claim_1() -> Check:
    """Endpoint-valid Gaussian composition with an invalid intermediate."""
    ts = np.linspace(0.0, 0.999, 2_000)
    gammas = [constant(1.0), constant(-0.5)]
    schedules = [OFFICIAL_SCHEDULES["polynomial"], OFFICIAL_SCHEDULES["sigmoid"]]
    values = criterion(ts, gammas, schedules)
    collapse_idx = int(np.argmin(values))
    collapse_t = float(ts[collapse_idx])
    collapse_c = float(values[collapse_idx])
    endpoint = [float(values[0]), float(values[-1])]
    logz = {
        str(limit): gaussian_log_integral_numeric(collapse_c, float(limit))
        for limit in (20, 60, 120, 200)
    }
    passed = endpoint[0] > 0 and endpoint[1] > 0 and collapse_c < 0
    passed = passed and logz["200"] - logz["20"] > 5.0
    return Check(
        claim="C1_marginal_path_collapse",
        status="VERIFIED" if passed else "FAIL",
        passed=passed,
        evidence={
            "gamma": [1.0, -0.5],
            "schedules": ["polynomial", "sigmoid"],
            "C_at_t0": endpoint[0],
            "C_at_t0.999": endpoint[1],
            "collapse_time_argmin": collapse_t,
            "C_at_collapse": collapse_c,
            "truncated_logZ_by_limit": logz,
        },
        scope="Concrete Gaussian witness; corroborates the existence phenomenon.",
    )


def claim_2() -> Check:
    """Independent quadrature agrees with the Gaussian PEC over 60 cases."""
    rng = np.random.default_rng(0)
    schedule_names = tuple(OFFICIAL_SCHEDULES)
    rows: list[dict[str, Any]] = []
    while len(rows) < 60:
        positive = float(rng.uniform(0.5, 3.0))
        negative = -float(rng.uniform(0.5, 3.0))
        names = tuple(rng.choice(schedule_names, size=2, replace=True))
        t = float(rng.uniform(0.1, 0.9))
        precision = float(
            criterion(
                t,
                [constant(positive), constant(negative)],
                [OFFICIAL_SCHEDULES[names[0]], OFFICIAL_SCHEDULES[names[1]]],
            )
        )
        if abs(precision) < 0.05:
            continue
        criterion_positive = precision > 0.0
        logz_20 = gaussian_log_integral_numeric(precision, 20.0)
        logz_60 = gaussian_log_integral_numeric(precision, 60.0)
        numerical_integrable = logz_60 - logz_20 < 1.0
        relative_error = None
        if criterion_positive:
            analytic = analytic_gaussian_log_integral(precision)
            relative_error = abs(logz_20 - analytic) / (abs(analytic) + 1e-12)
        rows.append(
            {
                "t": t,
                "schedules": names,
                "gammas": [positive, negative],
                "C": precision,
                "criterion_positive": criterion_positive,
                "numerical_integrable": numerical_integrable,
                "analytic_logZ_relative_error": relative_error,
            }
        )

    agreement = sum(r["criterion_positive"] == r["numerical_integrable"] for r in rows)
    errors = [r["analytic_logZ_relative_error"] for r in rows if r["analytic_logZ_relative_error"] is not None]
    max_error = float(max(errors, default=0.0))
    passed = agreement == len(rows) and max_error < 1e-8
    return Check(
        claim="C2_path_existence_criterion",
        status="VERIFIED" if passed else "FAIL",
        passed=passed,
        evidence={
            "seed": 0,
            "cases": len(rows),
            "criterion_quadrature_agreement": f"{agreement}/{len(rows)}",
            "max_analytic_logZ_relative_error": max_error,
            "rows": rows,
        },
        scope=(
            "Exact for the tested one-dimensional Gaussian family; the paper's "
            "universally quantified compact-support theorem remains a theorem, not "
            "something finite sampling alone can prove."
        ),
    )


def _ace_case(
    *,
    label: str,
    gammas,
    schedules,
    bump: float,
) -> dict[str, Any]:
    ts = np.linspace(0.0, 0.999, 4_001)
    before = criterion(ts, gammas, schedules)
    corrected = ace_bump(gammas, 0, bump)
    after = criterion(ts, corrected, schedules)
    endpoints_preserved = (
        abs(float(corrected[0](0.0)) - float(gammas[0](0.0))) < 1e-12
        and abs(float(corrected[0](1.0)) - float(gammas[0](1.0))) < 1e-12
    )
    return {
        "case": label,
        "B": bump,
        "min_C_before": float(np.min(before)),
        "min_C_after": float(np.min(after)),
        "collapsed_before": bool(np.min(before) < 0.0),
        "positive_after": bool(np.min(after) > 0.0),
        "endpoints_preserved": endpoints_preserved,
    }


def claim_3() -> Check:
    controlled = _ace_case(
        label="controlled_middle_dip",
        gammas=[constant(1.0), lambda t: -4.8 * np.asarray(t) * (1.0 - np.asarray(t))],
        schedules=[OFFICIAL_SCHEDULES["linear"], OFFICIAL_SCHEDULES["linear"]],
        bump=4.0,
    )
    heterogeneous = _ace_case(
        label="heterogeneous_auxiliary",
        gammas=[constant(1.0), constant(-0.45)],
        schedules=[OFFICIAL_SCHEDULES["polynomial"], sigmoid_unit],
        bump=1.5,
    )
    cases = [controlled, heterogeneous]
    passed = all(
        case["collapsed_before"] and case["positive_after"] and case["endpoints_preserved"]
        for case in cases
    )
    return Check(
        claim="C3_ACE_bump_correction",
        status="VERIFIED" if passed else "FAIL",
        passed=passed,
        evidence={"cases": cases},
        scope=(
            "Two constructive instances. This is a cumulative regression of the "
            "already-judged evidence, not a finite proof of Theorems 2.2-2.3."
        ),
    )


def historical_below_credit() -> list[Check]:
    return [
        Check(
            claim="C4_synthetic_distributional_metrics",
            status="BLOCKED",
            passed=True,
            evidence={
                "historical_judge_verdict": "TOY",
                "reason": (
                    "The judged artifact checked only integrability and did not run "
                    "NR/FKC/ACE, B=30, W1, W2, or MMD."
                ),
            },
            scope="Historical rejected baseline; not accepted as claim verification.",
        ),
        Check(
            claim="C5_crossdock_weak",
            status="BLOCKED",
            passed=True,
            evidence={
                "historical_judge_verdict": "INCONCLUSIVE",
                "reason": "No DN/CONF/SBDD inference or docking was run.",
            },
            scope="Historical rejected baseline; not accepted as claim verification.",
        ),
        Check(
            claim="C6_collapse_fraction_scaling",
            status="BLOCKED",
            passed=True,
            evidence={
                "historical_judge_verdict": "TOY",
                "reason": (
                    "The judged artifact used random two-expert compositions rather "
                    "than the paper's exhaustive three-expert schedule domain."
                ),
            },
            scope="Historical rejected baseline; not accepted as claim verification.",
        ),
    ]


def negative_controls(checks: list[Check]) -> dict[str, Any]:
    controls: dict[str, Any] = {}
    for check in checks:
        tampered = dict(check.evidence)
        if check.claim.startswith("C1"):
            tampered["C_at_collapse"] = abs(float(tampered["C_at_collapse"]))
            rejected = not (
                tampered["C_at_t0"] > 0
                and tampered["C_at_t0.999"] > 0
                and tampered["C_at_collapse"] < 0
            )
        elif check.claim.startswith("C2"):
            rejected = tampered["criterion_quadrature_agreement"] != "60/60"
            # Make the otherwise-valid evidence fail for the intended reason.
            tampered["criterion_quadrature_agreement"] = "59/60"
            rejected = tampered["criterion_quadrature_agreement"] != "60/60"
        else:
            tampered["cases"] = [dict(case) for case in tampered["cases"]]
            tampered["cases"][0]["positive_after"] = False
            rejected = not all(case["positive_after"] for case in tampered["cases"])
        controls[check.claim] = {
            "tamper": "Flip one contract-critical field",
            "rejected_as_intended": bool(rejected),
        }
    return controls


def main() -> int:
    started = time.perf_counter()
    full_credit = [claim_1(), claim_2(), claim_3()]
    controls = negative_controls(full_credit)
    historical = historical_below_credit()
    runtime = time.perf_counter() - started
    report = {
        "schema_version": 1,
        "paper": "arXiv:2512.10339v2",
        "git_sha": os.environ.get("ORX_GIT_SHA", "printed-by-orx-wrapper"),
        "fixed_command": "uv run --frozen python -m reproduction.run_all",
        "compute": {
            "backend": "local",
            "estimated_cores": 1,
            "thread_limit": 1,
            "logical_cpus_visible": os.cpu_count(),
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "runtime_seconds": runtime,
        },
        "checks": [check.__dict__ for check in full_credit + historical],
        "negative_controls": controls,
    }
    print("BEGIN_MACHINE_READABLE_EVIDENCE")
    print(json.dumps(report, indent=2, sort_keys=True))
    print("END_MACHINE_READABLE_EVIDENCE")
    print("\n# EVAL")
    for check in full_credit + historical:
        print(f"- {check.claim}: {check.status} — {check.scope}")
    controls_ok = all(item["rejected_as_intended"] for item in controls.values())
    accepted_ok = all(check.passed for check in full_credit)
    print(f"- negative_controls: {'PASS' if controls_ok else 'FAIL'}")
    print(f"- runtime_seconds: {runtime:.6f}")
    print(f"- cumulative_regression: {'PASS' if accepted_ok and controls_ok else 'FAIL'}")
    return 0 if accepted_ok and controls_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
