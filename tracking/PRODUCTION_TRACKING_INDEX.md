# Production Tracking Index

This is the first index of material that is done enough to track for eventual
publication in `nbarker2021/CQECMPLX-Production`.

The index tracks composites. It does not choose a winner among duplicates.

## Composite Candidates

| Composite | Status | Why It Is Trackable | First Production Route |
|---|---|---|---|
| `CQECMPLX-Kernel-Sidecar` | `trackable-slice` | sidecar runtime, operator web, Docker deploy, module/data contracts, deployment proofs | `production/kernel-runtime` |
| `CQECMPLX-Docker-Operator` | `trackable-composite` | kernel Docker proof, Docker tool adapter, Compose boundary, D:\DockerContainers platform evidence | `production/kernel-runtime` + `production/adapters` |
| `CQECMPLX-DevKit-MCPOS-MORSR-Runtime` | `trackable-runtime-candidate` | DevKit MCP OS exposes server/client, CQE layer tools, MORSR optimization, handle-based heavy data, validation framework, and AGRM/MDHG integration | `production/adapters` + `production/kernel-runtime` + `production/diagnostics` |
| `CQECMPLX-LatticeForge-ReForge` | `trackable-composite` | PartsFactory lattice-forge, ReForge/Forge kernel ring, morphism ledger payload, lattice/forge claim density | `production/lib-forge` |
| `CQECMPLX-E8-MORSR-Diagnostics` | `trackable-composite` | E8/MORSR/CQE names recur across repo profiles, kernel ring, R30/Formalization proof bridge | `production/proof-receipts` + `production/lib-forge` |
| `CQECMPLX-MCP-API-Tooling` | `trackable-composite` | CMPLXMCP content-profile complete, MCP/API surfaces in DevKit, Monorepo, DockerContainers MCP toolkit | `production/adapters` |
| `CQECMPLX-Formalization-R30-Proof` | `trackable-proof` | Formalization and R30 are proof/lattice/theorem/paper dense and cross-reference PartsFactory | `production/papers` + `production/proof-receipts` |
| `CQECMPLX-MMDB-E8-Vector-Payloads` | `trackable-payload` | CMPLX/CMPLXUNI DB payload candidates include MMDB, vector stores, E8 DBs | `production/payload-ledger` |
| `CQECMPLX-Manny-Memory-Instruction-Payloads` | `trackable-payload` | Manny contains memory and instruction SQLite payloads with Docker/Compose/MCP evidence | `production/payload-ledger` |
| `CQECMPLX-CMPLXNEXT-Orchestration` | `trackable-composite` | Monorepo exposes CMPLXNEXT storage, MCP agent net, IDE, frontend bridge terms | `production/orchestration` |
| `CQECMPLX-CMPLXUNI-Swarm-Frontend` | `trackable-frontend-orchestration-candidate` | CMPLXUNI binds E8/Leech, unified families, MMDB, ThinkTank, MCP, agent runtime, CLI, and Next.js UI | `production/orchestration` + `production/adapters` + `production/ui` |
| `CQECMPLX-TMN-Role-Family` | `trackable-composite` | TMN/TMN1 expose role/tool family names plus API/Docker/formal signals | `production/tool-families` |
| `CQECMPLX-TMN1-Conservation-Fullstack` | `trackable-fullstack-operations-candidate` | TMN1 docs and infrastructure bind MORSR pulses, E8 transforms, conservation law, Docker roles, channels, economy, and CQE formalizations | `production/operations` + `production/tool-families` + `production/adapters` |
| `CQECMPLX-Product-Fourpack` | `trackable-product-candidate` | historical products expose README/PITCH surfaces, Docker metadata, SDK/package metadata, and monitoring configs | `production/products` + `production/adapters` + `production/proof-receipts` |
| `CQECMPLX-Repo-Accounting` | `trackable-slice` | all 12 top-level repo zips are content-profile-complete; DB and summaries exist | `production/workspace-corpus-index` |
| `CQECMPLX-Paper-Proof-Bundle` | `trackable-publish-candidate` | local production body has papers 00-32, formal folders, intent index, PDFs, and proof receipts | `production/papers` + `production/proof-receipts` |
| `CQECMPLX-ProofValidated-Kernel` | `trackable-composite` | validated hierarchical Docker proof kernel has orchestrator, paper validator, compose, and deployment docs | `production/kernel-runtime` + `production/proof-receipts` |
| `CQECMPLX-NVEST-EG8-Gate` | `trackable-composite` | NVEST and E/G8 share umbrella, CQE, Hidden Guess Result, and adapter layers | `production/diagnostics` + `production/adapters` |
| `CQECMPLX-MORSR-Pulse-Family` | `trackable-staged` | public CMPLX-MORSR and CQE_MORSR scaffolds expose pulse, validation, CQE, and adapter layers | `production/diagnostics` + `production/lib-forge` |
| `CQECMPLX-LibForge-Lattice-ReForge-Ring` | `trackable-composite` | lib-forge, lattice_forge_src, kernel ring, PartsFactory, and Forge packages overlap into one Forge-family layer | `production/lib-forge` |
| `CQECMPLX-Docker-Compose-Boundary` | `trackable-composite` | kernel Docker adapter, compose boundary, ProofValidated compose, and DockerContainers need one boundary route | `production/adapters` + `production/kernel-runtime` |
| `CQECMPLX-Odysseus-MCP-Memory` | `needs-portability-review` | Odysseus has MCP routes, memory routes, vector memory, Docker GPU compose, and tests | `production/adapters` + `production/memory` |
| `CQECMPLX-Analog-Forge-Workbench` | `needs-package-review` | analog Forge workbench has package source, tests, workbook sheets, receipt templates, and PDF reports | `production/tool-families` + `production/proof-receipts` |
| `CQECMPLX-MetaMaterial-Designer` | `trackable-package-candidate` | package-shaped Forge module has paper, Docker, compose, app, tests, and generated reports | `production/lib-forge` + `production/tool-families` |
| `CQECMPLX-Payload-Ledger` | `trackable-ledger` | payload metadata covers MMDB, E8 DBs, vector stores, Manny memory, morphism ledger, and nested archives | `production/payload-ledger` |
| `CQECMPLX-CMPLXNEXT-Orchestration` | `trackable-profile-bound` | Monorepo profile exposes CMPLXNEXT storage, MCP agent net, IDE, and frontend bridge identities | `production/orchestration` |
| `CQECMPLX-TMN-Role-Family` | `trackable-profile-bound` | TMN/TMN1 profiles expose named tool roles and family identities | `production/tool-families` |
| `CQECMPLX-AirLock-CQE-Forge-Lineage` | `trackable-airlock-lineage` | AirLock contains CQE engine mirrors, cqe-production, ForgeFactory lineage, tests, and review docs | `production/airlock-reviewed` + `production/lib-forge` + `production/tool-families` |

