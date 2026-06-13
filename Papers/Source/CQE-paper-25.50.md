# Paper 25.50 - Energetic Traversal Claim Contract

## Purpose

This contract defines the minimum fields required before a traversal claim can
be promoted from example to paper evidence.

## Required Fields

Each step must provide a path id, step id, source object, target object,
transport id, `(L, C, R)` state, Noether residue, Shannon residue, Landauer
cost, absorption capacity, weights `alpha`, `beta`, `gamma`, computed `theta`,
unit policy, step closure status, and obligation label when present.

Each path must provide the ordered step list, `theta_path`, path closure status,
open-step ids, and a Boolean statement of whether physical energy is claimed.
For Paper 25 the physical-energy Boolean must remain false.

## Promotion Rules

A row may be promoted when its `theta` is replayable from the NSL fields and
its unit policy is declared. A path may be promoted when its total is replayable
from its rows and all open rows are preserved.

The following promotions are rejected:

- analog `theta` to physical joules without calibration,
- `theta <= 0` to thermodynamic optimum,
- smaller `theta_path` to geodesic or least-action proof without a domain
  metric,
- NSL accounting to physical-law unification,
- uncalibrated absorption to measured absorption.

## Linked Review

The paper may speak forward to later applied tools by exporting the row schema.
It may speak backward to Paper 00 by strengthening the unit-honesty and
obligation-carry rules. It may not hide open lifts behind positive language.
