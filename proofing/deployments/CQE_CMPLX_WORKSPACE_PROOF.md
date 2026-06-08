# CQE_CMPLX Workspace Deployment Proof

## Identity

- Root: `CQE_CMPLX`
- Local path: `D:\CQE_CMPLX`
- Claimed role: active development corpus and source workspace.
- Production interpretation: master staging/workbench root for Forge family,
  MORSR, NVEST, CQE-G8, PartsFactory, R30, papers, products, and archives.

## Deployment Surfaces

- Runtime: many; must be classified per sub-root.
- Services: product folders and package repos.
- Docker/K8s: present in some sub-roots.
- MCP/API: likely in CMPLX/PartsFactory/MCP-adjacent folders.
- File-fed/sidecar: kernel and Forge-family docs use file-fed patterns.
- Data/corpus: full workspace capture included in kernel production package.

## Proof Artifacts

- `ForgeFamilyBlueprint/`
- `CMPLX-MORSR/`
- `CQE_MORSR/`
- `CMPLX-NVEST/`
- `CQE-E_G8/`
- non-lib Forge index inside CMPLX-Kernel package.
- workspace index inside CMPLX-Kernel package.

## Adapter Boundary

- Binary Boundary Adapter: globally required for new tools.
- Universal Adapter: globally required for host/network handshakes.
- Network/API handshakes: discover per tool.
- Hidden Guess Result mode: quiet by default; required only in training/local
  diagnostics.

## Production Split

Reusable lib behavior:

- `CMPLX-PartsFactory-main/src/cmplx/engine`
- Fourier engine vehicle.
- creator/formal math engine.
- Forge family contract/adapters.

Product/source/corpus material:

- papers;
- R30 packages;
- product_* roots;
- Forge/ReForge archives;
- MORSR/NVEST/CQE-G8 umbrellas.

Excluded or airlocked:

- raw archive dumps;
- duplicate/generated package content;
- caches/venvs/test scratches;
- anything without manifest/receipt.

## Risks

- Very large mixed-purpose workspace.
- Many overlapping source-of-truth candidates.
- Some materials are archives of other repos/packages.

## Promotion Decision

State: `staged`

First safe slice:

- method umbrellas;
- portable lib delta;
- Forge family contracts;
- proofing indexes.

Required gates:

- per-subroot deployment proof;
- per-tool manifest;
- adapter boundary receipts.

