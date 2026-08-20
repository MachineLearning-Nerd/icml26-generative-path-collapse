# Environment and reproduction contract

## Fixed command

~~~text
uv sync --frozen
uv run --frozen python -m reproduction.run_all
~~~

The evaluator-visible mirror uses the same command:
`uv run --frozen python -m reproduction.run_all`.

## Pinned environment

- Python: `3.11.*`
- Dependencies: `pyproject.toml` and `uv.lock`
- Backend: local CPU
- Thread limit: one OpenMP/BLAS/MKL/Accelerate/NumExpr thread
- GPU: none
- Logical CPUs visible during the recorded run: eight
- Cumulative formal wall time: approximately 40 seconds
- Scientific-check time: `0.048119` seconds
- Recorded cost: `$0`

The thread caps are set in `reproduction/run_all.py` before NumPy/SciPy are
imported. The run is deterministic for Claim 2's seed `0`; Claim 6 is an
exhaustive deterministic enumeration with no stochastic seed.

## Evidence inputs

- Verifier source: `reproduction/run_all.py`
- Numerical primitives: `reproduction/core.py`
- Current machine-readable output: `space/evidence/current_results.json`
- Claim outputs: `space/evidence/c1.json` through `c6.json`
- Exact Claim 6 counts: `space/evidence/claim_6_counts.csv`
- Source and lock copies exposed to the evaluator: `space/evidence/code/`
- Tested verifier revision: `7f03a7485362f580f6dad02b7de9f5e156d9262e`

Claims 4 and 5 are intentionally not rerun with substitute checkpoints,
benchmarks, or unauthorized GPU resources. Their exact missing capabilities
are recorded in [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md).
