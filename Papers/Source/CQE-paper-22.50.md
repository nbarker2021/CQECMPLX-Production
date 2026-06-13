# Paper 22.50 - MetaForge Claim Contract

## Admission Rule

A Paper 22 claim is admitted only when it is framed as a materials candidate
unless simulation, fabrication, and measurement receipts are attached. A
candidate must include material-source rows, partner-selection scores, fold
output, seam/obligation rows, production accounting, and a falsifier.

## Required Fields

Each candidate row must provide:

- base material,
- partner material,
- source database or custom-file receipt,
- Pareto score and component scores,
- fold count,
- final candidate estimates,
- error-wall summary,
- seam proposals or explicit no-seam reason,
- production-energy estimate,
- cost/time estimate,
- open obligations,
- falsification condition.

## Rejected Promotions

The following promotions are not allowed:

- candidate estimate to measured material property,
- positive production estimate to manufacturability proof,
- seam proposal to validated interface design,
- fold output to finite-element result,
- predicted auxetic sign to measured Poisson ratio,
- package visualization to experimental evidence,
- material database row to certified supplier data.

## Falsifiers

A candidate row is falsified if the partner score cannot be reproduced, if the
fold count or final estimates change without a changed receipt, if a seam row is
missing for a declared boundary issue, if production energy or cost is absent,
or if a fabricated sample contradicts the predicted behavior.

## Carry Rule

Later papers may import Paper 22 as an applied-materials candidate generator.
They inherit its open obligations unless they provide stronger domain receipts.
