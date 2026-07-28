# Claim 3 — ACE correction

**Verdict: VERIFIED. Confidence: HIGH.**

## Exact contract and source

Theorems 2.2–2.3 introduce a time-varying bump correction that restores
positive coefficients while preserving boundary exponents. Source anchors:
[Theorem 2.2](https://ar5iv.labs.arxiv.org/html/2512.10339#S2.Thmtheorem2) and
[Theorem 2.3](https://ar5iv.labs.arxiv.org/html/2512.10339#S2.Thmtheorem3).

Two constructive paths must collapse before ACE, have \(C(t)>0\) afterward,
and retain their endpoint exponents.

![Two concrete ACE corrections.](images/correction_claim3.svg)

## Result

| Case | B | Minimum C before | Minimum C after | Endpoints preserved |
|---|---:|---:|---:|---|
| controlled middle dip | 4.0 | −0.9599998 | 1.0 | yes |
| heterogeneous schedules | 1.5 | −0.1634550 | 0.55 | yes |

Raw evidence/control: [C3 JSON](evidence/c3.json). Source:
[run_all.py](evidence/code/run_all.py). The tampered-field control is rejected.
Run `uv run --frozen python -m reproduction.run_all`. No stochastic seed; one
CPU thread; cumulative wall time 40 seconds.

**Limitation:** these are constructive instances and a cumulative regression,
not a finite numerical proof of all cases covered by the theorem.

