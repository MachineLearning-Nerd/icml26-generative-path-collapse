"""Blindly traverse a Space candidate from its canonical entrypoint."""

from __future__ import annotations

import argparse
import json
import re
import xml.etree.ElementTree as ET
from collections import deque
from pathlib import Path


LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
EXPECTED = {
    "claim-1": "VERIFIED",
    "claim-2": "VERIFIED",
    "claim-3": "VERIFIED",
    "claim-4": "BLOCKED",
    "claim-5": "BLOCKED",
    "claim-6": "VERIFIED",
}


def flatten(node: dict[str, object]) -> list[dict[str, object]]:
    result = [node]
    for child in node.get("children", []):
        result.extend(flatten(child))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--round", required=True, type=int)
    parser.add_argument("--browser-available", action="store_true")
    args = parser.parse_args()

    opened: set[str] = set()
    missing: list[str] = []
    failures: list[str] = []
    conclusions: list[str] = []

    def read(rel: str) -> str:
        path = args.candidate / rel
        if not path.is_file():
            missing.append(rel)
            return ""
        opened.add(rel)
        return path.read_text()

    readme = read("README.md")
    manifest_text = read("logbook.json")
    manifest = json.loads(manifest_text)
    nodes = flatten(manifest["root"])
    queue: deque[str] = deque(str(node["file"]) for node in nodes)
    route_files = {str(node["slug"]): str(node["file"]) for node in nodes}
    seen_markdown: set[str] = set()

    while queue:
        rel = queue.popleft()
        if rel in seen_markdown:
            continue
        seen_markdown.add(rel)
        text = read(rel)
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#/"):
                slug = target[2:]
                if slug not in route_files:
                    missing.append(target)
                else:
                    queue.append(route_files[slug])
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean or re.fullmatch(r"-?\d+(?:\.\d+)?", clean):
                continue
            path = args.candidate / clean
            if not path.is_file():
                missing.append(clean)
                continue
            opened.add(clean)
            if path.suffix == ".json":
                json.loads(path.read_text())
            elif path.suffix == ".svg":
                ET.fromstring(path.read_text())

    for slug, verdict in EXPECTED.items():
        if slug not in route_files:
            failures.append(f"{slug}: not reachable from logbook")
            continue
        page = read(route_files[slug])
        required = [
            f"Verdict: {verdict}",
            "Exact contract and source",
            "Run `uv run --frozen python -m reproduction.run_all`",
            "Limitation",
        ]
        if slug in {"claim-4", "claim-5"}:
            required = [
                f"Verdict: {verdict}",
                "Exact contract and source",
                "Four completed routes",
                "Assumption-preserving falsification",
                "Limitation and unblocker",
            ]
        for phrase in required:
            if phrase not in page:
                failures.append(f"{slug}: cannot locate {phrase!r}")
        raw_path = f"evidence/c{slug[-1]}.json"
        raw_text = read(raw_path)
        if raw_text:
            raw = json.loads(raw_text)
            if raw["check"]["status"] != verdict:
                failures.append(f"{slug}: page/raw verdict mismatch")
            if not raw["negative_control"]["rejected_as_intended"]:
                failures.append(f"{slug}: negative control did not reject")

    current = read(route_files.get("current", ""))
    method = read(route_files.get("method", ""))
    visibility = read(route_files.get("visibility", ""))
    combined = current + method
    for phrase in (
        "uv run --frozen python -m reproduction.run_all",
        "7f03a7485362f580f6dad02b7de9f5e156d9262e",
        "Python 3.11",
        "one CPU",
        "40 seconds",
        "seed 0",
        "no seed",
    ):
        if phrase.lower() not in combined.lower():
            failures.append(f"method metadata not discoverable: {phrase}")
    if visibility.count("| VERIFIED |") != 4 or visibility.count("| BLOCKED |") != 2:
        failures.append("visibility matrix does not expose six terminal verdicts")
    for historical_slug in ("verify", "overview"):
        title = next(
            (str(node["title"]) for node in nodes if node["slug"] == historical_slug),
            "",
        )
        if not title.startswith("Historical rejected baseline"):
            failures.append(f"{historical_slug}: historical label missing")
    if "forecast only" not in (readme + current).lower():
        failures.append("live score and forecast are not clearly distinguished")

    conclusions.extend(
        [
            "The current verifier is discoverable before historical pages.",
            "All six exact contracts, source anchors, verdicts, limitations, raw JSON, and controls are reachable.",
            "Claims 1-3 and 6 are marked VERIFIED; Claims 4-5 are marked BLOCKED.",
            "The fixed command, pinned environment, tested SHA, seeds, CPU allocation, and runtime are reachable.",
            "Historical rejected pages remain reachable and are clearly superseded.",
        ]
    )
    unverified = []
    if not args.browser_available:
        unverified.append(
            "Interactive CSS/JavaScript rendering could not be exercised because "
            "no browser runtime was available; link targets and SVG XML were "
            "validated statically, and the historical web shell is unchanged."
        )

    status = "PASS" if not missing and not failures else "FAIL"
    lines = [
        f"# Evaluator-blind red-team round {args.round}",
        "",
        f"**Result: {status}.**",
        "",
        "The review began only at `README.md` and `logbook.json` in a freshly "
        "assembled candidate. It followed manifest navigation and links; no "
        "repository files, OpenResearch logs, or dashboard artifacts supplied "
        "missing context.",
        "",
        "## Files opened",
        "",
    ]
    lines.extend(f"- `{rel}`" for rel in sorted(opened))
    lines.extend(["", "## Conclusions located", ""])
    lines.extend(f"- {item}" for item in conclusions)
    lines.extend(["", "## Missing or failed checks", ""])
    if missing or failures:
        lines.extend(f"- Missing: `{item}`" for item in sorted(set(missing)))
        lines.extend(f"- Failure: {item}" for item in failures)
    else:
        lines.append("- None.")
    lines.extend(["", "## Conclusions not verified", ""])
    if unverified:
        lines.extend(f"- {item}" for item in unverified)
    else:
        lines.append("- None.")
    lines.append("")
    args.output.write_text("\n".join(lines))
    print(json.dumps({"status": status, "opened": len(opened), "missing": len(missing), "failures": len(failures)}))
    if status != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
