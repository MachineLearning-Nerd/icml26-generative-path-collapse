# Current evidence (2026-07-28)

![Exact paper/reproduction agreement for Claim 6.](images/headline_claim6.svg)

**Live judged score: 8/12.** The conservative post-evaluation forecast is
**8–10/12**, with **10/12** the best-supported possible score. These are
forecasts only, not judge results.

## Claim summary

| Claim | Exact paper statement tested | Current evidence | Raw data | Checker and control | Verdict |
|---|---|---|---|---|---|
| 1 | A ratio-of-densities composition can have valid endpoints but a non-normalizable intermediate marginal (Sec. 2.2). | \(C(0)=0.49998\), \(C(0.999)=250130.23\), intermediate minimum \(-9.376\); truncated logZ rises 1,870.8→187,523.3 as \(L\) rises 20→200. | [C1 JSON](evidence/c1.json) | Independent truncated integrals; tampered contract rejected | **VERIFIED** |
| 2 | For the paper's factorized Gaussian setting, path existence is equivalent to every \(C_k(t)>0\) (Theorem 2.1). | Sign and quadrature agree 60/60; maximum analytic relative error \(4.11\times10^{-15}\). | [C2 JSON](evidence/c2.json), [60 cases CSV](evidence/claim_2_cases.csv) | Numerical quadrature; tampered contract rejected | **VERIFIED** |
| 3 | The ACE bump can restore \(C_k(t)>0\) while preserving endpoint exponents (Theorems 2.2–2.3). | Two collapsed paths corrected; minimum corrected \(C\): 1.0 and 0.55; endpoints preserved. | [C3 JSON](evidence/c3.json) | Pre/post criterion; tampered contract rejected | **VERIFIED** |
| 4 | On the five-seed synthetic benchmark, ACE \(B=30\) reports W1=0.28, W2=0.40, MMD=0.027 versus NR/FKC (Table 2). | Four distinct routes completed; exact checkpoints/samples absent and released evaluator CUDA-only. | [C4 audit JSON](evidence/c4.json) | Asset/resource audits; removal of mandatory falsification route rejected | **BLOCKED** |
| 5 | On nine CrossDock-Weak pairs at \(\omega=1.3\), ACE reports 100% validity, Vina −5.72, OSR 93.30% (Table 3). | Four distinct routes completed; exact tasks/samples absent and public runner uses a different benchmark. | [C5 audit JSON](evidence/c5.json) | Protocol/asset audits; removal of mandatory falsification route rejected | **BLOCKED** |
| 6 | Among the paper's five-schedule three-expert compositions, collapse rises 41%→80% as \(\omega\) rises 1→15 (Appendix E.2). | Exact counts `[41,47,52,66,77,80]`; independent 20,001-point checker agrees on all 600 classifications. | [C6 JSON](evidence/c6.json), [counts CSV](evidence/claim_6_counts.csv) | Independent dense grid; positive-exponent control gives all zeros and is rejected | **VERIFIED** |

## One command, one environment

```bash
uv run --frozen python -m reproduction.run_all
```

- Python 3.11; [pyproject.toml](evidence/code/pyproject.toml) and
  [uv.lock](evidence/code/uv.lock) are evaluator-visible.
- Tested verifier:
  [run_all.py](evidence/code/run_all.py) and
  [core.py](evidence/code/core.py).
- Tested Git SHA:
  `7f03a7485362f580f6dad02b7de9f5e156d9262e`.
- Determinism: seed 0 for Claim 2; exhaustive enumeration/no seed for Claim 6.
- Compute estimate and allocation: one CPU core/thread; eight logical CPUs
  visible; no GPU.
- Cumulative formal run: ID
  `5cc88562-1ec4-48ed-b027-8658778d4d3b`, 40 seconds wall time,
  0.048119 seconds inside the numerical checks.
- [Complete machine-readable result](evidence/current_results.json).

## Limitations

Claims 1–3 are constructive finite corroborations in Gaussian families; their
universal theorems are not claimed to be proved by sampling. Claim 6 is exact
over the complete finite domain stated by Appendix E.2. Claims 4–5 are
BLOCKED—not verified or falsified—because no available route preserves all
claim assumptions. The historical proxy remains accessible but is not current
evidence.