## First Publishable Tracking Rule

For now, publishable means the tracking record, proof route, and composite
definition can be committed. It does not mean raw payloads, raw archives, or
full generated corpora should enter the repo.

## Inputs Used

- Existing deployment proof docs in `proofing/`.
- Repo zip accounting database and summaries under
  `D:\CQE_CMPLX\Claude-Codex-Memory\Codex work\CX-Repo-Literal-Accounting`.
- Kernel runtime and ring under `D:\CQE_CMPLX\CMPLX-Kernel`.
- Local production body under `D:\CQE_CMPLX\CQECMPLX-Production`.
- Docker platform under `D:\CQE_CMPLX\DockerContainers`.

## Next Tracking Work

1. Convert the new population queue records into exact promotion manifests.
2. Complete one composite spec per candidate.
3. Run payload expansion only after the payload ledger records exact candidates.
4. Bind paper claims from Production, AirLock, and Kernel roots.
5. Promote indexes and curated forms before raw code movement.

## Population Queue

The active management queue is `tracking/POPULATION_QUEUE.md`.

Machine-readable records are in `tracking/POPULATION_QUEUE.json`.

Source bindings live under `tracking/source-bindings/`.

Promotion manifests live under `tracking/promotion-manifests/`.

Coverage dashboard lives at `tracking/TRACKING_COVERAGE.md`.

Lib-forge package split lives at
`tracking/lib-forge-package-splits/LIB_FORGE_PACKAGE_SPLIT.md`.

Payload ledger lives at `tracking/payload-ledger/PAYLOAD_LEDGER.md`.

Deep review passes live under `tracking/deep-review/`.

Paper claim binding lives at
`tracking/paper-claim-bindings/PAPER_CLAIM_BINDING.md`.
