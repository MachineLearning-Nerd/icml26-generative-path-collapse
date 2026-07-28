"""Assemble and validate an additive, evaluator-visible Space candidate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


OVERRIDDEN_HISTORICAL_PATHS = {"README.md", "logbook.json", "pages/index.md"}
TEXT_SUFFIXES = {".md", ".json", ".csv", ".py", ".toml", ".svg", ".lock"}
TEXT_NAMES = {".python-version"}
SECRET_PATTERNS = (
    re.compile(rb"hf_[A-Za-z0-9]{20,}"),
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(rb"(?i)(?:api[_-]?key|access[_-]?token|secret)\s*[:=]\s*['\"][^'\"]{12,}"),
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def files_under(root: Path) -> dict[str, Path]:
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
    }


def validate_links(candidate: Path, manifest: dict[str, object]) -> list[str]:
    slugs: set[str] = set()

    def collect(node: dict[str, object]) -> None:
        slugs.add(str(node["slug"]))
        for child in node.get("children", []):
            collect(child)

    collect(manifest["root"])
    problems: list[str] = []
    for rel, path in files_under(candidate).items():
        if path.suffix != ".md":
            continue
        text = path.read_text()
        for target in MARKDOWN_LINK.findall(text):
            target = target.split("#", 1)[0] if not target.startswith("#/") else target
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#/"):
                if target[2:] not in slugs:
                    problems.append(f"{rel}: missing route {target}")
                continue
            clean = target.split("?", 1)[0]
            if re.fullmatch(r"-?\d+(?:\.\d+)?", clean):
                continue
            if not (candidate / clean).is_file():
                problems.append(f"{rel}: missing root-relative asset {clean}")
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--judged", required=True, type=Path)
    parser.add_argument("--overlay", required=True, type=Path)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--release-dir", required=True, type=Path)
    args = parser.parse_args()

    if args.candidate.exists():
        raise SystemExit("candidate directory must be fresh and absent")
    shutil.copytree(args.judged, args.candidate)
    for rel, source in files_under(args.overlay).items():
        target = args.candidate / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)

    old_files = files_under(args.judged)
    candidate_files = files_under(args.candidate)
    missing_old = sorted(set(old_files) - set(candidate_files))
    if missing_old:
        raise SystemExit(f"historical subset failure ({len(missing_old)} missing)")
    changed_protected = [
        rel
        for rel, old_path in old_files.items()
        if rel not in OVERRIDDEN_HISTORICAL_PATHS
        and digest(old_path) != digest(candidate_files[rel])
    ]
    if changed_protected:
        raise SystemExit(
            f"historical protected-file hash failure ({len(changed_protected)} changed)"
        )

    overlay_files = files_under(args.overlay)
    non_text = sorted(
        rel
        for rel, path in overlay_files.items()
        if path.suffix not in TEXT_SUFFIXES and path.name not in TEXT_NAMES
    )
    if non_text:
        raise SystemExit(f"non-text upload rejected ({len(non_text)} files)")

    secret_hits = []
    for rel, path in overlay_files.items():
        content = path.read_bytes()
        if any(pattern.search(content) for pattern in SECRET_PATTERNS):
            secret_hits.append(rel)
    if secret_hits:
        raise SystemExit(f"possible secret material rejected ({len(secret_hits)} files)")

    manifest = json.loads((args.candidate / "logbook.json").read_text())
    for rel, path in candidate_files.items():
        if path.suffix == ".json":
            json.loads(path.read_text())
    link_problems = validate_links(args.candidate, manifest)
    if link_problems:
        raise SystemExit("\n".join(link_problems))

    args.release_dir.mkdir(parents=True, exist_ok=True)
    allowlist = sorted(overlay_files)
    (args.release_dir / "hf_upload_allowlist.txt").write_text(
        "\n".join(allowlist) + "\n"
    )
    (args.release_dir / "hf_upload_manifest.sha256").write_text(
        "".join(f"{digest(overlay_files[rel])}  {rel}\n" for rel in allowlist)
    )
    summary = {
        "candidate_file_count": len(candidate_files),
        "historical_file_count": len(old_files),
        "historical_paths_missing": 0,
        "protected_historical_files_changed": 0,
        "upload_file_count": len(allowlist),
        "upload_text_only": True,
        "json_valid": True,
        "link_problems": 0,
        "secret_pattern_hits": 0,
    }
    (args.release_dir / "validation_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
