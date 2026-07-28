# Claim 1 — Marginal Path Collapse

**Verdict: VERIFIED. Confidence: HIGH.**

## Exact contract and source

Section 2.2 states an existence phenomenon: a ratio-of-densities composition
may have valid endpoint densities while an intermediate density is
non-normalizable. Source anchor:
[Section 2.2](https://ar5iv.labs.arxiv.org/html/2512.10339#S2.SS2).

The constructive contract uses one-dimensional centered Gaussian experts,
polynomial/sigmoid schedules, and exponents \([1,-0.5]\). It requires positive
endpoint precision and negative precision at an intermediate time, plus
growing truncated log-normalizers.

## Result

- \(C(0)=0.4999774151>0\)
- \(C(0.999)=250130.2312>0\)
- \(\min_t C(t)=-9.3764710\) at \(t\approx0.88806\)
- truncated logZ: 1,870.765 at \(L=20\), 16,872.107 at \(L=60\),
  67,504.588 at \(L=120\), 187,523.253 at \(L=200\)

This directly witnesses valid endpoints and a divergent intermediate density.

## Reproduce and audit

Run `uv run --frozen python -m reproduction.run_all`. Source:
[run_all.py](evidence/code/run_all.py), [core.py](evidence/code/core.py).
Raw output and the contract-critical negative control:
[C1 JSON](evidence/c1.json). The control flips one required field and is
rejected. The one-thread cumulative run took 40 seconds; this numerical check
used no stochastic seed.

**Limitation:** this verifies the claimed existence phenomenon with a concrete
Gaussian witness; it does not use finite sampling to assert a universal
theorem.

