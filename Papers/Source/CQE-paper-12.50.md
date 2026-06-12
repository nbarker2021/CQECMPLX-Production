# Paper 12.50 - CA Prediction Surface Claim Contract

## Purpose

Paper 12.50 defines what counts as a valid cellular-automaton prediction
surface claim. It separates finite local proof from empirical or open
prediction layers.

## Admitted Paper 12 Claims

The following claims are admitted from Paper 12:

```text
Rule30 local truth table matches L xor (C or R)
T_EMISSION matches Rule30 on all eight LCR states
Rule30 = Rule90 xor (C and not R)
there are eight local LCR states
there are 64 silent-boundary ECAs
cold-start Rule 30 extraction remains open
spectral prediction remains empirical
```

## Claim Requirements

Any later paper using Paper 12 must state:

```text
which CA rule is being used
which local state or depth query is being used
which prediction layer produced the value
the cost class of the layer
the defect or error status of the layer
which receipt proves the layer
which obligations remain open
```

## Linked Receipt

The minimum receipt link for Paper 12 is:

```text
paper: CQE-paper-12
theorem: CA prediction surface finite local layers
receipt: production/formal-papers/CQE-paper-12/ca_prediction_surface_receipt.json
status: pass
```

The receipt is sufficient for the finite local layers. It is not sufficient by
itself for cold-start Rule 30 extraction, spectral prediction accuracy, or
case-by-case closure of all silent-boundary rules.

## Boundary Failures

The following are boundary failures:

```text
claiming spectral prediction is proved by the local receipt
using T_EMISSION without a local LCR state
omitting layer cost or defect
turning the 64-rule count into a universal closure proof
using empirical accuracy as theorem
```

Boundary failures become obligations or are rejected by the consuming paper.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted layer result or scope status
revealed receipt
match/mismatch
next audit boundary if mismatch
```

The cold-start and spectral prompts are required because their correct answer
is open/empirical in this paper.

## Conclusion

Paper 12.50 lets later papers import CA prediction surfaces honestly. It keeps
the exact local layer strong while preventing open prediction layers from
posing as closed theorem.
