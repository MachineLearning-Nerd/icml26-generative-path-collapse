"""Export evaluator-visible, machine-readable evidence from the tested verifier."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from reproduction.run_all import (
    blocked_claim_audits,
    claim_1,
    claim_2,
    claim_3,
    claim_6,
    negative_controls,
)


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def export(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    verified = [claim_1(), claim_2(), claim_3()]
    claim_6_check, claim_6_control = claim_6()
    blocked, blocked_controls = blocked_claim_audits()
    ordered = verified + blocked + [claim_6_check]
    controls = negative_controls(verified)
    controls[claim_6_check.claim] = claim_6_control
    controls.update(blocked_controls)

    write_json(
        output / "current_results.json",
        {
            "schema_version": 1,
            "paper": "arXiv:2512.10339v2",
            "fixed_command": "uv run --frozen python -m reproduction.run_all",
            "tested_verifier_git_sha": (
                "7f03a7485362f580f6dad02b7de9f5e156d9262e"
            ),
            "formal_run_id": "5cc88562-1ec4-48ed-b027-8658778d4d3b",
            "formal_run_duration_seconds": 40,
            "formal_scientific_runtime_seconds": 0.048119209008291364,
            "estimated_cpu_cores": 1,
            "thread_limit": 1,
            "logical_cpus_visible": 8,
            "checks": [check.__dict__ for check in ordered],
            "negative_controls": controls,
        },
    )
    for check in ordered:
        claim_number = check.claim.split("_", 1)[0].lower()
        write_json(
            output / f"{claim_number}.json",
            {
                "check": check.__dict__,
                "negative_control": controls[check.claim],
                "fixed_command": "uv run --frozen python -m reproduction.run_all",
                "tested_verifier_git_sha": (
                    "7f03a7485362f580f6dad02b7de9f5e156d9262e"
                ),
            },
        )
    with (output / "claim_2_cases.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "t",
                "schedule_1",
                "schedule_2",
                "gamma_1",
                "gamma_2",
                "C",
                "criterion_positive",
                "numerical_integrable",
                "analytic_logZ_relative_error",
            ],
        )
        writer.writeheader()
        for row in verified[1].evidence["rows"]:
            writer.writerow(
                {
                    "t": row["t"],
                    "schedule_1": row["schedules"][0],
                    "schedule_2": row["schedules"][1],
                    "gamma_1": row["gammas"][0],
                    "gamma_2": row["gammas"][1],
                    "C": row["C"],
                    "criterion_positive": row["criterion_positive"],
                    "numerical_integrable": row["numerical_integrable"],
                    "analytic_logZ_relative_error": (
                        ""
                        if row["analytic_logZ_relative_error"] is None
                        else row["analytic_logZ_relative_error"]
                    ),
                }
            )
    with (output / "claim_6_counts.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "guidance_weight",
                "eligible_triplets",
                "paper_collapses",
                "reference_collapses",
                "independent_collapses",
                "fraction",
                "classification_sha256",
            ],
        )
        writer.writeheader()
        for reference, independent in zip(
            claim_6_check.evidence["reference_checker_rows"],
            claim_6_check.evidence["independent_checker_rows"],
            strict=True,
        ):
            writer.writerow(
                {
                    "guidance_weight": reference["guidance_weight"],
                    "eligible_triplets": reference["eligible_triplets"],
                    "paper_collapses": reference["expected_collapses"],
                    "reference_collapses": reference["observed_collapses"],
                    "independent_collapses": independent["observed_collapses"],
                    "fraction": reference["observed_fraction"],
                    "classification_sha256": reference["classification_sha256"],
                }
            )

    code_dir = output / "code"
    code_dir.mkdir(exist_ok=True)
    for source in (
        Path("reproduction/core.py"),
        Path("reproduction/run_all.py"),
        Path("pyproject.toml"),
        Path("uv.lock"),
        Path(".python-version"),
    ):
        shutil.copy2(source, code_dir / source.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    export(args.output)


if __name__ == "__main__":
    main()
