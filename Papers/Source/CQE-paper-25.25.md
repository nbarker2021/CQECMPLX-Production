# Paper 25.25 - Energetic Traversal Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 25's traversal receipt. The proof
is in Paper 25 and its formal verifier; this file holds the tool route and the
analog route.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-25/verify_energetic_traversal.py`

The expected status is `pass_with_open_obligations`. The verifier checks
`NSLTerm` arithmetic, the four-row transport-obligation spine, the `2 + 6` VOA
default analog cost, additive path totals, one closed normalized traversal, and
one open uncalibrated traversal.

## Analog Route

Draw each transport as a row with source, target, and `(L, C, R)`. Write the
four NSL fields beside it: conservation residue, information residue,
irreversible cost, and absorption. Add the first three values, subtract
absorption, and mark the row closed only when the result is less than or equal
to zero.

To expose the path, thread the rows in order. The path total is the sum of the
row totals. A negative or zero path may close only when no row is marked
uncalibrated. Any positive row or uncalibrated row is carried forward as an
obligation.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- closing NSL step,
- non-closing NSL step,
- closing normalized traversal,
- open traversal,
- uncalibrated physical-energy promotion,
- invalid least-action promotion,
- valid obligation carry.

The answer key distinguishes analog accounting closure from physical-energy
closure.
