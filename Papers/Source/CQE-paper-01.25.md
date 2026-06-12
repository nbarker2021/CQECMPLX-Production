# Paper 1.25 - Toolkit for the LCR Carrier

## Purpose

Paper 1.25 describes the tools available for reviewing Paper 1. The tools are
support systems. They do not replace the Paper 1 proof.

## Review Objects

The Paper 1 toolkit works with four objects:

```text
LCR state      = (L,C,R)
center map     = pi_C(L,C,R) = C
reversal map   = rho(L,C,R) = (R,C,L)
shell grade    = L + C + R
```

The reader can verify every Paper 1 result by hand, by script, or by receipt.

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json
```

The verifier enumerates `{0,1}^3`, checks reversal, counts shell grades, and
rejects the false claim that all opposed boundary positions must contain
unequal values.

## Analog Toolkit

A physical reconstruction requires only:

- three marked positions,
- two token colors or binary marks,
- a way to flip left and right,
- a receipt line.

Procedure:

```text
draw L | C | R
place binary values
record shell = L + C + R
swap L and R
check that C did not move
mark fixed state or reversal pair
test (1,0,1) against any value-inequality claim
```

The analog route exists to expose the same finite proof without requiring the
software stack.

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
How many binary LCR states are there?
Does rho preserve C?
How many states are fixed by rho?
Which shell-2 state falsifies boundary-value inequality?
```

Expected answers:

```text
8
yes
4
(1,0,1)
```

## Boundary

Paper 1.25 is a toolkit supplement. It does not add claims to Paper 1. Any new
claim found during tool use must be promoted through Paper 1.50's claim
contract before it can enter the scientific sequence.
