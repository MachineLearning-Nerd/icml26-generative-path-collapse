# Claim 2 — Path Existence Criterion

**Verdict: VERIFIED. Confidence: HIGH.**

## Exact contract and source

Theorem 2.1, under the paper's compact-support/factorized setting, makes path
existence equivalent to positivity of every coordinate coefficient
\(C_k(t)=\sum_i\gamma_i(t)/(\alpha_t^{(i)})^2\).
Source anchor:
[Theorem 2.1](https://ar5iv.labs.arxiv.org/html/2512.10339#S2.Thmtheorem1).

The executable calibration contract samples 60 deterministic seed-0 Gaussian
compositions. For every case, the criterion sign must agree with independent
numerical integrability; positive cases must agree with the analytic Gaussian
normalizer.

## Result

- criterion/quadrature verdict agreement: **60/60**
- maximum analytic log-normalizer relative error:
  **\(4.1073\times10^{-15}\)**
- raw cases: [CSV](evidence/claim_2_cases.csv)
- full evidence/control: [C2 JSON](evidence/c2.json)

The independent checker uses numerical quadrature rather than the sign formula
as its integrability oracle. A tampered contract field is rejected.

## Reproduce and scope

Run `uv run --frozen python -m reproduction.run_all` with the visible
[source](evidence/code/run_all.py) and
[locked environment](evidence/code/uv.lock). Seed: 0. Allocation: one CPU
thread; cumulative wall time: 40 seconds.

**Limitation:** the finite Gaussian calibration does not purport to prove a
universally quantified theorem. It rigorously reruns the already judged
machine-precision corroboration.

