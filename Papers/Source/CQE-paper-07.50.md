# Paper 7.50 - Discrete-Continuous Bridge Claim Contract

## Purpose

Paper 7.50 defines what counts as a valid bridge claim. It preserves the
discrete proof while allowing continuous presentation.

## Admitted Paper 7 Claims

The following claims are admitted from Paper 7:

```text
finite numeric traces admit piecewise-linear interpolation
integer samples are preserved exactly
maximum sample error is zero
adjacent segments share endpoints
Rule30/Rule90 correction identity remains true on indexed LCR states
between-sample physics remains an obligation
```

## Claim Requirements

Any later paper using a Paper 7 bridge must state:

```text
the original indexed trace
the interpolation rule
the sample preservation receipt
whether any between-sample claim is being made
which separate receipt proves any between-sample claim
```

## Linked Receipt

The minimum receipt link for Paper 7 is:

```text
paper: CQE-paper-07
theorem: Sample-preserving discrete-continuous bridge
receipt: production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json
status: pass
```

The receipt is sufficient for sample preservation. It is not sufficient by
itself for Hamiltonian dynamics, continuum collapse, CMB interpretation,
Hawking claims, or any physical uniqueness between samples.

## Boundary Failures

The following are boundary failures:

```text
erasing the original discrete receipt after drawing the bridge
claiming a curve proves physical dynamics between samples
changing indexed sample values without a new receipt
using interpolation to hide correction or residual rows
importing continuous-field language without naming the trace
```

Boundary failures become obligations or are rejected by the consuming paper.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted sample error or scope status
revealed receipt
match/mismatch
next obligation if mismatch
```

The between-sample overclaim prompt is required because the correct answer is
negative.

## Conclusion

Paper 7.50 lets later papers use continuous presentations honestly. It admits
sample preservation while keeping physical dynamics tied to separate proof.
