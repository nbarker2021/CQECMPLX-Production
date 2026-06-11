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
| `CQECMPLX-CMPLXUNI-Swarm-Frontend` | yes | draft | yes |
| `CQECMPLX-Docker-Compose-Boundary` | yes | yes | yes |
| `CQECMPLX-DevKit-MCPOS-MORSR-Runtime` | yes | draft | yes |
| `CQECMPLX-LibForge-Lattice-ReForge-Ring` | yes | yes | split started |
| `CQECMPLX-MetaMaterial-Designer` | yes | yes | yes |
| `CQECMPLX-MORSR-Pulse-Family` | yes | yes | yes |
| `CQECMPLX-NVEST-EG8-Gate` | yes | yes | yes |
| `CQECMPLX-Odysseus-MCP-Memory` | yes | yes | yes |
| `CQECMPLX-Paper-Proof-Bundle` | yes | yes | yes |
| `CQECMPLX-Payload-Ledger` | yes | yes | yes |
| `CQECMPLX-ProofValidated-Kernel` | yes | yes | yes |
| `CQECMPLX-Product-Fourpack` | yes | draft | yes |
| `CQECMPLX-Repo-Forms-Accounting` | yes | yes | yes |
| `CQECMPLX-TMN1-Conservation-Fullstack` | yes | draft | yes |
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
| `production/diagnostics/CQECMPLX-MORSR-Pulse-Family/PROMOTION_SLICE_2026-06-11_MORSR_PUBLIC_SCAFFOLD.md` | promoted scaffold | `tracking/promotion-manifests/CQECMPLX-MORSR-Pulse-Family.manifest.json` |
| `production/adapters/CQECMPLX-Docker-Compose-Boundary/PROMOTION_SLICE_2026-06-11_DOCKER_COMPOSE_BOUNDARY.md` | promoted | `tracking/promotion-manifests/CQECMPLX-Docker-Compose-Boundary.manifest.json` |
| `production/adapters/CQECMPLX-DevKit-MCPOS-MORSR-Runtime/PROMOTION_SLICE_2026-06-11_DEVKIT_MCPOS_DOCS_INVENTORY.md` | promoted docs/inventory | `tracking/promotion-manifests/CQECMPLX-DevKit-MCPOS-MORSR-Runtime.manifest.json` |
| `production/orchestration/CQECMPLX-CMPLXUNI-Swarm-Frontend/PROMOTION_SLICE_2026-06-11_CMPLXUNI_DOCS_CONFIGS.md` | promoted docs/configs | `tracking/promotion-manifests/CQECMPLX-CMPLXUNI-Swarm-Frontend.manifest.json` |
| `production/products/CQECMPLX-Product-Fourpack/PROMOTION_SLICE_2026-06-11_PRODUCT_FOURPACK_DOCS_DEPLOY.md` | promoted docs/deploy metadata | `tracking/promotion-manifests/CQECMPLX-Product-Fourpack.manifest.json` |
| `production/operations/CQECMPLX-TMN1-Conservation-Fullstack/PROMOTION_SLICE_2026-06-11_TMN1_OPERATIONS_DOCKER_DOCS.md` | promoted docs/docker metadata | `tracking/promotion-manifests/CQECMPLX-TMN1-Conservation-Fullstack.manifest.json` |
| `production/lib-forge/CQECMPLX-MetaMaterial-Designer/PROMOTION_SLICE_2026-06-11_METAMATERIAL_SOURCE_PACKAGE.md` | promoted source/package | `tracking/promotion-manifests/CQECMPLX-MetaMaterial-Designer.manifest.json` |
