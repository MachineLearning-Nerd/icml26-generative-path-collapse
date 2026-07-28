# Evaluation

Run exactly:

```bash
uv run --frozen python -m reproduction.run_all
```

The machine-readable block and final `cumulative_regression` line are the raw result. The command exits nonzero if the claim or its negative control fails. Runtime and CPU visibility are printed by the command.
