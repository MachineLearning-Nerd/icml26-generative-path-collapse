# Claim 6 method

The reference checker translates the five released PyTorch schedule formulas
to NumPy and reproduces the released notebook's exact 200-point criterion.
It enumerates all 125 ordered triplets and retains exactly the 100 cases in
which the two likelihood-ratio schedules differ.

The independent checker evaluates the same analytic schedule formulas on
20,001 time points. Its horizon and query count were selected as a fixed
101-fold grid refinement, not derived from the expected counts. Acceptance
requires both checkers to reproduce all six Table E.5 counts and to agree on
every individual triplet classification.

The negative control removes the negative exponent from the denominator.
That intentionally broken composition has three positive precision terms and
must produce zero collapses, causing the exact table contract to fail.

Fixed command:

```text
uv run --frozen python -m reproduction.run_all
```

The verifier exits nonzero if any accepted claim regression, exact count,
independent classification, or negative control fails.
