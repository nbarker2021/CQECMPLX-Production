# Paper 1.50 - LCR Claim Contract

## Purpose

Paper 1.50 defines what counts as a valid claim about the LCR carrier. It is a
meta-review layer between Paper 1 and the papers that depend on Paper 1.

## Admitted Paper 1 Claims

The following claims are admitted from Paper 1:

```text
LCR is the minimal carrier for one center and two boundary addresses.
Binary LCR has exactly eight states.
Left-right reversal preserves C.
Left-right reversal is an involution.
Binary shell counts are 1,3,3,1.
The shell-2 state (1,0,1) disproves boundary-value inequality.
The shell-2 stratum supplies the side-flip doublet interface.
```

## Claim Requirements

Any later paper using LCR must state:

```text
which center is being preserved
which boundary addresses are being read
which transform is applied
which Paper 1 result is being imported
whether the use is proved, bounded, candidate, or obligation
```

A later paper may not silently treat value inequality as the definition of
opposition. Opposition is an address relation.

## Linked Receipt

The minimum receipt link for Paper 1 is:

```text
paper: CQE-paper-01
theorem: Minimal LCR carrier
receipt: production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json
status: pass
```

The receipt is sufficient for the finite carrier facts. It is not sufficient
by itself for the full `J_3(O)` registration or Standard Model extension
claims.

## Boundary Failures

The following are boundary failures:

```text
claiming L and R are opposed because their values differ
using a two-address carrier while claiming one center and two boundaries
moving C without declaring a recentering
using the shell-2 doublet as a full physics proof without later-paper support
```

Boundary failures are not deleted. They are routed to obligation or later
paper support.

## Conclusion

Paper 1.50 lets later papers import the LCR carrier honestly. It preserves the
finite proof while preventing overclaiming.
