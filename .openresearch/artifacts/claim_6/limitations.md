# Claim 6 limitations and deviations

- This reproduces the paper's finite schedule-combinatorics result, not the
  downstream neural sampling experiments associated with selected triplets.
- The primary checker deliberately matches the released notebook's operational
  interval `[0, 0.99]` and 200-point discretization. It does not reinterpret
  Table E.5 as a continuum theorem over `[0,1)`.
- The independent checker is a much denser deterministic grid. Agreement on
  all 600 weight-triplet classifications guards against grid-resolution
  artifacts for this stated finite experiment.
- The implementation uses NumPy rather than PyTorch, with the released analytic
  formulas translated term for term.
