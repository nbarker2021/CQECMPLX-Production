# Paper 17.25 - Error-Correction Tower Toolkit

## Purpose

This supplement gives the reviewer the practical instruments for Paper 17. It
does not carry the proof. It exposes the verified tower so the proof can be
replayed digitally or by hand.

## Digital Route

Run the promoted verifier:

```text
python production/formal-papers/CQE-paper-17/verify_error_correction_tower.py
```

The minimum accepted receipt must include:

```text
chain status
parameter chain
Hamming 7 Fano receipt
extended Hamming 8 receipt
Golay 24 ingredient receipt
powered 72/Nebe bound receipt
Niemeier E8^3 root-shell landing receipt
explicit open Leech and W(E8) fields
```

## Analog Route

Use a code-card stack:

```text
1-card local bit
3-card S3 neighborhood
7-card Fano plane
8-card extended Hamming/E8 seed
24-card 3x8 Golay ingredient carrier
72-card Nebe sheet-bound panel
```

At each rung, mark the local center, the allowed closure frame, the minimum
distance or closure condition, and any residue that must pass forward as an
open obligation.

## Hidden-Guess Diagnostic

The reviewer first classifies an unknown row as:

```text
verified rung
ingredient only
root-shell profile only
open promotion
invalid claim
```

Only after that choice is made may the verifier reveal the receipt. This keeps
the diagnostic useful as training data without letting the answer leak into
the classification.

## Boundary

This toolkit may demonstrate the tower. It may not promote Golay ingredients
into a Leech construction, and it may not promote an E8 seed into a completed
`W(E8)` extraction table.

## Conclusion

Paper 17.25 makes the error-correction tower easy to inspect. It remains a
support layer for the formal claims in Paper 17.
