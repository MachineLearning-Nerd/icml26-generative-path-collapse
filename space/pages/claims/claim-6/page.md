# Claim 6 — collapse prevalence scaling

![The exact six-point match.](images/headline_claim6.svg)

**Verdict: VERIFIED. Confidence: HIGH.**

## Exact contract and source

Appendix E.2 considers ordered three-expert compositions built from five
standard schedules. Of 125 ordered triplets, 120 are not all equal and exactly
100 satisfy the likelihood non-homogeneity condition. The reported collapse
counts at \(\omega=[1,1.1,1.5,2,7.5,15]\) are
`[41,47,52,66,77,80]`. Source anchors:
[Appendix E.2](https://ar5iv.labs.arxiv.org/html/2512.10339#A5.SS2).

The contract exhaustively enumerates the complete stated finite domain on the
released 200-point \([0,0.99]\) grid with epsilon \(10^{-12}\), then requires a
separate 20,001-point implementation to agree per triplet.

## Result

| ω | Eligible | Paper | Reproduction | Independent checker |
|---:|---:|---:|---:|---:|
| 1.0 | 100 | 41 | 41 | 41 |
| 1.1 | 100 | 47 | 47 | 47 |
| 1.5 | 100 | 52 | 52 | 52 |
| 2.0 | 100 | 66 | 66 | 66 |
| 7.5 | 100 | 77 | 77 | 77 |
| 15.0 | 100 | 80 | 80 | 80 |

All **600/600** per-triplet classifications agree. Because the complete finite
domain is enumerated, there is no seed or sampling confidence interval.

Raw files: [C6 JSON](evidence/c6.json) and
[counts/classification hashes CSV](evidence/claim_6_counts.csv). Source:
[core.py](evidence/code/core.py) and [run_all.py](evidence/code/run_all.py).

## Independent checker and control

The independent route uses 20,001 points rather than calling the reference
200-point checker. The negative control makes all three precision terms
positive by changing the denominator exponent's sign. It yields
`[0,0,0,0,0,0]`, and the verifier rejects it against the exact contract.
Control output is inline in [C6 JSON](evidence/c6.json).

Run `uv run --frozen python -m reproduction.run_all`. Allocation: one CPU
thread; cumulative wall time 40 seconds. Official-code source revision:
`ziseoklee/ACE@66534202cb255b6891d5dcbe2e9e18af88ff5615`.

**Limitation and deviation:** none from the finite schedule-triplet domain.
This exact finite-domain result does not generalize the percentages to other
schedule families. It replaces the historical random two-expert proxy.
