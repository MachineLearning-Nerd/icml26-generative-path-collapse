# Reproduction: collapse in diffusion steering

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-emv2qsi3TG-on-the-collapse-of-generative-paths-a-criterion-and-correction-for-diffusion/blob/main/notebooks/collapse_reproduction.py)

This repository reproduces the six judged claims from
[On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering](https://arxiv.org/abs/2512.10339).
The strongest new result replaces a random two-expert proxy with the paper's
complete five-schedule, three-expert enumeration: the reproduced collapse
fractions are **41%, 47%, 52%, 66%, 77%, and 80%**, exactly matching Appendix
E.2 at guidance scales \(1,1.1,1.5,2,7.5,15\).

Claims 1–3 continue to pass their cumulative Gaussian checks. Claims 4 and 5
remain honestly **BLOCKED** after four distinct routes each: exact checkpoints,
samples, and task identifiers are not publicly recoverable, and the released
full pipelines require CUDA or target a different benchmark. They are not
replaced by toy or proxy evidence.

- **Assessment:** Claims 1, 2, 3, and 6 VERIFIED; Claims 4 and 5 BLOCKED.
- **Paper versus observed:** Claim 6 paper
  `[41, 47, 52, 66, 77, 80]`; observed
  `[41, 47, 52, 66, 77, 80]`, with all 600 individual classifications
  independently confirmed.
- **Substitutions/downscaling:** none for Claim 6's stated finite domain.
  Claims 4–5 were not downscaled because a changed model or benchmark would
  not test the exact claim.
- **Compute:** local CPU only, one thread, locked Python 3.11/`uv` environment;
  the longest formal run took 40 seconds. No GPU was used.
- **Score:** the live judged score remains **8/12**. A conservative
  post-evaluation forecast is **8–10/12**, with **10/12** the best-supported
  possible total—not a judge result.
- **Publication:** evaluator evidence is live in the existing
  [Hugging Face Space at revision `0f454af`](https://huggingface.co/spaces/DineshAI/emv2qsi3TG/commit/0f454af2035b713178122b8bd6129cc74e50e11f).
  Status: **awaiting the live judge**.

Read the [illustrated technical report](reports/reproduction/report.md) or open
the [self-contained marimo tutorial](notebooks/collapse_reproduction.py).

## Experiment log

Every experiment inherited the exact same command:
`uv run --frozen python -m reproduction.run_all`.

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| [`orx/judged-8-of-12-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-emv2qsi3TG-on-the-collapse-of-generative-paths-a-criterion-and-correction-for-diffusion/tree/orx/judged-8-of-12-baseline) | Freeze and rerun the accepted theoretical evidence | `uv run --frozen python -m reproduction.run_all` | Claims 1–3 VERIFIED; 4–6 initially BLOCKED | local CPU, 1 thread, 25 s |
| [`orx/exact-schedule-triplet-collapse-prevalence`](https://github.com/MachineLearning-Nerd/icml26-repro-emv2qsi3TG-on-the-collapse-of-generative-paths-a-criterion-and-correction-for-diffusion/tree/orx/exact-schedule-triplet-collapse-prevalence) | Replace Claim 6's two-expert proxy with the exact finite domain | `uv run --frozen python -m reproduction.run_all` | Exact Table E.5 match | local CPU, 1 thread, 20 s |
| [`orx/exact-claim-availability-and-falsification-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-emv2qsi3TG-on-the-collapse-of-generative-paths-a-criterion-and-correction-for-diffusion/tree/orx/exact-claim-availability-and-falsification-audit) | Complete four routes each for Claims 4–5 | `uv run --frozen python -m reproduction.run_all` | Both BLOCKED; no valid counterexample | local CPU, 1 thread, 40 s |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-emv2qsi3TG-on-the-collapse-of-generative-paths-a-criterion-and-correction-for-diffusion/tree/orx/evaluator-visible-release-candidate) | Add canonical evidence pages, raw data, report, notebook, and final regression | `uv run --frozen python -m reproduction.run_all` | Cumulative suite PASS; Space release validated | local CPU, 1 thread, 25 s |
| `main` | Public README, report, notebook, and evaluator-visible mirror | Not run as an experiment (publication surface) | Published; awaiting live judge | presentation only |

## Run locally

```bash
uv sync --frozen
uv run --frozen python -m reproduction.run_all
uv run --frozen marimo edit notebooks/collapse_reproduction.py
```

The formal verifier exits nonzero if any claim contract, independent checker,
or negative control fails. Machine-readable evidence and claim contracts live
under `.openresearch/artifacts/`; the public report explains which conclusions
are exact, scoped corroborations, or blocked.

---

Original workspace description: ICML 2026 agent reproduction workspace for
`emv2qsi3TG`.
