# Production Repo Map

Canonical remote:

```text
https://github.com/nbarker2021/CQECMPLX-Production
```

This repo is the main production identity. Other git and local roots are
members of this production family, but they enter this repo only once shaped.

## Local Intake Roots

| Root | Role | Promotion Status |
|---|---|---|
| `D:\CQECMPLX-Production` | current local production body | ready for slice review |
| `D:\CQECMPLX-AirLock` | quarantine and lineage intake | staged |
| `D:\CQE_CMPLX` | full development corpus | staged |
| `D:\CMPLX-Kernel` | deployable sidecar kernel and package builder | runtime ready, corpus staged |

## Public Git Roots Seen

| Repo | Role Guess | Intake Status |
|---|---|---|
| `nbarker2021/CMPLX-1T` | high-level CMPLX root | pending clone/review |
| `nbarker2021/CMPLX-Monorepo` | existing monorepo/submodule structure | pending clone/review |
| `nbarker2021/CMPLXUNI` | unified system build | pending clone/review |
| `nbarker2021/CMPLX` | core CMPLX repo | pending clone/review |
| `nbarker2021/CMPLXMCP` | MCP surface | pending clone/review |
| `nbarker2021/CMPLXDevKit` | developer kit | pending clone/review |

## Promotion Lanes

- `production/kernel-runtime` - the literal sidecar kernel runtime.
- `production/lib-forge` - reusable library contracts and adapters.
- `production/proof-receipts` - proof and diagnostic receipts.
- `production/papers` - paper/source context.
- `production/airlock-reviewed` - material that cleared airlock review.
- `production/workspace-corpus-index` - indexed references to large corpus material.

