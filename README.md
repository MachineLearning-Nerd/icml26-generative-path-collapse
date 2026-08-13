# On the Collapse of Generative Paths

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-generative-path-collapse/blob/main/notebooks/collapse_reproduction.py)

Independent claim-by-claim reproduction audit for [*On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering*](https://arxiv.org/abs/2512.10339), by Ziseok Lee, Minyeong Hwang, Wooyeol Lee, Sanghyun Jo, Jihyung Ko, Young Bin Park, Jae-Mun Choi, Eunho Yang, and Kyungsu Kim. This repository is an independent reproduction and evidence audit, not the authors' official implementation.

## Paper in one paragraph

The paper studies inference-time steering that composes diffusion or flow-model marginals by multiplying and dividing time-indexed densities. It identifies **Marginal Path Collapse**: valid endpoint distributions can produce an intermediate expression that is not normalizable. The paper gives a sharp sufficient Path Existence Criterion and proposes Adaptive Path Correction with Exponents (ACE), which uses time-varying exponents to stabilize the path. It also evaluates the correction on compositional image generation and flexible-pose scaffold decoration.

## Audit headline

The live judged score remains **8/12**. This audit records Claims 1, 2, 3, and 6 as **VERIFIED** and Claims 4 and 5 as **BLOCKED**. A conservative post-evaluation forecast is 8–10/12; that forecast is not a new judge result.

## Claim and evidence ledger

| Claim | Audit status | How the result is produced |
| --- | --- | --- |
| 1. Marginal Path Collapse exists | **VERIFIED** | Construct a Gaussian witness with valid endpoints and a negative intermediate precision; show that the truncated log-normalizer diverges as the integration limit grows. |
| 2. Path Existence Criterion | **VERIFIED** | Evaluate the scalar Gaussian precision criterion on 60 seeded compositions and compare it with independent numerical quadrature; all 60 verdicts agree and the maximum analytic-normalizer relative error is \(4.11\times10^{-15}\). |
| 3. ACE correction | **VERIFIED** | Apply the ACE exponent bump to a controlled middle dip and a heterogeneous-schedule case; both paths become positive while endpoint exponents remain unchanged. Negative controls fail closed when the contract is tampered with. |
| 4. Synthetic W1/W2/MMD table | **BLOCKED** | Audit four routes: public-artifact replay, CPU reconstruction, resource/metric feasibility, and assumption-preserving falsification. The exact learned checkpoints, samples, and raw table assets are unavailable, and a CUDA-only evaluator cannot be run under the authorized contract. |
| 5. CrossDock-Weak table | **BLOCKED** | Audit the exact nine-task contract, generated SDF population, checkpoint availability, benchmark identity, and possible counterexamples. The public runner targets a different 76-task benchmark and no assumption-matched replay or falsification is available. |
| 6. Collapse fraction versus guidance | **VERIFIED** | Reconstruct the five schedules, enumerate all \(5^3=125\) ordered triplets, retain the 100 eligible heterogeneous compositions, and independently recheck all classifications on a 20,001-point grid. The reproduced counts are 41%, 47%, 52%, 66%, 77%, and 80%, exactly matching the paper's finite table. |

Claims 4 and 5 are deliberately marked **BLOCKED**, not failed or verified. Proxy models, a different benchmark, or arithmetic on printed aggregates would not test their original assumptions.

## How each claim is produced

Each claim follows the same evidence path:

1. Freeze the paper's quantifiers, inputs, and expected conclusion in the claim contract under `.openresearch/artifacts/`.
2. Implement the primary derivation, construction, availability audit, or exact enumeration in `reproduction/`.
3. Run an independent checker and a contract-breaking negative control where the claim supports one.
4. Preserve raw machine-readable results, source audits, limitations, and exact commands.
5. Publish the cumulative result through `reports/reproduction/report.md`, `space/pages/`, and the release manifest.

The fixed local command is:

```bash
uv sync --frozen
uv run --frozen python -m reproduction.run_all
```

The locked Python 3.11 environment uses one CPU thread. The cumulative audit run took about 40 seconds locally; no GPU or remote compute was used.

## Repository contents

- [`reproduction/`](reproduction/) — Gaussian criteria, ACE checks, exact schedule enumeration, and independent checkers.
- [`reports/reproduction/report.md`](reports/reproduction/report.md) — illustrated technical report and limitations.
- [`notebooks/collapse_reproduction.py`](notebooks/collapse_reproduction.py) — self-contained tutorial notebook.
- [`.openresearch/artifacts/`](.openresearch/artifacts/) — claim contracts, source audits, raw outputs, and negative controls.
- [`space/`](space/) — evaluator-visible static Space source and logbook mirror.
- [`release/`](release/) — release allowlist, manifest, validation summary, and red-team records.
- [`branch-audit.md`](branch-audit.md) — mapping from former generated branch names to clean names.

## Branch map

`main` is the cumulative publication surface. The focused branches preserve the evidence lineage; the complete migration mapping is in [`branch-audit.md`](branch-audit.md).

| Clean branch | Purpose | Status |
| --- | --- | --- |
| [`historical/judged-baseline`](https://github.com/MachineLearning-Nerd/icml26-generative-path-collapse/tree/historical/judged-baseline) | Preserve the accepted 8/12 baseline and the originally judged evidence | Historical record |
| [`audit/claim6-schedule-enumeration`](https://github.com/MachineLearning-Nerd/icml26-generative-path-collapse/tree/audit/claim6-schedule-enumeration) | Replace the two-expert Claim 6 proxy with exact five-schedule, three-expert enumeration | Claim 6 evidence |
| [`audit/claims4-5-availability`](https://github.com/MachineLearning-Nerd/icml26-generative-path-collapse/tree/audit/claims4-5-availability) | Complete the four-route availability and falsification audit for Claims 4–5 | Claims 4–5 blocked |
| [`release/evaluator-candidate`](https://github.com/MachineLearning-Nerd/icml26-generative-path-collapse/tree/release/evaluator-candidate) | Package canonical evidence pages, raw data, report, notebook, and release validation | Release candidate |
| [`main`](https://github.com/MachineLearning-Nerd/icml26-generative-path-collapse/tree/main) | Current README, report, notebook, and evaluator-visible mirror | Current |

## Citation

```bibtex
@article{lee2026collapse,
  title         = {On the Collapse of Generative Paths: A Criterion and Correction for Diffusion Steering},
  author        = {Lee, Ziseok and Hwang, Minyeong and Lee, Wooyeol and Jo, Sanghyun and Ko, Jihyung and Park, Young Bin and Choi, Jae-Mun and Yang, Eunho and Kim, Kyungsu},
  journal       = {arXiv preprint arXiv:2512.10339},
  year          = {2026},
  doi           = {10.48550/arXiv.2512.10339},
  url           = {https://arxiv.org/abs/2512.10339}
}
```

Paper: [arXiv:2512.10339v2](https://arxiv.org/abs/2512.10339). The official implementation reviewed during the audit is [`ziseoklee/ACE`](https://github.com/ziseoklee/ACE/tree/66534202cb255b6891d5dcbe2e9e18af88ff5615). The historical evaluator artifact remains available in the [DineshAI/emv2qsi3TG Space](https://huggingface.co/spaces/DineshAI/emv2qsi3TG/commit/0f454af2035b713178122b8bd6129cc74e50e11f).

## Thank you

Thank you to Ziseok Lee, Minyeong Hwang, Wooyeol Lee, Sanghyun Jo, Jihyung Ko, Young Bin Park, Jae-Mun Choi, Eunho Yang, and Kyungsu Kim for developing the collapse criterion and ACE correction, and for sharing the paper and implementation that made this independent audit possible. The reproduction keeps blocked claims visibly blocked so that the authors' exact assumptions and contributions remain clear.

## Attribution and limitations

This repository is maintained by [MachineLearning-Nerd](https://github.com/MachineLearning-Nerd). It is not affiliated with the paper's authors. Numerical checks and finite enumerations corroborate the stated claims but do not replace the paper's general proofs. Claims 4 and 5 require unavailable artifacts or compute that preserve their exact experimental contracts.
