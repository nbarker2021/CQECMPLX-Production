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
| `CQECMPLX-LibForge-Lattice-ReForge-Ring` | yes | yes | split started |
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

1. Exact payload ledger body generated from accounting CSV/JSON.
2. Paper-claim binding from Production, AirLock, and Kernel roots.
3. First actual source promotion slice after the above management records are complete.

## Split Ledgers

- `tracking/lib-forge-package-splits/LIB_FORGE_PACKAGE_SPLIT.md`
- `tracking/lib-forge-package-splits/LIB_FORGE_PACKAGE_SPLIT.json`
- `tracking/payload-ledger/PAYLOAD_LEDGER.md`
- `tracking/payload-ledger/PAYLOAD_LEDGER.json`
- `tracking/paper-claim-bindings/PAPER_CLAIM_BINDING.md`
- `tracking/paper-claim-bindings/PAPER_CLAIM_BINDING.json`

## Promoted Slices

| Slice | Status | Manifest |
|---|---|---|
| `production/PROMOTION_SLICE_2026-06-11_PAPER_PROOF_TEXT.md` | promoted | `tracking/promotion-manifests/CQECMPLX-Paper-Proof-Bundle.manifest.json` |
| `production/workspace-corpus-index/PROMOTION_SLICE_2026-06-11_REPO_FORMS_INDEX.md` | promoted | `tracking/promotion-manifests/CQECMPLX-Repo-Forms-Accounting.manifest.json` |
| `production/diagnostics/CQECMPLX-NVEST-EG8-Gate/PROMOTION_SLICE_2026-06-11_NVEST_EG8_CONTRACTS.md` | promoted | `tracking/promotion-manifests/CQECMPLX-NVEST-EG8-Gate.manifest.json` |
