# Paper 31.25 - Meta LCR Readout Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 31's retrospective readout. The
proof is in Paper 31 and its formal verifier. The toolkit is for walking the
corpus as LCR without converting the walk into hidden proof support.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-31/verify_meta_lcr_readout.py`

The expected status is `pass_as_retrospective_readout`. The verifier checks
gluon invariance, the Rule 30 truth table, the Paper 30 receipt, dependency
direction, and the forward link to Paper 32.

## Analog Route

Take the Paper 30 ribbon. For each paper position, read three cards:

`L = inherited context`

`C = selected thesis`

`R = residue or next target`

After each read, copy the residue forward instead of erasing it. At Paper 30,
tie the right boundary to Paper 31 as readout. At Paper 31, point the forward
boundary to Paper 32 as package/deployment target.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- center invariant,
- Rule 30 boundary row,
- valid retrospective readout,
- invalid upstream dependency,
- standing open obligation,
- valid Paper 32 forward target.

The answer key separates "explains the stack" from "proves the stack."
