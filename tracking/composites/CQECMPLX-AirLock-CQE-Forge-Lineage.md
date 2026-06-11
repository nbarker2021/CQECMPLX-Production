# CQECMPLX-AirLock-CQE-Forge-Lineage

Status: `trackable-airlock-lineage`

Route: `production/airlock-reviewed` + `production/lib-forge` +
`production/tool-families`

## Composite Identity

This composite captures the AirLock lineage material that connects CQE engine,
CQE production packaging, shared memory, ForgeFactory, and LatticeForge/ReForge
lineage.

## Included Families

- CQE engine mirror.
- CQE-engine-v0.1.
- cqe-production-v0.1 package body.
- ForgeFactory v0.3 lineage read.
- CQE shared memory.
- ManiForge and MandleForge stubs.
- Paper/tool/workbook test material.

## Boundary Rule

AirLock is a review and lineage source. It must not be promoted as a raw folder.

The production route is:

1. lineage docs;
2. source comparison against existing production/lib-forge forms;
3. reviewed package slices;
4. tests and receipts.

## Hard Exclusions

- `.venv`
- `.pytest_cache`
- `__pycache__`
- bytecode and executables
- local runtime metadata

## Source Bindings

- `tracking/source-bindings/CQECMPLX-AirLock-CQE-Forge-Lineage.json`
- `tracking/promotion-manifests/CQECMPLX-AirLock-CQE-Forge-Lineage.manifest.json`
