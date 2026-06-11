# CQECMPLX-Kernel-Sidecar

Status: `trackable-slice`

## Identity

This composite tracks the deployable sidecar kernel: file-fed runtime, operator
web UI, module registry, SQLite state layer, Docker deployment, and companion
kernel ring.

## Current Evidence

- `CMPLX-Kernel` deployment proof is `slice-ready`.
- `CMPLX Operator Web` deployment proof is `slice-ready`.
- `CMPLX Kernel Docker` deployment proof is `slice-ready`.
- Kernel runtime exists under:

```text
D:\CQE_CMPLX\CMPLX-Kernel\kernel
```

- The runtime contains:
  - `boot.py`;
  - `cmplx_kernel/`;
  - `web/`;
  - `deploy/docker/`;
  - `modules/MODULE_REGISTRY.json`;
  - schemas and docs.

## Composite Rule

The production composite name becomes:

```text
CQECMPLX-Kernel-Sidecar
```

The composite should publish as the smallest usable sidecar first. Runtime
state, caches, DB files, and raw corpora stay outside unless promoted through a
payload ledger.

## Not Yet Done

- Reconcile the current local kernel folder with the git production branch.
- Confirm final package boundaries after payload ledger is created.
- Add release instructions once remote publication begins.
