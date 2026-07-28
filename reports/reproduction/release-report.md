Previous live judged score: `8/12`

Conservative projected score range after the proposed change: `8–10/12`

Best-supported possible new score: `10/12` — forecast only, not a judge result

# Final reproduction release report

The evaluator artifact was published additively to the existing
`DineshAI/emv2qsi3TG` Space at revision
[`0f454af2035b713178122b8bd6129cc74e50e11f`](https://huggingface.co/spaces/DineshAI/emv2qsi3TG/commit/0f454af2035b713178122b8bd6129cc74e50e11f).
The paper is **awaiting the live judge**. No score increase is claimed.

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 2 | 2 | HIGH | VERIFIED | Constructive Gaussian collapse witness passes; existing full credit should remain. |
| 2 | 2 | 2 | HIGH | VERIFIED | Criterion/quadrature agreement 60/60 with \(4.11\times10^{-15}\) maximum relative error; existing full credit should remain. |
| 3 | 2 | 2 | HIGH | VERIFIED | Two ACE corrections restore positivity and preserve endpoints; existing full credit should remain. |
| 4 | 1 | 1 | LOW | BLOCKED | Exact five-seed checkpoints/samples are absent and the released evaluator is CUDA-only. Four distinct routes, including falsification, found no faithful verdict. Historical toy credit is not promoted. |
| 5 | 0 | 0 | LOW | BLOCKED | Exact CrossDock-Weak tasks/samples are absent and the public runner targets a different benchmark. Four distinct routes found no faithful replay or counterexample. |
| 6 | 1 | 2 | HIGH | VERIFIED | Exact exhaustive counts `[41,47,52,66,77,80]` and all 600 independent classifications match. Judge treatment is the remaining risk. |

Current total score: **8/12**. Conservative projected total: **8–10/12**.
Best-supported possible total: **10/12**. Claim 6 is the only claim for which
new full credit is forecast. Claims 4 and 5 remain BLOCKED.

## What changed

- Claims 1–3: preserved and rerun in every cumulative suite.
- Claim 4: the rejected integrability proxy is no longer presented as current
  Table 2 verification; four route records identify the exact unblockers.
- Claim 5: four route records replace the prior bare deferral and distinguish
  missing capability from falsification.
- Claim 6: replaced 300 random two-expert compositions with the exact
  five-schedule ordered-triplet finite domain and independent dense-grid
  checker.
- Evaluator surface: current evidence now appears first; old pages are labeled
  exactly **Historical rejected baseline**.

## Experiment tree

| Node | Branch | Git SHA | Formal result |
|---|---|---|---|
| Judged baseline | `orx/judged-8-of-12-baseline` | `3e45e3fbe8293edbadd193abf9b2e22f2e306773` | Claims 1–3 pass; 25 s |
| Exact Claim 6 | `orx/exact-schedule-triplet-collapse-prevalence` | `a06e981cfa6ebb7cb38c92409156ecc6ae95bb4f` | Exact Table E.5 match; 20 s |
| Availability/falsification audit | `orx/exact-claim-availability-and-falsification-audit` | `7f03a7485362f580f6dad02b7de9f5e156d9262e` | Claims 4–5 BLOCKED after four routes; 40 s |
| Winning release candidate | `orx/evaluator-visible-release-candidate` | `f82785a19241dc5f0b7b995f3bc31acb798dd65f` | Cumulative PASS; 25 s |

Every node used exactly:

```bash
uv run --frozen python -m reproduction.run_all
```

## Compute and cost

Each formal run was estimated at one CPU core and under five minutes, so the
authorized local backend was used. Actual numerical code was capped at one
thread; no GPU or Hugging Face compute job was used.

| Run | Backend | Actual allocation | Wall time | Numerical-check time |
|---|---|---|---:|---:|
| baseline | local | 1 CPU thread | 25 s | 0.026558 s |
| exact Claim 6 | local | 1 CPU thread | 20 s | 0.034820 s |
| audit | local | 1 CPU thread | 40 s | 0.048119 s |
| release candidate | local | 1 CPU thread | 25 s | 0.045605 s |

Remote CPU/GPU cost: **$0**. Local billed cost: **$0**.

## Release validation

- Fixed command regenerates all raw claim output: PASS.
- Cumulative Claims 1–3 regression: PASS.
- Exact Claim 6 reference and independent check: PASS.
- All six negative controls reject: PASS.
- `marimo check notebooks/collapse_reproduction.py`: PASS.
- Candidate JSON validity: PASS.
- Text-only upload allowlist: 31 files.
- Secret-pattern scan: zero hits.
- Judged/published subset: all 15 judged repository paths remain present.
- Protected historical hashes: zero changes.
- Uploaded-file hashes after redownload: 31/31 match.
- Evaluator-blind round 1: FAIL on four stale image links and two wording
  gaps; all six issues fixed.
- Evaluator-blind round 2: PASS, 33 files opened, zero missing/failures.
- Post-publication round 3: PASS, 33 files opened, zero missing/failures.
- Interactive CSS/JavaScript rendering: not exercised because no browser
  runtime was available. The unchanged historical web shell, navigation
  routes, raw links, and SVG XML were validated statically.

The initial local subset count of 48 included 33 Hugging Face download-cache
metadata files. The corrected repository-only count is 15; this is the count
used for post-publication validation.

## Evidence paths

- Illustrated report: `reports/reproduction/report.md`
- Tutorial notebook: `notebooks/collapse_reproduction.py`
- Executable verifier: `reproduction/run_all.py`
- Mathematical implementation: `reproduction/core.py`
- Internal contracts: `.openresearch/artifacts/claim_*/`
- Space canonical page: `space/pages/current/page.md`
- Per-claim pages: `space/pages/claims/claim-*/page.md`
- Combined raw output: `space/evidence/current_results.json`
- Claim 2 raw cases: `space/evidence/claim_2_cases.csv`
- Claim 6 raw counts: `space/evidence/claim_6_counts.csv`
- Visibility matrix: `space/pages/visibility/page.md`
- Upload allowlist: `release/hf_upload_allowlist.txt`
- Upload hashes: `release/hf_upload_manifest.sha256`
- Blind reviews: `release/red_team_round1.md`,
  `release/red_team_round2.md`, and
  `release/post_publication_red_team.md`

## Exact Hugging Face upload allowlist

```text
README.md
evidence/c1.json
evidence/c2.json
evidence/c3.json
evidence/c4.json
evidence/c5.json
evidence/c6.json
evidence/claim_2_cases.csv
evidence/claim_6_counts.csv
evidence/code/.python-version
evidence/code/core.py
evidence/code/pyproject.toml
evidence/code/run_all.py
evidence/code/uv.lock
evidence/current_results.json
images/blocked_asset_matrix.svg
images/correction_claim3.svg
images/headline_claim6.svg
images/mechanism_claim1.svg
logbook.json
pages/claims/claim-1/page.md
pages/claims/claim-2/page.md
pages/claims/claim-3/page.md
pages/claims/claim-4/page.md
pages/claims/claim-5/page.md
pages/claims/claim-6/page.md
pages/current/page.md
pages/index.md
pages/method/page.md
pages/report/page.md
pages/visibility/page.md
```

No deletion operation was issued. The failed first `hf upload` attempt changed
nothing; it was rejected during an unnecessary repository-creation check.
Publication then used the installed Hugging Face client's direct
`create_commit` API with only the 31 allowlisted text files.

## Material command record

Startup and source audit:

```bash
orx skill
orx skill orx-experiment-tree
orx skill orx-evidence
orx skill orx-git
orx skill orx-compute
orx skill orx-reports
orx projects --json
orx runs 6a84d23b-2261-4eae-8984-3e04cf610cda
orx project view 6a84d23b-2261-4eae-8984-3e04cf610cda
git branch -a
git status --short
git rev-parse HEAD
df -h .
orx paper 2512.10339 --full
curl -A "OpenResearch reproduction audit" https://ar5iv.labs.arxiv.org/html/2512.10339
sha256sum 2512.10339.html
hf auth whoami
hf download DineshAI/emv2qsi3TG --repo-type space --revision 9b6992fe238baa9afd6dae07652bae88a9c53bad
```

Tree, commit, and formal runs:

```bash
orx create-experiment 6a84d23b-2261-4eae-8984-3e04cf610cda --title "Judged 8-of-12 baseline" --run-command "uv run --frozen python -m reproduction.run_all"
orx create-experiment 6a84d23b-2261-4eae-8984-3e04cf610cda --title "Exact schedule-triplet collapse prevalence" --parent 9f04fe1b-9359-48b8-b66d-a9d78c9c55bc
orx create-experiment 6a84d23b-2261-4eae-8984-3e04cf610cda --title "Exact-claim availability and falsification audit" --parent 6f6dc783-efb1-43c3-8165-948dee076224
orx create-experiment 6a84d23b-2261-4eae-8984-3e04cf610cda --title "Evaluator-visible release candidate" --parent 685936f7-0a87-48f8-8b14-ff54bf450d78
orx project edit 6a84d23b-2261-4eae-8984-3e04cf610cda --run-command "uv run --frozen python -m reproduction.run_all"
orx exp run 9f04fe1b-9359-48b8-b66d-a9d78c9c55bc --backend local
orx exp run 6f6dc783-efb1-43c3-8165-948dee076224 --backend local
orx exp run 685936f7-0a87-48f8-8b14-ff54bf450d78 --backend local
orx exp run 07baf3f8-17da-4372-844a-94c48fc67930 --backend local
orx exp wait 07baf3f8-17da-4372-844a-94c48fc67930 --timeout 480
orx logs cb5433fc-5010-486b-97db-51c43f42d96a --bytes 200000
```

Artifact and release validation:

```bash
uv run --frozen python scripts/export_evaluator_evidence.py space/evidence
uv run --frozen python scripts/make_report_figures.py reports/reproduction/images space/images <dashboard-files-images>
uv run --frozen marimo check notebooks/collapse_reproduction.py
uv run --frozen python scripts/validate_release.py --judged <judged-revision> --overlay space --candidate <fresh-candidate> --release-dir release
uv run --frozen python scripts/red_team_candidate.py --candidate <fresh-candidate> --output release/red_team_round2.md --round 2
git commit -m "Publish evaluator-visible reproduction evidence"
git push origin orx/evaluator-visible-release-candidate
```

Publication and verification:

```bash
hf upload DineshAI/emv2qsi3TG space . --repo-type space <exact includes> --commit-message "Publish exact collapse-prevalence reproduction evidence"
# The preceding command was rejected before mutation by the repository-create rate limit.
/opt/homebrew/opt/python@3.14/bin/python3.14 <direct-create_commit-script>
hf download DineshAI/emv2qsi3TG --repo-type space --revision 0f454af2035b713178122b8bd6129cc74e50e11f --local-dir <fresh-directory>
uv run --frozen python scripts/red_team_candidate.py --candidate <fresh-published-revision> --output <post-publication-red-team> --round 3
curl https://huggingface.co/api/spaces/DineshAI/emv2qsi3TG
git ls-remote origin refs/heads/main
```

Angle-bracket values are paths or generated include lists recorded by the
adjacent manifest; no credential, token value, or generated wrapper is
included. Incidental read-only `rg`, `sed`, `find`, `git diff`, JSON formatting,
image inspection, and file-size commands did not affect evidence or external
state.

## Publication action

Completed action: additive text-only update to the existing Space, followed by
exact-revision redownload and validation. The reader-facing README, report,
notebook, verifier, and exact published Space text mirror are committed to
GitHub `main`. The next external action is the live judge's evaluation; no
second Space or score claim will be made.
