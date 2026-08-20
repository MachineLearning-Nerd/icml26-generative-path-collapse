# Branch audit

This repository was migrated from opaque OpenResearch-generated branch names to descriptive branches. The clean branches preserve the corresponding baseline, audit, and release snapshots.

## Mapping

| Former branch | Clean branch | Purpose |
| --- | --- | --- |
| `orx/judged-8-of-12-baseline` | `historical/judged-baseline` | Preserve the accepted 8/12 baseline and originally judged evidence. |
| `orx/exact-schedule-triplet-collapse-prevalence` | `audit/claim6-schedule-enumeration` | Replace the Claim 6 proxy with the exact five-schedule, three-expert enumeration. |
| `orx/exact-claim-availability-and-falsification-audit` | `audit/claims4-5-availability` | Audit four routes each for the blocked Claims 4–5. |
| `orx/evaluator-visible-release-candidate` | `release/evaluator-candidate` | Package evaluator-visible pages, raw evidence, report, notebook, and release validation. |
| `main` | `main` | Cumulative publication surface. |

## Migration guarantees

- Every live branch contains the current README and this branch audit.
- All reachable commits are attributed to `MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`.
- Former `orx/*` remote branches are deleted after their clean replacements are published.
- Active report and README links use the renamed repository and clean branch names.
- Historical evaluator metadata and the DineshAI Space identifier are preserved as provenance, not as GitHub ownership or branch names.

## Verification checklist

```bash
git show-ref --verify refs/heads/<branch>
git show <branch>:README.md >/dev/null
git show <branch>:branch-audit.md >/dev/null
git log <branch> --format='%an <%ae>' | sort -u
```
