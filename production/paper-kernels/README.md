# CQECMPLX 32-Paper Kernel Suite

This suite treats Papers 01-32 as four active blocks of eight papers. Each paper receives the same eight deployable kernel components so it can run alone or as part of the master suite.

Paper 00 is outside the active windows. It is the past burden: the minimum information contract and method requirement inherited by every active paper.

Primary registry: `PAPER_KERNEL_REGISTRY.json`.

Block manifests live under `blocks/`; per-paper kernels live under `papers/`.

## Run Selectors

Use `tools/run_paper_kernel_suite.py` to validate a single paper, one 8-paper block,
or the full active suite:

```bash
python production/paper-kernels/tools/run_paper_kernel_suite.py --selector CQE-paper-01 --training-mode --write-receipt
python production/paper-kernels/tools/run_paper_kernel_suite.py --selector block-00-papers-01-08 --training-mode --write-receipt
python production/paper-kernels/tools/run_paper_kernel_suite.py --selector suite --training-mode --write-receipt
```

The runner treats Paper 00 as the inherited contract and does not include it in
the active paper windows.
