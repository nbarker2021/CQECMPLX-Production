# Tracking Coverage

Created: 2026-06-11

This dashboard tracks whether each production candidate has the three management
pieces needed before source movement:

- source binding;
- promotion manifest;
- composite spec.

## Full Coverage

| ID | Source Binding | Manifest | Composite |
|---|---:|---:|---:|
| `CQECMPLX-AirLock-CQE-Forge-Lineage` | yes | yes | yes |
| `CQECMPLX-Analog-Forge-Workbench` | yes | yes | yes |
| `CQECMPLX-CMPLXNEXT-Orchestration` | yes | yes | yes |
| `CQECMPLX-Docker-Compose-Boundary` | yes | yes | yes |
| `CQECMPLX-LibForge-Lattice-ReForge-Ring` | yes | yes | partial |
| `CQECMPLX-MetaMaterial-Designer` | yes | yes | yes |
| `CQECMPLX-MORSR-Pulse-Family` | yes | yes | yes |
| `CQECMPLX-NVEST-EG8-Gate` | yes | yes | yes |
| `CQECMPLX-Odysseus-MCP-Memory` | yes | yes | yes |
| `CQECMPLX-Paper-Proof-Bundle` | yes | yes | yes |
| `CQECMPLX-Payload-Ledger` | yes | yes | yes |
| `CQECMPLX-ProofValidated-Kernel` | yes | yes | yes |
| `CQECMPLX-Repo-Forms-Accounting` | yes | yes | yes |
| `CQECMPLX-TMN-Role-Family` | yes | yes | yes |

## Still Needed

1. Package-family split under `CQECMPLX-LibForge-Lattice-ReForge-Ring`.
2. Exact payload ledger body generated from accounting CSV/JSON.
3. Paper-claim binding from Production, AirLock, and Kernel roots.
4. First actual source promotion slice after the above management records are complete.
