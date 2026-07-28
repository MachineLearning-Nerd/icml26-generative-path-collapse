# Evaluator-blind red-team round 3

**Result: PASS.**

The review began only at `README.md` and `logbook.json` in a freshly assembled candidate. It followed manifest navigation and links; no repository files, OpenResearch logs, or dashboard artifacts supplied missing context.

## Files opened

- `README.md`
- `evidence/c1.json`
- `evidence/c2.json`
- `evidence/c3.json`
- `evidence/c4.json`
- `evidence/c5.json`
- `evidence/c6.json`
- `evidence/claim_2_cases.csv`
- `evidence/claim_6_counts.csv`
- `evidence/code/.python-version`
- `evidence/code/core.py`
- `evidence/code/pyproject.toml`
- `evidence/code/run_all.py`
- `evidence/code/uv.lock`
- `evidence/current_results.json`
- `images/blocked_asset_matrix.svg`
- `images/correction_claim3.svg`
- `images/headline_claim6.svg`
- `images/mechanism_claim1.svg`
- `logbook.json`
- `pages/claims/claim-1/page.md`
- `pages/claims/claim-2/page.md`
- `pages/claims/claim-3/page.md`
- `pages/claims/claim-4/page.md`
- `pages/claims/claim-5/page.md`
- `pages/claims/claim-6/page.md`
- `pages/current/page.md`
- `pages/index.md`
- `pages/method/page.md`
- `pages/overview/page.md`
- `pages/report/page.md`
- `pages/verify/page.md`
- `pages/visibility/page.md`

## Conclusions located

- The current verifier is discoverable before historical pages.
- All six exact contracts, source anchors, verdicts, limitations, raw JSON, and controls are reachable.
- Claims 1-3 and 6 are marked VERIFIED; Claims 4-5 are marked BLOCKED.
- The fixed command, pinned environment, tested SHA, seeds, CPU allocation, and runtime are reachable.
- Historical rejected pages remain reachable and are clearly superseded.

## Missing or failed checks

- None.

## Conclusions not verified

- Interactive CSS/JavaScript rendering could not be exercised because no browser runtime was available; link targets and SVG XML were validated statically, and the historical web shell is unchanged.
