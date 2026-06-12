# Paper 02 - Correction Surface

## Abstract

Paper 02 formalizes the first repair layer after the LCR carrier. Once a local
state is represented as `(L, C, R)`, the system needs a disciplined way to
handle mismatch. This paper defines a correction surface as a typed residue map
that records where a simpler linear carrier fails to reproduce the target
transition. The point is not to call every failure a proof. The point is to
prevent failure from being erased.

For the Rule 30 / Rule 90 example already present in the codebase, the
correction surface is finite and exact:

```text
Rule30(L, C, R) = Rule90(L, R) xor correction(L, C, R)
correction(L, C, R) = C and not R
```

The correction fires exactly on the two LCR states `(0,1,0)` and `(1,1,0)`.
This supplies the paper's concrete theorem and its hand-checkable workbook
method.

## Role in the Suite

Paper 01 establishes the minimal local carrier. Paper 02 installs
proofreading: when a proposed transport does not close, the nonclosing part is
stored as a residue with a type, location, and next-step obligation. Later
papers can repair, curve, lift, or ledger that residue because Paper 02 prevents
it from being discarded.

## Definitions

Let `A = {0,1}` and let an LCR state be

```text
s = (L, C, R) in A^3.
```

Define the Rule 30 local update:

```text
R30(L, C, R) = L xor (C or R).
```

Define the Rule 90 local update:

```text
R90(L, R) = L xor R.
```

Define the correction map:

```text
corr(L, C, R) = C and not R.
```

A **correction surface** is the set of local states where `corr` is nonzero,
together with the receipt that records how that residue is fed to the next
transport step.

## Main Claim

**Theorem 2.1, Correction Decomposition.** For every binary LCR state,

```text
R30(L, C, R) = R90(L, R) xor corr(L, C, R).
```

Moreover, `corr` is nonzero exactly on

```text
{(0,1,0), (1,1,0)}.
```

### Proof

Over Boolean values,

```text
C or R = C xor R xor (C and R).
```

Therefore

```text
R30(L, C, R)
  = L xor (C or R)
  = L xor C xor R xor (C and R)
  = (L xor R) xor (C xor (C and R))
  = R90(L, R) xor (C and not R).
```

The last equality holds because `C xor (C and R)` is `1` exactly when `C=1`
and `R=0`, and is `0` otherwise. Thus the correction is `C and not R`.

Enumerating the eight LCR states, `C=1` and `R=0` occurs only for `(0,1,0)`
and `(1,1,0)`. QED.

## Correction Is Not Permission to Overclaim

Paper 02 has a narrow but important epistemic rule:

```text
failed transport -> typed residue -> obligation
```

It does not say:

```text
failed transport -> accepted theorem
```

This distinction matters for the whole suite. A mismatch is positive data only
because it is preserved with enough structure to be tested later. If the
residue is not typed, localized, and replayable, it remains an unresolved
failure.

## D4 Chart Projection

Existing lattice-forge material labels the eight LCR chart states by D4
axis/sheet coordinates. Under that codec, the correction firing states are:

```text
(0,1,0) -> axis 2, sheet 0
(1,1,0) -> axis 3, sheet 1
```

Thus the correction tape can be read as a one-bit projection of the D4 chart
state:

```text
corr != 0 iff (axis, sheet) in {(2,0), (3,1)}.
```

Paper 02 does not require the later D4 or triality claims to be proven here.
It only records the projection that later papers can consume.

## Hand Reconstruction

1. Draw the three LCR cells.
2. Fill each cell with a binary token.
3. Compute `Rule30 = L xor (C or R)`.
4. Compute `Rule90 = L xor R`.
5. Compute `corr = C and not R`.
6. Verify that `Rule30 = Rule90 xor corr`.
7. If `corr = 1`, mark a black residue token.
8. Copy the residue into an obligation row rather than erasing it.

The hand method should produce two firing states and six non-firing states.
The firing states are `(0,1,0)` and `(1,1,0)`.

## Code Reconstruction

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-02/verify_correction_surface.py
```

It verifies:

```text
1. The Rule 30 / Rule 90 / correction identity on all eight LCR states.
2. The exact correction firing set.
3. The D4 axis/sheet projection for the firing states.
4. The residue ledger shape required by the paper.
5. A falsifier: residue is not automatically accepted as proof.
```

## Validation and Hidden-Guess Layer

Paper 02 diagnostics should ask for a prediction before revealing the
correction set:

```text
Which LCR states make C and not R fire?
Does a nonzero correction prove the original route?
What must be recorded before residue can be used by the next paper?
```

The expected answers are:

```text
firing states: (0,1,0), (1,1,0)
proof status: no, correction creates an obligation
required record: state, rule, residue value, source route, next obligation
```

## Open Obligations

1. Wire this verifier into the installable `cqe_engine.formal` interface.
2. Reconcile the D4 axis/sheet labels with Paper 03's triality presentation.
3. Extend the receipt format so later papers can consume correction rows
   directly.
4. Add peer-review citations for Rule 30, Rule 90, Boolean normal forms, and
   cellular automaton linearization.

## Conclusion

Paper 02 converts mismatch into structured work. The proof is finite: the
correction surface is exactly `C and not R`, and it fires on two of the eight
binary LCR states. The scientific discipline is also finite: the residue is
useful only when it is preserved as a replayable obligation. This is why
correction becomes a surface rather than a trash bin.
