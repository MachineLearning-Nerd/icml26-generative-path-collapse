# Method, command, and provenance

## Fixed execution contract

```bash
uv run --frozen python -m reproduction.run_all
```

The command is identical on every experiment node. Parameters and claims live
in committed code, not environment-variable overrides. The visible
environment inputs are [.python-version](evidence/code/.python-version),
[pyproject.toml](evidence/code/pyproject.toml), and
[uv.lock](evidence/code/uv.lock). The implementation and executable verifier
are [core.py](evidence/code/core.py) and
[run_all.py](evidence/code/run_all.py).

The verifier exits nonzero if an accepted contract, independent check, or
negative control fails.

## Source audit

- Paper: `arXiv:2512.10339v2`
- Retrieved URL:
  `https://ar5iv.labs.arxiv.org/html/2512.10339`
- Retrieval UTC date: `2026-07-28`
- Retrieved HTML SHA-256:
  `1ea66da8241cfd6e4e4cf06c4a441218c53ee72b49da82c388436d842cb74f81`
- Anchors: Theorems 2.1–2.3 `S2.Thmtheorem1` through
  `S2.Thmtheorem3`; Table 2 `S3.T2`; Table 3 `S3.T3`; synthetic protocol
  `A3.SS1`; prevalence `A5.SS2`.
- Official code:
  `ziseoklee/ACE@66534202cb255b6891d5dcbe2e9e18af88ff5615`
- Tested verifier Git SHA:
  `7f03a7485362f580f6dad02b7de9f5e156d9262e`
- Pinned lock SHA-256:
  `f5109b405806cf329914e577fb26e5a667fd4b1cb68e01ec283a3c9aef87d426`

## Compute and runtime

Before each run the verifier was estimated to need one core and finish under
five minutes. It therefore used the authorized local target. Environment
thread variables cap OpenMP, OpenBLAS, MKL, Accelerate, and NumExpr at one
thread. Actual allocation: one thread, eight logical CPUs visible, no GPU.

| Node | Formal wall time | Scientific-check time | Backend |
|---|---:|---:|---|
| Judged baseline | 25 s | 0.026558 s | local CPU |
| Exact Claim 6 | 20 s | 0.034820 s | local CPU |
| Cumulative availability/falsification audit | 40 s | 0.048119 s | local CPU |

Total billed remote CPU/GPU cost: **$0**. The release process repeats the same
cumulative suite immediately before publication.

## Data and controls

- [All current results](evidence/current_results.json)
- [Claim 2 cases](evidence/claim_2_cases.csv)
- [Claim 6 counts and classification hashes](evidence/claim_6_counts.csv)
- [Claim 1](evidence/c1.json), [Claim 2](evidence/c2.json),
  [Claim 3](evidence/c3.json), [Claim 4](evidence/c4.json),
  [Claim 5](evidence/c5.json), [Claim 6](evidence/c6.json)

The current pages supersede the old verifier. The historical pages remain
unchanged and reachable solely for provenance.
