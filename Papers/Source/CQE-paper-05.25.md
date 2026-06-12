# Paper 5.25 - Toolkit for the Oloid Path Carrier

## Purpose

Paper 5.25 describes the review tools for the rolling path carrier. These
tools expose the finite path theorem and payload behavior; they do not add
prediction claims.

## Review Objects

The toolkit works with:

```text
rolling state       = (sheet, phase, parity)
input bit           = b in {0,1}
rolling step        = roll(q,b)
head/tail dyad      = (sheet, (phase mod 2) xor sheet xor parity)
payload             = Paper 4 repair constraint
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-05/verify_oloid_path_carrier.py
production/formal-papers/CQE-paper-05/oloid_path_carrier_receipt.json
```

Additional package evidence named by the dyad review:

```text
D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_rolling.py
D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_octonionic.py
D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_dual_path.py
D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\quad_oloid.py
D:\CQE_CMPLX\CMPLX-R30-main\FORMALIZATION\CAYLEY_DICKSON_OLOID_NORMAL_FORM.md
```

The promoted verifier is the authority for Paper 5's closed claim.

## Analog Toolkit

A physical reconstruction requires:

- two sheet labels,
- four phase labels,
- two parity labels,
- binary input tokens,
- payload cards for Paper 4 constraints.

Procedure:

```text
start at (0,0,0)
read one binary input bit
flip sheet
advance phase by one modulo four
xor parity with the input bit
record head/tail
attach any Paper 4 payload without changing the next step
reject skipped phases, skipped sheet flips, and nonbinary inputs
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What changes on every legal rolling step?
Can a payload alter the path rule?
What rejects a discontinuous path?
Does this receipt prove Rule 30 prediction?
```

Expected answers:

```text
sheet flips, phase advances, parity XORs the bit
no
skipped legal successor or invalid input
no
```

## Boundary

Paper 5.25 is a toolkit supplement. If a stronger Oloid geometry or prediction
claim is found, it must pass Paper 5.50's claim contract before it can alter
the scientific paper.
