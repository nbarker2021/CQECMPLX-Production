# Paper 19 - Observer Face-Selection

## Abstract

This paper defines observation as selecting one face of a local registered
state while retaining the unselected faces as obligations. The closed result is
finite: four frame faces are available, selecting one retains three latent
faces, the gluon coordinate `C` is invariant under `L <-> R` antipodal
reversal over all eight chart states, and the static `Z4` face template splits
as two fixed points plus six period-4 states. Bounded Monster-D4 route evidence
supports the observer-face reading after all eight chart states activate, but
it remains labeled `pass_with_open_gaps`.

This paper does not prove consciousness, physical measurement collapse, a
completed SPINOR signature, or a global observer theorem.

## Claims

**Claim 19.1.** The observer has four selectable frame faces:
`C-centroid`, `R-centroid`, `C-flipped`, and `L-centroid`.

**Claim 19.2.** Selecting one face retains exactly three latent faces.

**Claim 19.3.** The gluon coordinate `C` is invariant under `L <-> R`
antipodal reversal for all eight chart states.

**Claim 19.4.** The static `Z4` face template has two fixed points, zero
period-2 states, and six period-4 states.

**Claim 19.5.** The bounded observer-route harness provides evidence after
all eight chart states activate, but remains open-gap evidence.

## Definitions

A **face** is one selectable reading of the local chart: a frame, chirality, or
dyad side.

**Face selection** is the act of committing one face as active.

A **latent face** is an unselected face carried forward with a recovery rule.

The **gluon** is the coordinate `C`, the locally invariant midpoint of the
`L | C | R` window.

An **open observer promotion** is any claim that turns this finite selection
machinery into consciousness, physical collapse, or an unverified SPINOR
signature.

## Theorem 19

Observation in the CQE paper suite is admissible as finite face selection with
retained latent alternatives:

```text
select one face -> keep three latent faces -> preserve C -> record residue
```

and no stronger observer claim is closed here.

## Proof

The verifier defines four frame faces. This proves Claim 19.1.

For each face index `0..3`, the verifier selects one face and records the
other three as latent. This proves Claim 19.2.

The gluon-invariance verifier checks all eight chart states. For each state,
`gluon(s) = C` and `gluon(swap_LR(s)) = C`. This proves Claim 19.3 and gives
the reconstruction rule for antipodal unselected faces.

The `Z4` template verifier reports two fixed points, no period-2 states, and
six period-4 states. This proves Claim 19.4.

The Monster-D4 lift harness reports `pass_with_open_gaps` with all eight chart
states enumerated and D4 lift preserved after activation. Because the harness
also carries open-gap status, it supports the observer-route reading without
closing a global observer theorem. This proves Claim 19.5.

Together these claims prove the theorem.

## Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-19/verify_observer_face_selection.py
```

Receipt:

```text
production/formal-papers/CQE-paper-19/observer_face_selection_receipt.json
```

Closed layers:

```text
four selectable frame faces
one selected face retains three latent faces
gluon C invariant under LR antipodal reversal
static Z4 face template: 2 fixed, 0 period-2, 6 period-4
bounded observer-route evidence after eight-state activation
```

Open layers:

```text
SPINOR signature observation
full frame-inversion Q(S) executable binding in the promoted layer
consciousness or measurement-collapse interpretation
global physical observer theorem
```

## Falsifiers

The paper fails if selected faces delete latent faces.

It fails if `C` changes under antipodal reversal.

It fails if the `Z4` template contains period-2 states.

It fails if open-gap observer evidence is promoted as a completed theorem.

It fails if SPINOR is claimed observed without a receipt.

## Role in the Suite

Paper 18 exports bounded representation routes. Paper 19 says how an observer
selects a face of such a route without deleting the alternatives. Paper 20 can
therefore ledger each selected face and each retained obligation separately.

## Conclusion

Paper 19 closes finite observer face-selection. The selection mechanism is
useful precisely because it preserves the unselected faces instead of turning
them into hidden assumptions.
