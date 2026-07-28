# Claim 4 — synthetic W1/W2/MMD

**Verdict: BLOCKED. Confidence: LOW. Historical judge credit: TOY (1/2).**

## Exact contract and source

Table 2 reports, over five seeds, 10,000 particles and 1,000 SDE steps:

| Method | W1 | W2 | MMD |
|---|---:|---:|---:|
| NR | 0.78 | 1.07 | 0.068 |
| FKC | 2.13 | 2.44 | 1.43 |
| ACE, B=30 | 0.28 | 0.40 | 0.027 |

Source anchors: [Table 2](https://ar5iv.labs.arxiv.org/html/2512.10339#S3.T2)
and [synthetic protocol](https://ar5iv.labs.arxiv.org/html/2512.10339#A3.SS1).
The exact stochastic table—not an integrability proxy—is the contract.

## Four completed routes

1. **Exact artifact replay:** the official commit has code but no trained toy
   checkpoints, generated sample arrays, raw table, or notebook outputs.
   Releases contain no assets and exact-paper Hugging Face searches found no
   model/dataset.
2. **From-source CPU reconstruction:** the three used experts require 14,000
   batch-1024 training iterations. The evaluator hardcodes CUDA; the authors
   specify about 30 A6000 minutes. GPU use is not authorized.
3. **Independent metric/resource audit:** 15 method-seed runs imply 150
   million particle-steps. A 10k² float64 OT matrix is 800 MB; the released
   20k² MMD path has 400 million entries before temporaries. No samples exist
   for a metric-only replay.
4. **Assumption-preserving falsification:** another model or sampler cannot
   contradict results for unreleased learned parameters. No valid
   counterexample was established.

Raw route records and negative-control output:
[C4 audit JSON](evidence/c4.json). The checker rejects removal of the mandatory
fourth route. Audit code:
[run_all.py](evidence/code/run_all.py). Fixed command:
`uv run --frozen python -m reproduction.run_all`; one CPU thread; 40 seconds
cumulative.

## Limitation and unblocker

A faithful verdict needs either the exact trained checkpoints/generated
samples for all seeds or an author-validated CPU implementation with
assumption-matched regeneration. The old integrability-only proxy is preserved
under **Historical rejected baseline** and is not current verification.

