# Claim 5 source audit

The exact source is arXiv:2512.10339v2, Table 3 and Appendix C.2. The paper
uses nine CrossDock-Weak ligand-pocket pairs, five candidates per condition,
two seeds, 500 denoising steps, and guidance weight 1.3. It reports ACE
validity 100.0%, Vina mean -5.72, and overall success 93.30%; the NR
comparison reports validity 84.77% and Vina mean -2.93.

The official code audit targets
`ziseoklee/ACE@66534202cb255b6891d5dcbe2e9e18af88ff5615`.
The current README instead documents a 76-task CrossDocked2020 benchmark at
weight 1.4 with `B1=30`, `B2=0.336`, and diffusion scale 2.0. No
CrossDock-Weak task list, exact Table 3 runner, generated SDF files, or docking
CSV is committed.

The release pins three external pretrained-model submodules and downloads
DiffSBDD and GeoDiff checkpoints during setup. Its stated requirement is Linux
x86-64, NVIDIA CUDA, and approximately 15 GB.
