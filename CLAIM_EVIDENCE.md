# Claim evidence ledger

Each verdict below comes from the committed verifier, raw machine-readable
output, source audit, and negative control linked in the table. A VERIFIED
result means the stated finite or constructive scope passed; it does not turn
finite computation into a proof of a universally quantified theorem.

| Claim | Verdict | Primary output | Production path |
| --- | --- | --- | --- |
| C1 | VERIFIED_SCOPED | `space/evidence/c1.json` | `reproduction/run_all.py::claim_1` |
| C2 | VERIFIED_SCOPED | `space/evidence/c2.json`, `space/evidence/claim_2_cases.csv` | `reproduction/run_all.py::claim_2` |
| C3 | VERIFIED_SCOPED | `space/evidence/c3.json` | `reproduction/run_all.py::claim_3` |
| C4 | BLOCKED | `space/evidence/c4.json` | `reproduction/run_all.py::blocked_claim_audits` |
| C5 | BLOCKED | `space/evidence/c5.json` | `reproduction/run_all.py::blocked_claim_audits` |
| C6 | VERIFIED_SCOPED | `space/evidence/c6.json`, `space/evidence/claim_6_counts.csv` | `reproduction/run_all.py::claim_6` |

## C1 — Marginal Path Collapse

The verifier constructs a Gaussian ratio-of-densities witness with
`gamma=[1.0,-0.5]` and polynomial/sigmoid schedules. Endpoint precision is
positive at `t=0` and `t=0.999`, while the intermediate minimum is
`-9.376471042500807`. The truncated log-normalizer grows from `1870.7653` at
`L=20` to `187523.2533` at `L=200`.

The result is produced by `criterion`, an independent truncated-integral
calculation, and a tampered-field negative control. It corroborates the
existence phenomenon for this concrete Gaussian witness; it does not claim to
re-prove Theorem 2.1.

## C2 — Path Existence Criterion

The verifier samples 60 seeded Gaussian compositions, compares the scalar
precision sign with independent numerical quadrature, and compares
normalizable cases with the analytic Gaussian log-normalizer. All 60
classifications agree and the maximum relative error is
`4.107305928547298e-15`.

The production path is `reproduction/run_all.py::claim_2`; raw rows are in
`space/evidence/c2.json` and `space/evidence/claim_2_cases.csv`. This is a
finite calibration of the factorized Gaussian setting, not a finite proof of
the paper's universal compact-support theorem.

## C3 — Adaptive Path Correction with Exponents

Two paths are required to collapse before the ACE bump, become strictly
positive afterward, and preserve endpoint exponents. The controlled middle
dip changes minimum precision from `-0.9599997732` to `1.0`; the heterogeneous
case changes it from `-0.1634550443` to `0.55`.

The result is produced by `reproduction/run_all.py::claim_3` and
`space/evidence/c3.json`. It is constructive corroboration of the correction
mechanism, not a finite proof of all theorem cases.

## C4 — Synthetic W1/W2/MMD table

The exact contract is five seeds, 10,000 particles, 1,000 SDE steps, methods
NR/FKC/ACE with `B=30`, and the Table 2 W1/W2/MMD values. The audit completed
four routes:

1. Exact public-artifact replay: code is available, but trained checkpoints,
   samples, raw tables, and notebook outputs are absent.
2. From-source CPU reconstruction: the released evaluator hardcodes CUDA and
   the stated training path requires the authors' GPU setup.
3. Independent resource/metric audit: exact replay requires 15 method-seed
   runs, 150 million particle-steps, and large OT/MMD allocations; no raw
   samples exist for a metric-only replay.
4. Assumption-preserving falsification: no valid counterexample was found;
   another model, sampler, or printed-table arithmetic would change the claim.

Therefore C4 is **BLOCKED**, not verified or falsified. The historical toy
credit (`1/2`) is preserved as provenance and is not promoted to a current
claim. Unblockers are exact trained checkpoints or raw samples, plus an
authorized CUDA path or author-validated CPU implementation.

## C5 — CrossDock-Weak table

The exact contract is nine ligand-pocket pairs, two seeds, five candidates per
seed, 500 denoising steps, guidance `omega=1.3`, and the Table 3 validity/Vina/
success metrics. The audit completed four routes:

1. Exact protocol and asset replay: generated molecules and per-sample docking
   records are absent.
2. Released benchmark cross-check: the public runner targets a different
   76-task CrossDocked2020 setup at `omega=1.4`.
3. Independent molecule-metric audit: validity and Vina require the exact
   generated SDF population; reference ligands are not a substitute.
4. Assumption-preserving falsification: no valid counterexample was found;
   another benchmark or incomplete CPU pipeline would violate the contract.

Therefore C5 is **BLOCKED**, not verified or falsified. The unblockers are the
exact nine task identifiers, generated ACE/NR molecules or reproducible seed
inputs, and authorized Linux/CUDA execution for the pinned checkpoints.

## C6 — Collapse prevalence versus guidance

The verifier reconstructs the five schedules, enumerates all `5^3=125`
ordered triplets, retains the 100 eligible heterogeneous compositions, and
evaluates the paper's six guidance weights on the released 200-point interval.
An independent checker repeats every classification on a 20,001-point grid.
The counts match exactly: `[41, 47, 52, 66, 77, 80]`. The positive-exponent
negative control yields zero collapses at all six weights and is rejected.

This is an exhaustive result for the finite Appendix E.2 domain. It does not
generalize those percentages to other schedule families or continuous
parameter domains.
