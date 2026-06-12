# Paper 2.25 - Toolkit for the Correction Surface

## Purpose

Paper 2.25 describes the tools for reviewing Paper 2. These tools expose the
same finite correction theorem by script, table, or hand reconstruction. They
do not add claims beyond Paper 2.

## Review Objects

The toolkit uses five objects:

```text
LCR state       = (L,C,R)
Rule30 update   = L xor (C or R)
Rule90 update   = L xor R
correction      = C and not R
D4 projection   = axis/sheet label for the state
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-02/verify_correction_surface.py
production/formal-papers/CQE-paper-02/correction_surface_receipt.json
```

The verifier enumerates `{0,1}^3`, computes Rule 30, Rule 90, and the
correction term, then checks that:

```text
Rule30 = Rule90 xor correction
correction fires only on (0,1,0) and (1,1,0)
the firing D4 coordinates are (2,0) and (3,1)
nonzero residue is marked as obligation, not proof
```

## Analog Toolkit

A physical reconstruction requires only:

- three marked positions,
- binary tokens or marks,
- one table row for Rule 30,
- one table row for Rule 90,
- one residue mark,
- one receipt line.

Procedure:

```text
draw L | C | R
place binary values
compute Rule30 = L xor (C or R)
compute Rule90 = L xor R
compute corr = C and not R
check Rule30 = Rule90 xor corr
if corr = 1, write an obligation row
```

The analog route should produce exactly two residue rows:

```text
(0,1,0)
(1,1,0)
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
Which two binary LCR states make C and not R fire?
Does a nonzero correction close the failed route as proof?
What D4 coordinates are exported by the correction states?
```

Expected answers:

```text
(0,1,0) and (1,1,0)
no
(2,0) and (3,1)
```

## Boundary

Paper 2.25 is a toolkit supplement. If tool use uncovers a new correction,
projection, or route, it must be promoted through Paper 2.50's validation
contract before it can change the scientific paper.
