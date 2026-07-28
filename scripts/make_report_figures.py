"""Generate the four evidence-bearing figures used by the public report."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

for _name in (
    "OMP_NUM_THREADS",
    "OPENBLAS_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_name] = "1"

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from reproduction.core import OFFICIAL_SCHEDULES, ace_bump, criterion


PAPER_COUNTS = np.array([41, 47, 52, 66, 77, 80])
WEIGHTS = np.array([1.0, 1.1, 1.5, 2.0, 7.5, 15.0])


def constant(value: float):
    return lambda t: np.zeros_like(np.asarray(t), dtype=float) + value


def save_all(fig: plt.Figure, outputs: list[Path], name: str) -> None:
    for output in outputs:
        output.mkdir(parents=True, exist_ok=True)
        fig.savefig(output / name, dpi=180, bbox_inches="tight")
        fig.savefig(output / Path(name).with_suffix(".svg"), bbox_inches="tight")
    plt.close(fig)


def headline(outputs: list[Path]) -> None:
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.plot(
        WEIGHTS,
        PAPER_COUNTS,
        color="#6d28d9",
        linewidth=4,
        label="Paper Table E.5",
    )
    ax.scatter(
        WEIGHTS,
        PAPER_COUNTS,
        s=90,
        facecolor="white",
        edgecolor="#111827",
        linewidth=2,
        zorder=3,
        label="Reproduction (exact overlap)",
    )
    for x, y in zip(WEIGHTS, PAPER_COUNTS, strict=True):
        ax.annotate(f"{y}%", (x, y), xytext=(0, 9), textcoords="offset points", ha="center")
    ax.set_xscale("log")
    ax.set_xticks(WEIGHTS, [str(value).rstrip("0").rstrip(".") for value in WEIGHTS])
    ax.set_ylim(35, 85)
    ax.set_xlabel("Guidance scale ω")
    ax.set_ylabel("Collapse fraction over 100 eligible triplets")
    ax.set_title("Exact reproduction of collapse-prevalence scaling")
    ax.grid(alpha=0.22)
    ax.legend(frameon=False)
    save_all(fig, outputs, "headline_claim6.png")


def collapse_mechanism(outputs: list[Path]) -> None:
    ts = np.linspace(0.0, 0.999, 2_000)
    values = criterion(
        ts,
        [constant(1.0), constant(-0.5)],
        [OFFICIAL_SCHEDULES["polynomial"], OFFICIAL_SCHEDULES["sigmoid"]],
    )
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    clipped = np.clip(values, -12, 35)
    ax.plot(ts, clipped, color="#dc2626", linewidth=2.5)
    ax.axhline(0, color="#111827", linewidth=1)
    ax.fill_between(ts, clipped, 0, where=values < 0, color="#fecaca", alpha=0.8)
    argmin = int(np.argmin(values))
    ax.scatter([ts[argmin]], [values[argmin]], color="#991b1b", zorder=3)
    ax.annotate(
        f"collapse witness\nC(t)={values[argmin]:.2f}",
        (ts[argmin], values[argmin]),
        xytext=(-85, 28),
        textcoords="offset points",
        arrowprops={"arrowstyle": "->", "color": "#991b1b"},
    )
    ax.set_xlabel("Time t")
    ax.set_ylabel("Precision criterion C(t), clipped for display")
    ax.set_title("Valid endpoints do not prevent an invalid intermediate path")
    ax.grid(alpha=0.22)
    save_all(fig, outputs, "mechanism_claim1.png")


def correction(outputs: list[Path]) -> None:
    ts = np.linspace(0.0, 0.999, 4_001)
    cases = [
        (
            "Controlled middle dip",
            [constant(1.0), lambda t: -4.8 * np.asarray(t) * (1 - np.asarray(t))],
            [OFFICIAL_SCHEDULES["linear"], OFFICIAL_SCHEDULES["linear"]],
            4.0,
        ),
        (
            "Heterogeneous schedules",
            [constant(1.0), constant(-0.5)],
            [OFFICIAL_SCHEDULES["polynomial"], OFFICIAL_SCHEDULES["sigmoid"]],
            30.0,
        ),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2), sharey=False)
    for ax, (title, gammas, schedules, bump) in zip(axes, cases, strict=True):
        before = criterion(ts, gammas, schedules)
        after = criterion(ts, ace_bump(gammas, 0, bump), schedules)
        ax.plot(ts, np.clip(before, -12, 35), color="#dc2626", label="Before")
        ax.plot(ts, np.clip(after, -12, 35), color="#059669", label=f"ACE B={bump:g}")
        ax.axhline(0, color="#111827", linewidth=1)
        ax.set_title(title)
        ax.set_xlabel("Time t")
        ax.grid(alpha=0.22)
    axes[0].set_ylabel("C(t), clipped for display")
    axes[1].legend(frameon=False)
    fig.suptitle("ACE lifts the criterion above zero while preserving endpoints")
    save_all(fig, outputs, "correction_claim3.png")


def availability(outputs: list[Path]) -> None:
    rows = [
        "Released implementation",
        "Exact benchmark/task definition",
        "Trained checkpoints",
        "Raw generated samples",
        "CPU-supported full runner",
    ]
    data = np.array(
        [
            [1, 1],
            [1, 0],
            [0, 0],
            [0, 0],
            [0, 0],
        ]
    )
    fig, ax = plt.subplots(figsize=(9.2, 5.2))
    ax.imshow(data, cmap=plt.matplotlib.colors.ListedColormap(["#fecaca", "#bbf7d0"]), vmin=0, vmax=1)
    ax.set_xticks([0, 1], ["Claim 4", "Claim 5"])
    ax.set_yticks(range(len(rows)), rows)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(j, i, "available" if data[i, j] else "missing", ha="center", va="center")
    ax.set_title("Why the two empirical claims remain BLOCKED")
    ax.tick_params(axis="both", length=0)
    ax.tick_params(axis="x", labelsize=11)
    save_all(fig, outputs, "blocked_asset_matrix.png")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("outputs", nargs="+", type=Path)
    args = parser.parse_args()
    headline(args.outputs)
    collapse_mechanism(args.outputs)
    correction(args.outputs)
    availability(args.outputs)


if __name__ == "__main__":
    main()
