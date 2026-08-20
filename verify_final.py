"""Verify the standardized repository dossier and published branch surface."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_BRANCHES = {
    "audit/claim6-schedule-enumeration",
    "audit/claims4-5-availability",
    "historical/judged-baseline",
    "main",
    "release/evaluator-candidate",
}
EXPECTED_COMMITS = 16
CANONICAL_IDENTITY = "MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>"
EXPECTED_STATUSES = {
    "C1": "VERIFIED_SCOPED",
    "C2": "VERIFIED_SCOPED",
    "C3": "VERIFIED_SCOPED",
    "C4": "BLOCKED",
    "C5": "BLOCKED",
    "C6": "VERIFIED_SCOPED",
}


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"verification failed: {message}")


def published_branches() -> set[str]:
    try:
        lines = git("ls-remote", "--heads", "origin").splitlines()
    except subprocess.CalledProcessError:
        lines = []
    if lines:
        return {line.split("\t", 1)[1].removeprefix("refs/heads/") for line in lines}
    return set(git("for-each-ref", "--format=%(refname:short)", "refs/heads").splitlines())


def main() -> None:
    claims = json.loads((ROOT / "claims.json").read_text(encoding="utf-8"))
    verdicts = json.loads((ROOT / "reproduction_verdicts.json").read_text(encoding="utf-8"))
    manifest = json.loads((ROOT / "EVIDENCE_MANIFEST.json").read_text(encoding="utf-8"))
    logbook = json.loads((ROOT / "space/logbook.json").read_text(encoding="utf-8"))
    summary = json.loads((ROOT / "release/validation_summary.json").read_text(encoding="utf-8"))

    branches = published_branches()
    require(branches == EXPECTED_BRANCHES, "published branches")
    require(not any(branch.startswith("orx/") for branch in branches), "legacy orx branch")
    require(int(git("rev-list", "--all", "--count")) == EXPECTED_COMMITS, "reachable commit count")
    identities = git("log", "--all", "--format=%an <%ae>%n%cn <%ce>").splitlines()
    require(identities and all(identity == CANONICAL_IDENTITY for identity in identities), "canonical identity")

    require(verdicts["claim_statuses"] == EXPECTED_STATUSES, "verdict statuses")
    require(claims["overall_status"] == "PARTIAL_C1_C2_C3_C6_VERIFIED_C4_C5_BLOCKED", "claims overall status")
    require(verdicts["overall_verdict"] == claims["overall_status"], "verdict overall status")
    require(all((ROOT / path).exists() for path in manifest["required_paths"]), "manifest paths")
    require(summary == {
        "candidate_file_count": 43,
        "historical_file_count": 15,
        "historical_paths_missing": 0,
        "json_valid": True,
        "link_problems": 0,
        "protected_historical_files_changed": 0,
        "secret_pattern_hits": 0,
        "upload_file_count": 31,
        "upload_text_only": True,
    }, "release summary")

    required_routes = {
        "current": "pages/current/page.md",
        "claim-1": "pages/claims/claim-1/page.md",
        "claim-2": "pages/claims/claim-2/page.md",
        "claim-3": "pages/claims/claim-3/page.md",
        "claim-4": "pages/claims/claim-4/page.md",
        "claim-5": "pages/claims/claim-5/page.md",
        "claim-6": "pages/claims/claim-6/page.md",
    }
    routes: dict[str, str] = {}

    def collect(node: dict[str, object]) -> None:
        routes[str(node["slug"])] = str(node["file"])
        for child in node.get("children", []):
            collect(child)

    collect(logbook["root"])
    for slug, path in required_routes.items():
        require(routes.get(slug) == path and (ROOT / "space" / path).is_file(), f"route {slug}")

    for number, expected in enumerate(EXPECTED_STATUSES.values(), start=1):
        evidence = json.loads((ROOT / f"space/evidence/c{number}.json").read_text(encoding="utf-8"))
        require(evidence["check"]["status"] == expected.removesuffix("_SCOPED"), f"C{number} raw verdict")
        require(evidence["negative_control"]["rejected_as_intended"], f"C{number} negative control")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require("arXiv:2512.10339" in readme, "paper citation")
    require("Thank you" in readme, "thank-you note")
    require("forecast" in readme.lower(), "score forecast boundary")
    require("STATUS.md" in readme and "CLAIM_EVIDENCE.md" in readme, "dossier links")
    require("MachineLearning-Nerd@users.noreply.github.com" in (ROOT / "branch-audit.md").read_text(encoding="utf-8"), "branch identity documentation")

    print(
        "FINAL_AUDIT=VERIFIED "
        f"branches={len(EXPECTED_BRANCHES)} commits={EXPECTED_COMMITS} "
        "claims=C1:C2:C3:C6_verified_scoped,C4:C5_blocked "
        "historical_score=8/12 current_score_claim=false publication_allowed=false"
    )


if __name__ == "__main__":
    main()
