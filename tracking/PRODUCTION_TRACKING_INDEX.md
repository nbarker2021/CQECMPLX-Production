# Production Tracking Index

This is the first index of material that is done enough to track for eventual
publication in `nbarker2021/CQECMPLX-Production`.

The index tracks composites. It does not choose a winner among duplicates.

## Composite Candidates

| Composite | Status | Why It Is Trackable | First Production Route |
|---|---|---|---|
| `CQECMPLX-Kernel-Sidecar` | `trackable-slice` | sidecar runtime, operator web, Docker deploy, module/data contracts, deployment proofs | `production/kernel-runtime` |
| `CQECMPLX-Docker-Operator` | `trackable-composite` | kernel Docker proof, Docker tool adapter, Compose boundary, D:\DockerContainers platform evidence | `production/kernel-runtime` + `production/adapters` |
| `CQECMPLX-LatticeForge-ReForge` | `trackable-composite` | PartsFactory lattice-forge, ReForge/Forge kernel ring, morphism ledger payload, lattice/forge claim density | `production/lib-forge` |
| `CQECMPLX-E8-MORSR-Diagnostics` | `trackable-composite` | E8/MORSR/CQE names recur across repo profiles, kernel ring, R30/Formalization proof bridge | `production/proof-receipts` + `production/lib-forge` |
| `CQECMPLX-MCP-API-Tooling` | `trackable-composite` | CMPLXMCP content-profile complete, MCP/API surfaces in DevKit, Monorepo, DockerContainers MCP toolkit | `production/adapters` |
| `CQECMPLX-Formalization-R30-Proof` | `trackable-proof` | Formalization and R30 are proof/lattice/theorem/paper dense and cross-reference PartsFactory | `production/papers` + `production/proof-receipts` |
| `CQECMPLX-MMDB-E8-Vector-Payloads` | `trackable-payload` | CMPLX/CMPLXUNI DB payload candidates include MMDB, vector stores, E8 DBs | `production/payload-ledger` |
| `CQECMPLX-Manny-Memory-Instruction-Payloads` | `trackable-payload` | Manny contains memory and instruction SQLite payloads with Docker/Compose/MCP evidence | `production/payload-ledger` |
| `CQECMPLX-CMPLXNEXT-Orchestration` | `trackable-composite` | Monorepo exposes CMPLXNEXT storage, MCP agent net, IDE, frontend bridge terms | `production/orchestration` |
| `CQECMPLX-TMN-Role-Family` | `trackable-composite` | TMN/TMN1 expose role/tool family names plus API/Docker/formal signals | `production/tool-families` |
| `CQECMPLX-Repo-Accounting` | `trackable-slice` | all 12 top-level repo zips are content-profile-complete; DB and summaries exist | `production/workspace-corpus-index` |

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

1. Create one composite spec per candidate.
2. Bind each candidate to source paths and proof docs.
3. Run payload expansion only after the payload ledger records exact candidates.
4. Bind paper claims from Production, AirLock, and Kernel roots.
