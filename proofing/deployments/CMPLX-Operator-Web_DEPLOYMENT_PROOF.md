# CMPLX Operator Web Deployment Proof

## Identity

`CMPLX Operator Web` is the preinstalled local frontend/API layer for the
CMPLX-Kernel sidecar. It lets a local operator or host AI use the same kernel
contract through HTTP and a browser UI.

## Deployment Surface

```text
D:\CMPLX-Kernel\kernel
```

Runtime files:

- `boot.py`
- `cmplx_kernel/operator_server.py`
- `cmplx_kernel/module_registry.py`
- `cmplx_kernel/state_store.py`
- `web/index.html`
- `web/operator.css`
- `web/operator.js`
- `modules/MODULE_REGISTRY.json`
- `docs/OPERATOR_WEB_CONSOLE.md`
- `docs/MODULE_AND_DATA_CONTRACT.md`

## API Surface

- `GET /api/health`
- `GET /api/modules`
- `GET /api/kernel-ring`
- `GET /api/events`
- `POST /api/process`
- `POST /api/module-state`

## Adapter Boundary

The operator web layer is a Universal Adapter host over the existing sidecar
contract. It does not replace the file-fed kernel. It routes HTTP requests into
the same token-string process path and records event receipts.

Generated SQLite state is runtime data. It is excluded from production source
unless a Binary Boundary Adapter receipt promotes an explicit snapshot.

## Diagnostic Contract

The UI exposes training mode and local full-program mode as toggles. Hidden
Guess Result remains quiet unless one of those modes enables it.

## State

`slice-ready`

The first safe slice is the stdlib operator/API/module/state scaffold. Future
database engines, authentication, remote hosting, and multi-user operation need
separate proof docs before production promotion.
