# Claim 4 source audit

The exact source is arXiv:2512.10339v2, Table 2 and Appendix C.1. The paper
reports five seeds, 10,000 samples, 1,000 SDE steps, noise level 0.5, ESS
threshold 0.7, and ACE bump `B=30`. The exact methods named by the claim are
NR, FKC, and ACE. The paper means `(W1, W2, MMD)` are:

- NR: `(0.78, 1.07, 0.068)`
- FKC: `(2.13, 2.44, 1.43)`
- ACE B=30: `(0.28, 0.40, 0.027)`

The official code audit targets
`ziseoklee/ACE@66534202cb255b6891d5dcbe2e9e18af88ff5615`.
Its full-evaluation README requires an NVIDIA CUDA GPU and says toy-expert
training takes about 30 minutes on an RTX A6000. The evaluation script uses
the schedule combination cosine/DDPM/linear, hardcodes CUDA, and expects
`PretrainedToyModels/`.

The repository contains neither that checkpoint directory nor raw result CSVs,
sample arrays, or notebook outputs. Both GitHub releases have zero assets.
Exact-paper searches of the Hugging Face model and dataset APIs returned no
matching artifact on 2026-07-28.
