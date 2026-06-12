# Paper 2.50 - Correction Surface Claim Contract

## Purpose

Paper 2.50 defines what counts as a valid claim about the Paper 2 correction
surface. It is the contract that prevents a residue from being hidden,
overpromoted, or imported without its receipt.

## Admitted Paper 2 Claims

The following claims are admitted from Paper 2:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
the correction fires exactly on (0,1,0) and (1,1,0)
the firing rows project to D4 coordinates (2,0) and (3,1)
nonzero correction is an obligation-bearing residue, not proof closure
```

## Claim Requirements

Any later paper using the Paper 2 correction surface must state:

```text
which LCR state is being used
which update route is being compared
whether the correction value is 0 or 1
which receipt proves the correction row
whether the row is closed, obligation, candidate, or downstream proof input
```

## Linked Receipt

The minimum receipt link for Paper 2 is:

```text
paper: CQE-paper-02
theorem: Correction surface decomposition
receipt: production/formal-papers/CQE-paper-02/correction_surface_receipt.json
status: pass
```

The receipt is sufficient for the finite Rule 30 / Rule 90 correction theorem.
It is not sufficient by itself for full D4 triality, boundary repair, or
physical interpretation claims.

## Boundary Failures

The following are boundary failures:

```text
counting nonzero residue as a closed proof
using a correction row without naming the source state
changing the firing set without rerunning the verifier
importing D4 coordinates while claiming Paper 2 proves full D4 triality
dropping the failed route that produced the residue
```

Boundary failures are not deleted. They become typed obligations for Paper 3,
Paper 4, or later repair layers.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted firing set
predicted proof status
revealed receipt
match/mismatch
next obligation if mismatch
```

This keeps the diagnostic useful as training data without allowing the answer
to leak into the prediction.

## Conclusion

Paper 2.50 lets later papers import the correction surface honestly. It keeps
the finite theorem available while preserving the distinction between residue,
obligation, and proof.
