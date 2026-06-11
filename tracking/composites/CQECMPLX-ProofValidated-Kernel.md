# CQECMPLX-ProofValidated-Kernel

Status: `trackable-composite`

Route: `production/kernel-runtime` + `production/proof-receipts`

## Composite Identity

`CQECMPLX-ProofValidated-Kernel` is the hierarchical proof validation runtime
slice. It combines the ProofValidatedSuite kernel with the existing sidecar
kernel direction.

## Included Families

- Docker-in-Docker validated compose.
- master orchestrator.
- per-paper validator.
- falsifier.
- workbook/isomorphism modules.
- module registry.
- operator server and operator web console.
- schemas and examples.
- deployment and architecture docs.

## Production Rule

This does not replace `CQECMPLX-Kernel-Sidecar`. It must be reconciled into a
composite runtime slice that preserves sidecar behavior, Docker boundary rules,
module contracts, and proof receipt generation.

## Gates

- Python syntax check.
- compose boundary review.
- runtime data exclusion.
- Hidden Guess Result toggle represented where diagnostics run.

## Source Bindings

- `tracking/source-bindings/CQECMPLX-ProofValidated-Kernel.json`
- `tracking/promotion-manifests/CQECMPLX-ProofValidated-Kernel.manifest.json`
