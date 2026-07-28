# Claim 6 source audit

Paper source: arXiv:2512.10339v2, retrieved from
`https://ar5iv.labs.arxiv.org/html/2512.10339` on 2026-07-28 UTC. The complete
HTML SHA-256 is
`1ea66da8241cfd6e4e4cf06c4a441218c53ee72b49da82c388436d842cb74f81`.

Relevant anchors are Section 4, Appendix C.1, Appendix E.2 (`A5.SS2`), and
Table E.5 (`A5.T5`). The paper states an exhaustive domain of 5^3 = 125
ordered three-expert schedule triplets for
`q1 * (q2/q3)^w`. Appendix C.1 distinguishes 120 triplets that are not all
equal from the 100 likelihood-nonhomogeneous triplets satisfying
`alpha2 != alpha3`; Table E.5 reports percentages over the latter 100 cases.
The exact reported counts for `w = [1, 1.1, 1.5, 2, 7.5, 15]` are
`[41, 47, 52, 66, 77, 80]`.

The released notebook at
`ziseoklee/ACE@66534202cb255b6891d5dcbe2e9e18af88ff5615` evaluates the
equivalent permuted expression `(q(a1)/q(a2))^w * q(a3)`, on 200 equally
spaced points from 0 to 0.99 with epsilon `1e-12`. Its criterion is
`w/alpha(a1)^2 - w/alpha(a2)^2 + 1/alpha(a3)^2`. The schedule functions are
loaded from `2d_synthetic/ace_lib/interpolant_schedules.json`.

No stochastic quantifier is involved: this is a finite, deterministic,
exhaustive claim.
