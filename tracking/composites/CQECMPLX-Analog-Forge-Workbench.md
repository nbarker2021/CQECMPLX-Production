# CQECMPLX-Analog-Forge-Workbench

Status: `needs-package-review`

Route: `production/tool-families` + `production/proof-receipts`

## Composite Identity

`CQECMPLX-Analog-Forge-Workbench` is a ForgeFactory analog package for workbook,
simulation, receipt, and report generation flows.

## Included Families

- package source under `forgefactory_analog_workbench`;
- workbook sheet templates;
- receipt templates;
- simulation and operator code;
- package metadata;
- tests;
- generated exports and PDFs as deferred publication artifacts.

## Production Rule

Promote source, docs, sheets, package metadata, and tests first.

Generated exports, notebooks, and PDFs require a publication manifest because
they are outputs, not the package core.

## Source Bindings

- `tracking/source-bindings/CQECMPLX-Analog-Forge-Workbench.json`
- `tracking/promotion-manifests/CQECMPLX-Analog-Forge-Workbench.manifest.json`
