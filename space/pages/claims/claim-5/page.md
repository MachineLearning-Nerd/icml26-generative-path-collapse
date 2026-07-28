# Claim 5 — CrossDock-Weak

**Verdict: BLOCKED. Confidence: LOW. Historical judge credit: 0/2.**

## Exact contract and source

Table 3 uses nine CrossDock-Weak ligand-pocket pairs, two seeds, five
candidates per seed, 500 denoising steps, and guidance \(\omega=1.3\). It
reports ACE validity **100.0%**, mean Vina **−5.72**, and overall success
**93.30%**, versus NR validity **84.77%** and Vina **−2.93**.
Source: [Table 3](https://ar5iv.labs.arxiv.org/html/2512.10339#S3.T3).

## Four completed routes

1. **Exact protocol/asset replay:** no generated molecules or per-sample Table
   3 docking records are released.
2. **Released benchmark cross-check:** the current runner targets 76
   CrossDocked2020 tasks at \(\omega=1.4\), with different correction
   constants—not the nine CrossDock-Weak tasks at 1.3.
3. **Independent molecule-metric audit:** validity and Vina require the
   generated SDF population. Reference ligands test a different population.
   The released stack also requires external checkpoints, Linux/CUDA, and
   roughly 15 GB.
4. **Assumption-preserving falsification:** a different benchmark, reference
   ligand, or incomplete CPU pipeline violates the claim assumptions. No valid
   counterexample was established.

Raw route records and negative-control output:
[C5 audit JSON](evidence/c5.json). The checker rejects removal of the mandatory
fourth route. Audit code:
[run_all.py](evidence/code/run_all.py). Fixed command:
`uv run --frozen python -m reproduction.run_all`; one CPU thread; 40 seconds
cumulative.

## Limitation and unblocker

Faithful testing requires the exact nine task identifiers plus generated
ACE/NR molecules (or reproducible seed inputs) and an authorized execution
path for the pinned molecular checkpoints. Until then the exact claim is
BLOCKED, not falsified.

