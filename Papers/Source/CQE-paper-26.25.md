# Paper 26.25 - Z-Pinch and Shear Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 26's carrier and shear receipt.
The proof is in Paper 26 and its formal verifier; the physical Z-pinch reading
is not discharged here.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-26/verify_zpinch_shear_horizon.py`

The expected status is `pass_with_open_obligations`. The verifier checks the
integer Oloid period, octonion period, octonion non-associativity, the 16-bit
Rule 30 carrier shear probe, and the transport-ledger pinch classification.

## Analog Route

Draw a four-position rolling strip. Advance one quarter turn per tape bit and
record sheet, phase, and parity. Beside it, draw two orient threads, one for
the `e4` carrier and one for the `e5` carrier. Mark a shear knot where the
orient bits differ.

The analog row passes when it reproduces the same carrier landing and the same
shear-knot positions. It does not become a plasma experiment.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- integer carrier closure,
- octonion period closure,
- carrier residue,
- shear analog,
- ledger pinch reclassification,
- invalid physical Z-pinch promotion,
- invalid friction/generation promotion.

The answer key separates carrier proof from candidate physical reading.
