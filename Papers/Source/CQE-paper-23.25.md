# Paper 23.25 - FoldForge Toolkit Supplement

## Purpose

This supplement explains how to reproduce the FoldForge descriptor receipt. It
is support material. The proof-carrying item is Paper 23 and its formal receipt.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-23/verify_foldforge_descriptor.py`

The expected status is `pass_with_open_obligations`. The verifier writes
`foldforge_descriptor_receipt.json` and checks residue-window construction,
contact-map symmetry, candidate bifurcation marks, bounded winding evidence,
oloid-predictor defects, and bifurcation-detector open gaps.

## Analog Route

Write the residue chain as beads on a line. Mark each bead as hydrophobic or
not. For every interior bead, place `L`, `C`, and `R` markers on the previous,
current, and next bead. Draw a contact when two hydrophobic beads are separated
by at least three positions. The contact drawing is the analog contact map. Mark
side changes in the local windows as candidate turn events.

This does not predict a native structure. It shows that the same descriptor can
be replayed without software.

## Hidden-Guess Diagnostic

Training mode should hide the diagnostic label until after the reviewer chooses
one:

- valid residue window,
- invalid residue window,
- contact-map receipt,
- candidate bifurcation,
- bounded winding witness,
- open biological obligation,
- invalid structure-prediction promotion.

The revealed answer trains the difference between a descriptor and a biological
claim.
