# Paper 30.25 - Grand Ribbon Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 30's corpus ribbon. The proof is
in Paper 30 and its formal verifier. The toolkit exposes the repeated
eight-slot form so a reader can inspect the corpus without mistaking the
framing for a new theorem.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-30/verify_grand_ribbon_meta_framer.py`

The expected status is `pass_with_open_packaging_obligations`. The verifier
checks the slot schema, fills papers 00-29 as a 30-position sweep, builds a
terminal composition route, checks the transport-obligation ledger, and
confirms that Paper 31 is prepared only as readout.

## Analog Route

Draw one long ribbon with eight bins per position:

`C L R B T O W A`

Create positions for papers 00 through 29. At each position, place a center
card, a left-boundary card, a right-boundary card, a boundary-rule card, a
tool/receipt card, an obligation card, a workbook card, and an anchor card.

A bin is closed only when it has both a value and a provenance tag. If the
value exists without provenance, mark it as open. If an obligation exists,
place it in the `O` bin instead of removing it.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- filled ribbon slot,
- unfilled ribbon slot,
- valid provenance row,
- open transport lift,
- invalid hidden lift,
- valid Paper 31 readout,
- invalid Paper 31 dependency.

The answer key distinguishes a proof-stack position from a retrospective
readout.
