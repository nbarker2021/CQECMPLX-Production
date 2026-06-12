# Paper 5.75 - Oloid Path Carrier as Next-State Precondition

## Purpose

Paper 5.75 explains how the rolling path carrier becomes a precondition for
Paper 6 and later accumulated-center papers.

## Exported State

Paper 5 exports:

```text
rolling trace
legal adjacent-step relation
head/tail dyads
payload attachment rule
invalid-bit rejection
discontinuous-jump rejection
scope boundary: no prediction claim
```

## Use in Paper 6

Paper 6 may register Paper 5 outputs as causal proof edges. The edge must
preserve:

```text
source paper
target paper
edge type
receipt
status
```

Paper 5 proves path continuity. Paper 6 proves that the dependency graph
records that continuity without hiding obligations.

## Use in Paper 7

Paper 7 may sample or visualize a carried trace only if it preserves the
original discrete receipt. Interpolation or presentation cannot erase the
rolling trace that Paper 5 proves.

## Use in Later Papers

Later papers may use Paper 5 as the carrier for:

- accumulated center state,
- Hamiltonian window inputs,
- mass-residue carriers,
- lattice-boundary payload transport,
- product and adapter workflows.

Every use must state whether it imports the finite carrier theorem or proves a
new prediction/physics claim.

## Precondition Rule

Before a later paper uses Paper 5, it should be able to answer:

```text
What is the input stream?
What is the current rolling state?
Which adjacent step proves continuity?
What payload is carried?
Does the payload alter the path rule?
Which receipt proves the carrier fact?
```

## Conclusion

Paper 5.75 turns the rolling path theorem into portable state. It exports a
legal carrier that can move repaired constraints forward while keeping
prediction and physical interpretation tied to their own later receipts.
