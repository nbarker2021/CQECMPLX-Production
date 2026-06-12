# Paper 13.25 - Toolkit for Quark-Face Transport

## Purpose

This support paper exposes the tools for Paper 13. It is not the proof-carrying
paper. The proof is the finite algebraic closure in Paper 13; this toolkit shows
how to inspect the same closure digitally and by ordinary visible marks.

## Digital Toolkit

Run:

```text
python production/formal-papers/CQE-paper-13/verify_quark_face_transport.py
```

The verifier checks:

```text
shell-2 chart state count
trace-2 J_3(O) idempotent receipt
S3 closure over the trace-2 triple
exact n=3 SU(3) group-ring closure
bounded G2/F4/T5A classifier honesty boundary
six-face color/anticolor analog consistency
```

The receipt is:

```text
production/formal-papers/CQE-paper-13/quark_face_transport_receipt.json
```

## Minimal Analog Surface

Use three tokens labelled:

```text
C-  C0  C+
```

Write the associated chart states:

```text
C- = 110
C0 = 101
C+ = 011
```

Write the associated idempotents:

```text
C- = E11 + E22
C0 = E11 + E33
C+ = E22 + E33
```

Now apply each of the six permutations of `(1,2,3)` to the idempotent labels.
Every result must return to one of the three labels. That is the analog check
for S3 closure.

## Six-Face Exposure

The optional color/anticolor exposure layer uses:

```text
R, G, B, anti-R, anti-G, anti-B
```

with:

```text
R -> G -> B -> R
anti-R -> R
anti-G -> G
anti-B -> B
```

This is a workbook visualization of color-face transport. It is not the
physical Standard Model proof.

## Hidden-Guess Diagnostic

Before revealing the receipt, ask the reviewer or model to choose:

```text
Does S3 close on the trace-2 triple?
Does exact n=3 closure have zero residual?
Does the bounded route derive the bit from depth alone?
Does the color/anticolor model prove physical quark color?
```

Only after the guess is recorded reveal the receipt:

```text
yes
yes
no
no
```

The diagnostic trains the boundary that matters most in this paper: algebraic
closure is closed; physical derivation is not silently promoted.

## Boundary

This toolkit may reproduce the Paper 13 algebraic transport receipt. It may not
convert the color analogy into a physical derivation without a separate claim
contract and calibrated evidence.
