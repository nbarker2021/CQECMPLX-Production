# Production Population Queue

Created: 2026-06-11

This queue identifies material that can populate `nbarker2021/CQECMPLX-Production`.
It is an aggregation queue, not a final merge list. When multiple roots express the
same identity, the production action is to build a composite form and keep source
lineage visible.

## Population Rules

- Track first, copy later.
- Preserve duplicate evidence until a composite form explains the union.
- Promote code only through a named route with a source binding and gate status.
- Do not bring caches, bytecode, virtual environments, raw zip files, or local
  runtime debris into production.
- Non-math diagnostics require Hidden Guess Result when training mode is enabled.
- External handshakes require Binary Boundary Adapter and Universal Adapter
  Program bindings.

## Ready To Track Now

| ID | Production Route | Current Shape | Source Binding | Next Action |
|---|---|---|---|---|
| `CQECMPLX-Paper-Proof-Bundle` | `production/papers` + `production/proof-receipts` | papers 00-32, formal folders, PDFs, proof receipts, paper intent index | `tracking/source-bindings/CQECMPLX-Paper-Proof-Bundle.json` | make exact publish manifest for text papers first, then receipts |
| `CQECMPLX-ProofValidated-Kernel` | `production/kernel-runtime` + `production/proof-receipts` | Docker-in-Docker proof kernel, orchestrator, paper validator, operator docs | `tracking/source-bindings/CQECMPLX-ProofValidated-Kernel.json` | compare against `CQECMPLX-Kernel-Sidecar` and build a composite runtime slice |
| `CQECMPLX-NVEST-EG8-Gate` | `production/diagnostics` + `production/adapters` | CMPLX-NVEST wave diagnostic umbrella paired with CQE-E/G8 gate | `tracking/source-bindings/CQECMPLX-NVEST-EG8-Gate.json` | add composite spec and bind Hidden Guess Result schema as required diagnostic gate |
| `CQECMPLX-MORSR-Pulse-Family` | `production/diagnostics` + `production/lib-forge` | CMPLX-MORSR and CQE_MORSR staged pulse/validation umbrellas | `tracking/source-bindings/CQECMPLX-MORSR-Pulse-Family.json` | keep staged until later private MORSR source is supplied; track local public scaffold now |
| `CQECMPLX-LibForge-Lattice-ReForge-Ring` | `production/lib-forge` | lib-forge, lattice_forge_src, ChromaForge, GraphStax, PixelForge, kernel ring | `tracking/source-bindings/CQECMPLX-LibForge-Lattice-ReForge-Ring.json` | aggregate Forge identities into package families before copying code |
| `CQECMPLX-Docker-Compose-Boundary` | `production/adapters` + `production/kernel-runtime` | kernel Docker adapter, compose boundary inserts, DockerContainers platform, validated suite compose | `tracking/source-bindings/CQECMPLX-Docker-Compose-Boundary.json` | build one compose boundary manifest that separates internal-below-kernel and external-insert needs |
| `CQECMPLX-DevKit-MCPOS-MORSR-Runtime` | `production/adapters` + `production/kernel-runtime` + `production/diagnostics` | DevKit MCP OS runtime with CQE layer tools, MORSR optimization, handle-based heavy data, validation, and AGRM/MDHG | `tracking/source-bindings/CQECMPLX-DevKit-MCPOS-MORSR-Runtime.json` | promote docs/inventory first, then review source for sidecar runtime import viability |
| `CQECMPLX-Repo-Forms-Accounting` | `production/workspace-corpus-index` | curated repo forms plus literal zip accounting database and summaries | `tracking/source-bindings/CQECMPLX-Repo-Forms-Accounting.json` | publish indexes and forms, not raw zips |
| `CQECMPLX-Odysseus-MCP-Memory` | `production/adapters` + `production/memory` | Odysseus MCP, memory routes, vector memory, Docker GPU compose | `tracking/source-bindings/CQECMPLX-Odysseus-MCP-Memory.json` | treat as adapter/memory module candidate under lib-forge after portability review |
| `CQECMPLX-Analog-Forge-Workbench` | `production/tool-families` + `production/proof-receipts` | ForgeFactory analog workbook/simulation/receipt package | `tracking/source-bindings/CQECMPLX-Analog-Forge-Workbench.json` | inspect tests and package metadata before promotion |
| `CQECMPLX-MetaMaterial-Designer` | `production/lib-forge` + `production/tool-families` | package-shaped Forge module with paper, Docker, app, tests, and generated reports | `tracking/source-bindings/CQECMPLX-MetaMaterial-Designer.json` | promote source/package files first; defer generated reports |
| `CQECMPLX-Payload-Ledger` | `production/payload-ledger` | metadata ledger for databases, nested archives, vector stores, and memory payloads | `tracking/source-bindings/CQECMPLX-Payload-Ledger.json` | commit metadata before any binary payload movement |
| `CQECMPLX-CMPLXNEXT-Orchestration` | `production/orchestration` | monorepo profile shows CMPLXNEXT storage, MCP agent net, IDE, and frontend bridge identities | `tracking/source-bindings/CQECMPLX-CMPLXNEXT-Orchestration.json` | promote orchestration map before code |
| `CQECMPLX-CMPLXUNI-Swarm-Frontend` | `production/orchestration` + `production/adapters` + `production/ui` | CMPLXUNI exposes E8/Leech, MMDB, ThinkTank, MCP, swarm chat, agent runtime, CLI, and Next.js UI | `tracking/source-bindings/CQECMPLX-CMPLXUNI-Swarm-Frontend.json` | promote docs/config templates first, then review UI build path |
| `CQECMPLX-TMN-Role-Family` | `production/tool-families` | TMN/TMN1 expose role names and tool-family identities | `tracking/source-bindings/CQECMPLX-TMN-Role-Family.json` | promote role taxonomy before per-role code |
| `CQECMPLX-TMN1-Conservation-Fullstack` | `production/operations` + `production/tool-families` + `production/adapters` | TMN1 exposes MORSR pulses, E8 transforms, conservation enforcement, Docker fullstack, channels, and economy | `tracking/source-bindings/CQECMPLX-TMN1-Conservation-Fullstack.json` | promote operational docs first; ledger large formalization JSON |
| `CQECMPLX-Product-Fourpack` | `production/products` + `production/adapters` + `production/proof-receipts` | product_authentica/converge/entropy/sentinel expose product docs, Docker, SDK/package, and monitoring metadata | `tracking/source-bindings/CQECMPLX-Product-Fourpack.json` | promote docs/deploy metadata first; bind product claims before public wording |
| `CQECMPLX-AirLock-CQE-Forge-Lineage` | `production/airlock-reviewed` + `production/lib-forge` + `production/tool-families` | AirLock CQE engine, cqe-production, and ForgeFactory lineage source | `tracking/source-bindings/CQECMPLX-AirLock-CQE-Forge-Lineage.json` | promote lineage docs and reviewed source slices only |

