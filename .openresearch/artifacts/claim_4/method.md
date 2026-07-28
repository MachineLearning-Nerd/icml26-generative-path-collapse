# Claim 4 method and four routes

1. **Exact public-artifact replay.** Audited the official commit tree,
   release assets, notebook outputs, and exact-paper Hugging Face search.
   Result: no checkpoints or raw outputs to replay.
2. **From-source CPU reconstruction.** Audited the exact training and
   evaluation code. The three used experts require 14,000 batch-1024 training
   iterations; the evaluator hardcodes CUDA. GPU use is prohibited for this
   campaign, and an unvalidated CPU rewrite would deviate from the released
   implementation.
3. **Independent scope and metric audit.** The smallest exact comparison is
   15 method-seed runs and 150 million particle-steps. A single exact empirical
   OT cost matrix contains 100 million distances (800 MB at float64); the
   released MMD concatenation contains 400 million Gram entries before
   temporaries. No raw samples exist for independent metric recomputation.
4. **Mandatory falsification route.** Restated the exact stochastic claim and
   sought an assumption-matched counterexample. Different checkpoints,
   downscaled particles, proxy dynamics, or paper-table arithmetic do not
   satisfy the claim assumptions. No valid counterexample was established.

Fixed verifier command:

```text
uv run --frozen python -m reproduction.run_all
```

The completeness checker exits nonzero if any of the four routes is absent or
if the mandatory fourth route is mislabeled. The scientific verdict remains
BLOCKED, not PASS.
