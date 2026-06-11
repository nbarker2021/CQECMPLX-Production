# CQE_MORSR Library Bindings

## CQE Engine

Use CQE to:

- derive the C centroid from problem context
- package validation questions
- select operation mode
- attach MORSR diagnostics during solve/validate phases

## `cmplx.nsl`

Use NSL to:

- score recentering steps
- enforce or signal conservation
- provide `delta_phi` for receipts

## `cmplx.receipt`

Use receipts to:

- store sealed-result references
- record guess commits
- record reveal events
- record score and map updates

## `cmplx.morphon`

Use morphons for:

- CQE atom identity
- confirmed nodes
- parent/child recenter chain

## Wave/Market Tools

Use these as domain-neutral sniffers:

- wave centroid mismatch
- phase transition detection
- estimator ablation
- failure/success point localization

The market form is one application surface, not the engine identity.
