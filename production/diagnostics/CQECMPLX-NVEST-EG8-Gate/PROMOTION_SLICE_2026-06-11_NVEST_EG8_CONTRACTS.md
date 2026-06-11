# Promotion Slice: NVEST/E_G8 Diagnostic Contracts

Date: 2026-06-11

Source binding:

```text
tracking/source-bindings/CQECMPLX-NVEST-EG8-Gate.json
```

Promotion manifest:

```text
tracking/promotion-manifests/CQECMPLX-NVEST-EG8-Gate.manifest.json
```

## Included

- `CMPLX-NVEST` umbrella, manifest, engine, honesty, integration, CQE, staging,
  and universal adapter records.
- `CQE-E_G8` matching umbrella, manifest, engine, honesty, integration, CQE,
  staging, and universal adapter records.

## Counts

- Diagnostic contract files: 40
- Approximate bytes: 26869

## Required Behavior

Non-math diagnostics require Hidden Guess Result when training mode is enabled.

External handshakes require:

- Binary Boundary Adapter
- Universal Adapter Programs
- CQE bridge layer

## Reason

This slice gives the production repo the first diagnostic honesty and adapter
contract layer without importing runtime code.
