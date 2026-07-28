# Evaluator visibility matrix

Traversal starts at `README.md` → `pages/index.md` → **Current evidence**.
No repository knowledge, private run logs, or hidden dashboard artifacts are
needed.

| Claim | Canonical page | Code visible | Data inline | Raw link | Checker | Control | Exact claim tested | Reviewer verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claim 1](#/claim-1) | yes | yes | [JSON](evidence/c1.json) | truncated integrals | tamper rejected | Sec. 2.2 existence | VERIFIED |
| 2 | [Claim 2](#/claim-2) | yes | yes | [JSON](evidence/c2.json), [CSV](evidence/claim_2_cases.csv) | quadrature | tamper rejected | Thm. 2.1 Gaussian calibration | VERIFIED |
| 3 | [Claim 3](#/claim-3) | yes | yes | [JSON](evidence/c3.json) | pre/post criterion | tamper rejected | Thms. 2.2–2.3 instances | VERIFIED |
| 4 | [Claim 4](#/claim-4) | yes | yes | [audit JSON](evidence/c4.json) | four-route audit | missing route rejected | exact Table 2 protocol | BLOCKED |
| 5 | [Claim 5](#/claim-5) | yes | yes | [audit JSON](evidence/c5.json) | four-route audit | missing route rejected | exact Table 3 protocol | BLOCKED |
| 6 | [Claim 6](#/claim-6) | yes | yes | [JSON](evidence/c6.json), [CSV](evidence/claim_6_counts.csv) | independent dense grid | positive exponents rejected | exact Appendix E.2 domain | VERIFIED |

For all rows, the fixed command, locked environment, source anchors, verifier
SHA, seeds, CPU allocation, and runtime are visible on
[Method and provenance](#/method). Limitations and deviations appear on each
claim page. The complete combined output is
[downloadable JSON](evidence/current_results.json).

## Reviewer conclusion

- Exact current verifier is obvious from the canonical page: **yes**
- Old rejected verifier clearly labeled historical: **yes**
- Every displayed numerical result linked to raw output: **yes**
- BLOCKED claims distinguish missing capability from falsification: **yes**
- Live score distinguished from forecasts: **yes**

