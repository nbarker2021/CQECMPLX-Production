# Paper 20.25 - Layer-2 Synthesis Ledger Toolkit

## Purpose

This supplement exposes the ledger checks for Paper 20.

## Digital Route

Run:

```text
python production/formal-papers/CQE-paper-20/verify_layer2_synthesis_ledger.py
```

The receipt must show ledger verification, reachability examples, transport
row counts, and registry accept/reject behavior.

## Analog Route

Use a four-column board:

```text
solved
open
forbidden or failed
transported with residue
```

Place every row in exactly one column and write the witness on the row card.

## Hidden-Guess Diagnostic

Before revealing the row receipt, classify it as:

```text
solved
open
forbidden
transported
invalid promotion
```

Reveal the ledger row only after the classification.

## Boundary

The toolkit may aggregate rows. It may not upgrade a row beyond the source
paper's receipt.

## Conclusion

Paper 20.25 makes the ledger visible as a practical audit board.
