# CQECMPLX-AirLock Deployment Proof

## Identity

- Root: `CQECMPLX-AirLock`
- Local path: `D:\CQECMPLX-AirLock`
- Claimed role: airlock/quarantine/review intake.
- Production interpretation: controlled intake zone for artifacts not yet proven
  production-shaped.

## Deployment Surfaces

- Runtime: staged materials only.
- Services: possible staged service folders.
- Docker/K8s: possible staged package content.
- MCP/API: possible staged package content.
- File-fed/sidecar: possible staged package content.
- Data/corpus: lineage/read/review packages and mirrored engines.

## Proof Artifacts

- Included in CMPLX-Kernel production package.
- Needs dedicated manifest and review receipts in the production repo.

## Adapter Boundary

- Binary Boundary Adapter: required before any artifact exits the airlock.
- Universal Adapter: required for any host/tool integration.
- Network/API handshakes: must be discovered per artifact.
- Hidden Guess Result mode: training mode only unless local diagnostic run.

## Production Split

Reusable lib behavior:

- Unknown until per-artifact review.

Product/source/corpus material:

- package intake;
- lineage reads;
- production mirrors.

Excluded or airlocked:

- everything remains airlocked until manifest and portability review exist.

## Risks

- Airlock may contain caches, venvs, test scratches, and generated metadata.
- Source-of-truth may overlap with `D:\CQE_CMPLX` and `D:\CMPLX-Kernel`.

## Promotion Decision

State: `airlock`

First safe slice:

- airlock index and artifact manifest only.

Required gates:

- create full airlock manifest;
- classify each artifact;
- prove destination before copy.

