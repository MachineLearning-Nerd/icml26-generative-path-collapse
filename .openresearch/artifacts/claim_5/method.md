# Claim 5 method and four routes

1. **Exact protocol and asset replay.** Audited the paper protocol and release
   tree. No exact CrossDock-Weak generated molecules or per-sample Table 3
   records are available.
2. **Released benchmark crosscheck.** Compared the public 76-task
   CrossDocked2020 runner with the nine-task CrossDock-Weak claim. Its task
   domain and weight differ, so running it would not test the exact claim.
3. **Independent molecule-metric audit.** Validity and Vina require the
   generated SDF population. Reference ligand evaluation would be a different
   population. The setup additionally requires external checkpoints,
   Linux/CUDA, and about 15 GB.
4. **Mandatory falsification route.** Sought an assumption-matched
   counterexample. Neither the replacement benchmark nor reference ligands
   satisfy the claim domain, and no exact samples exist. No valid
   counterexample was established.

Fixed verifier command:

```text
uv run --frozen python -m reproduction.run_all
```

The completeness checker exits nonzero if any route is absent. Its PASS only
means the BLOCKED audit is complete; it does not convert Claim 5 into a
scientific PASS.