## Near Candidates

These are visible enough to keep in view, but need one more pass before they
become first-class population records:

| Candidate | Reason To Watch | Needed Next |
|---|---|---|
| `CQECMPLX-Manny-Memory-Instruction-Payloads` | SQLite memory/instruction payloads are already identified in repo accounting | payload ledger expansion |
| `CQECMPLX-MMDB-E8-Vector-Payloads` | MMDB, E8, and vector stores recur in zips and code roots | payload ledger expansion |

## Current Finding

The population space is large enough that the production repo should not become a
mirror of the workspace. It should become the management plane: records, source
bindings, composite specs, promotion manifests, and then curated production code
only after each slice has an explicit boundary.

## Manifest Layer

Promotion manifests now live in `tracking/promotion-manifests/`.

First manifest-ready slices:

- `CQECMPLX-Paper-Proof-Bundle`
- `CQECMPLX-ProofValidated-Kernel`
- `CQECMPLX-NVEST-EG8-Gate`
- `CQECMPLX-Docker-Compose-Boundary`
- `CQECMPLX-DevKit-MCPOS-MORSR-Runtime`
- `CQECMPLX-Repo-Forms-Accounting`
- `CQECMPLX-LibForge-Lattice-ReForge-Ring`
- `CQECMPLX-MetaMaterial-Designer`
- `CQECMPLX-Payload-Ledger`
- `CQECMPLX-CMPLXNEXT-Orchestration`
- `CQECMPLX-CMPLXUNI-Swarm-Frontend`
- `CQECMPLX-TMN-Role-Family`
- `CQECMPLX-TMN1-Conservation-Fullstack`
- `CQECMPLX-Product-Fourpack`
- `CQECMPLX-AirLock-CQE-Forge-Lineage`
- `CQECMPLX-MORSR-Pulse-Family`
- `CQECMPLX-Odysseus-MCP-Memory`
- `CQECMPLX-Analog-Forge-Workbench`

These manifests are allowed-path records. They do not copy source files by
themselves.
