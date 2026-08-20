# Audit report

The detailed illustrated report is
[reports/reproduction/report.md](reports/reproduction/report.md). The
evaluator-visible reader starts at [space/pages/index.md](space/pages/index.md)
and follows [space/logbook.json](space/logbook.json).

## Publication boundary

The historical judge result is **8/12**. The exact local evidence does not
claim a new score, author endorsement, or official implementation status.
Claims 4 and 5 stay BLOCKED because changing the model, benchmark, generated
samples, or compute contract would answer a different question.

## Evidence summary

| Claim group | Result | Evidence |
| --- | --- | --- |
| C1–C3 | VERIFIED_SCOPED | Gaussian witness, quadrature calibration, and two ACE correction constructions |
| C4 | BLOCKED | Four-route exact-asset/resource/falsification audit |
| C5 | BLOCKED | Four-route protocol/benchmark/asset/falsification audit |
| C6 | VERIFIED_SCOPED | Exhaustive 125-triplet reconstruction and dense independent checker |

## Release checks

- The existing evaluator-visible Space candidate passed its release validator.
- The existing evaluator-blind red-team round 3 passed.
- The current Space manifest preserves historical pages and links.
- The GitHub repository adds a claim dossier, source audit, environment
  contract, citation, thank-you note, machine-readable verdicts, and a
  fresh-clone verifier.
