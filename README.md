# CQECMPLX-Production

Canonical production repo for the CQE/CMPLX tool family.

This repository is intended to become the production body for the staged local
roots:

- `D:\CQECMPLX-Production`
- `D:\CQECMPLX-AirLock`
- `D:\CQE_CMPLX`
- `D:\CMPLX-Kernel`

The repo starts as a clean anchor. Staged material should enter by explicit
promotion slices, not by blind workspace dumps.

## Production Rule

A slice is ready for this repo when it has:

- clear identity and destination;
- manifest or index;
- portability review;
- CQE proof or receipt anchor where applicable;
- adapter boundary when it talks to another host/tool;
- Hidden Guess Result support when `training_mode` is enabled;
- no virtual environments, caches, bytecode, or local-only metadata.

## Git Head

Canonical remote:

```text
https://github.com/nbarker2021/CQECMPLX-Production
```

Canonical production head:

```text
main
```

Current intake/review branch:

```text
intake/production-kernel-map
```

Purpose: seed the production repo map and prepare the first fork lane for
later promotion of the sidecar kernel, production folder, airlock material, and
the `D:\CQE_CMPLX` workspace corpus.

The production head receives tracking records and production-shaped slices.
The intake branch remains available for review and staging work.
