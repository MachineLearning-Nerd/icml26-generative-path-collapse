# Reproduction status

## Overall verdict

**PARTIAL_C1_C2_C3_C6_VERIFIED_C4_C5_BLOCKED_HISTORICAL_SCORE_8_OF_12_NO_CURRENT_SCORE**

This repository is an independent, claim-by-claim audit of
[*On the Collapse of Generative Paths: A Criterion and Correction for
Diffusion Steering*](https://arxiv.org/abs/2512.10339). It is not the authors'
official implementation.

- Historical live judge result: **8/12** for `DineshAI/emv2qsi3TG`, judged
  2026-07-27.
- Current evidence does **not** claim a new judge score.
- `publication_allowed=false`; no author endorsement is claimed.
- Claims 1–3 and 6 are verified within the explicit scopes below.
- Claims 4 and 5 remain blocked because their exact empirical assets and
  authorized execution path are unavailable.

| Claim | Status | How the result is produced | Boundary |
| --- | --- | --- | --- |
| C1 Marginal Path Collapse | VERIFIED_SCOPED | Gaussian witness with valid endpoints, negative intermediate precision, and divergent truncated log-normalizer | Concrete witness; not a proof of the theorem |
| C2 Path Existence Criterion | VERIFIED_SCOPED | 60 seeded Gaussian cases, independent quadrature, and analytic-normalizer comparison | Finite Gaussian calibration; theorem remains theorem-level |
| C3 ACE correction | VERIFIED_SCOPED | Two collapsed paths corrected to positive precision while endpoints are preserved | Two constructive instances |
| C4 Synthetic W1/W2/MMD | BLOCKED | Four-route artifact, resource, metric, and falsification audit | Exact checkpoints/samples and CUDA path unavailable |
| C5 CrossDock-Weak | BLOCKED | Four-route protocol, benchmark, asset, and falsification audit | Exact nine-task assets and CUDA/Linux path unavailable |
| C6 Collapse prevalence | VERIFIED_SCOPED | Exhaustive 125-triplet reconstruction plus 20,001-point independent checker | Exact finite Appendix E.2 domain only |

See [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) for the production path for
each claim, [SOURCE_AUDIT.md](SOURCE_AUDIT.md) for paper and code
provenance, and [ENVIRONMENT.md](ENVIRONMENT.md) for the locked runtime.
