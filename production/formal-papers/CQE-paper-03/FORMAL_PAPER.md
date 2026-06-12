# Paper 03 - D4/J3 Triality Surface

## Abstract

Paper 03 introduces the first explicit multi-representation surface in the
active CQECMPLX suite. Paper 01 supplied the LCR carrier. Paper 02 supplied
typed correction residue. Paper 03 shows how the same eight local states can be
read through two additional, structure-preserving representations:

```text
LCR state <-> D4-style axis/sheet code <-> diagonal J3 carrier
```

The polished claim is intentionally narrower than the old title may suggest.
This paper does not prove the full triality automorphism theorem for D4, nor
does it use the full exceptional Jordan algebra. It proves the local triality
surface needed by this corpus: a lossless axis/sheet encoding of the eight LCR
states, together with a diagonal carrier whose trace equals the LCR shell and
whose trace-2 states are idempotent under coordinate-wise diagonal product.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

## Role in the Suite

Paper 03 is the first bridge paper. It lets later work move between three
readout languages without changing the local state:

```text
1. LCR language: local center and two boundaries.
2. Axis/sheet language: four antipodal pairs, two sheets each.
3. Diagonal J3 language: diag(L,C,R), trace, and trace-2 idempotents.
```

This is the correct entry point for triality language because it separates the
verified finite surface from later, stronger group-theoretic obligations.

## Definitions

Let the LCR state space be

```text
S = {0,1}^3.
```

Define the axis map:

```text
axis(0,0,0) = 0    axis(1,1,1) = 0
axis(1,0,0) = 1    axis(0,1,1) = 1
axis(0,1,0) = 2    axis(1,0,1) = 2
axis(0,0,1) = 3    axis(1,1,0) = 3
```

Define the sheet map:

```text
sheet(L,C,R) = 0 if L+C+R <= 1
sheet(L,C,R) = 1 if L+C+R >= 2.
```

Define the diagonal carrier:

```text
phi(L,C,R) = diag(L,C,R).
```

On diagonal carriers, use coordinate-wise multiplication as the diagonal
Jordan product:

```text
diag(a,b,c) o diag(a,b,c) = diag(a*a, b*b, c*c).
```

For binary diagonal entries, every coordinate is idempotent. The trace-2
claim is singled out because it is the stratum later used as the three-element
color/orbital surface.

## Main Claim

**Theorem 3.1, Local Triality Surface.** The map

```text
tau(L,C,R) = (axis(L,C,R), sheet(L,C,R), diag(L,C,R))
```

is a faithful three-language presentation of the eight binary LCR states. The
axis/sheet part is a bijection from `S` to `{0,1,2,3} x {0,1}`. The diagonal
part preserves shell as trace. The shell-2 states map to trace-2 diagonal
idempotents.

### Proof

The axis map partitions the eight states into four disjoint antipodal pairs:

```text
axis 0: (0,0,0), (1,1,1)
axis 1: (1,0,0), (0,1,1)
axis 2: (0,1,0), (1,0,1)
axis 3: (0,0,1), (1,1,0)
```

Within every axis pair, one state has shell at most 1 and one state has shell
at least 2. Therefore the sheet bit distinguishes the two states inside each
axis. Thus `(axis, sheet)` uniquely identifies one of the eight LCR states and
is a bijection.

For the diagonal carrier,

```text
trace(phi(L,C,R)) = L + C + R = shell(L,C,R).
```

If shell is 2, then `phi(L,C,R)` has exactly two diagonal `1` entries and one
diagonal `0` entry. Coordinate-wise multiplication gives

```text
phi o phi = phi,
```

so every shell-2 state maps to a trace-2 diagonal idempotent. QED.

## Relation to Papers 01 and 02

Paper 01 corrected the distinction between boundary address and boundary
value. Paper 03 keeps that correction: axis/sheet labels classify complete
states; they are not merely labels for unequal boundary values.

Paper 02 identified the correction firing states:

```text
(0,1,0) and (1,1,0).
```

Under the Paper 03 axis/sheet map, these become:

```text
(0,1,0) -> (axis 2, sheet 0)
(1,1,0) -> (axis 3, sheet 1)
```

This is why the correction surface can feed Paper 03: residue rows now have a
second coordinate language.

## What This Paper Does Not Yet Prove

The phrase "triality" has strong mathematical meanings. This paper proves a
local triality surface only. It does not, by itself, prove:

```text
1. The full D4 triality automorphism theorem.
2. A full F4 action on J3(O).
3. Exact S3 group-ring closure of the Rule 30 trace-2 transition matrix.
4. Any claim depending on off-diagonal octonionic entries.
```

Those claims require additional verifiers and are routed as obligations to
later formal passes. This paper supplies the coordinate surface they need.

## Hand Reconstruction

1. Draw the eight LCR states.
2. Pair each state with its bitwise complement.
3. Assign the four pairs to axes 0 through 3.
4. Mark sheet 0 for shell 0 or 1; mark sheet 1 for shell 2 or 3.
5. Confirm that every `(axis, sheet)` coordinate names exactly one LCR state.
6. Draw the diagonal `diag(L,C,R)`.
7. Confirm that trace equals shell.
8. For shell-2 states, multiply the diagonal by itself and confirm it is
   unchanged.

## Code Reconstruction

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-03/verify_triality_surface.py
```

It verifies:

```text
1. Axis/sheet encoding is bijective.
2. Axis pairs are antipodal complements.
3. The correction rows from Paper 02 land at (2,0) and (3,1).
4. Diagonal trace equals shell for all states.
5. Shell-2 diagonal carriers are idempotent.
6. Strong triality claims remain explicitly unproved obligations.
```

## Validation and Hidden-Guess Layer

The hidden-guess prompts for this paper are:

```text
Given an LCR state, what axis/sheet coordinate does it receive?
Which two axis/sheet coordinates carry the Paper 02 correction firing states?
Does this local surface prove full D4 triality?
Which states are trace-2 diagonal idempotents?
```

The third answer must be "no." That negative answer is part of the honesty
layer: the system must learn to stop at the verified surface.

## Open Obligations

1. Wire `verify_triality_surface` into the installable `cqe_engine.formal`
   interface.
2. Add the stronger S3 group-ring/J3 trace-2 proof as a separate theorem rather
   than hiding it inside this local codec paper.
3. Reconcile the axis naming between all chart-codec copies in the D drive.
4. Carry the exact Paper 02 correction coordinates into the Paper 04 boundary
   repair formalism.

## Conclusion

Paper 03 proves the first local triality surface: one finite state can be read
as LCR, as D4-style axis/sheet, and as a diagonal J3 carrier. This is enough to
support disciplined transport into later papers, while preserving the boundary
between verified finite structure and stronger exceptional-algebra claims that
still require their own proofs.
