# Paper 01 - LCR Chain Carrier

## Abstract

This paper formalizes the first active carrier used by the CQECMPLX paper
suite after the Paper 00 information contract. The carrier is the ordered
triple `(L, C, R)`: a left boundary, a center, and a right boundary. The
claim is deliberately modest but load-bearing. A system that must preserve a
distinguished center while recording two addressable boundary directions needs
at least three ordered slots. The LCR carrier is therefore the minimal chain
carrier for this class of local readout.

The paper separates three ideas that were previously blended together:
directional opposition, value inequality, and transport. Directional opposition
means that `L` and `R` are different addresses relative to `C`; it does not
mean that the two boundary values are always unequal. In particular, the
trace-2 state `(1, 0, 1)` has equal boundary values while still having two
opposed boundary positions. This correction is essential for a rigorous
presentation.

## Role in the Suite

Paper 00 is the inherited minimum information contract. Paper 01 is the first
active paper in the future-facing sequence. Its job is not to prove the entire
CQECMPLX corpus. Its job is to define the smallest local object that later
papers can transport, repair, curve, lift, observe, and deploy.

The four active paper windows therefore begin here:

```text
Paper 00: inherited contract outside the active windows
Window 1: Papers 01-08
Window 2: Papers 09-16
Window 3: Papers 17-24
Window 4: Papers 25-32
Active wrap: Paper 32 -> Paper 01
```

## Definitions

Let `A` be a finite alphabet. For the binary examples in this corpus,
`A = {0, 1}`.

An **LCR state** over `A` is an ordered triple

```text
s = (L, C, R) in A^3
```

where `C` is the distinguished center, `L` is the left boundary read relative
to `C`, and `R` is the right boundary read relative to `C`.

The **center projection** is

```text
pi_C(L, C, R) = C.
```

The **left-right reversal** is

```text
rho(L, C, R) = (R, C, L).
```

The **binary shell** or **trace grade** is

```text
shell(L, C, R) = L + C + R.
```

For binary states, this partitions the eight states into grades of
multiplicity `1, 3, 3, 1`.

Directional opposition is structural:

```text
address(L) != address(R)
```

Value inequality is state-dependent:

```text
value(L) != value(R)
```

The LCR carrier requires directional opposition. It does not require value
inequality in every state.

## Main Claim

**Theorem 1.1, Minimal LCR Carrier.** Any ordered local carrier that preserves
a distinguished center and records two addressable boundary directions requires
at least three slots. The carrier `(L, C, R)` realizes this lower bound, and is
therefore minimal.

### Proof

A carrier that preserves a distinguished center must contain at least one
address for the center. A carrier that records two boundary directions relative
to that center must contain one address for the left boundary and one address
for the right boundary. These three roles are pairwise distinct as addresses:
if the center address is identified with a boundary address, the center is no
longer distinguished; if the two boundary addresses are identified, the carrier
cannot distinguish left from right. Hence at least three addresses are required.

The ordered triple `(L, C, R)` has exactly these three addresses and no
additional address. It preserves the center through `pi_C`, records both
boundary directions, and supports reversal by `rho`. Thus it attains the lower
bound. QED.

## Finite Binary Inventory

For the binary corpus case, the state space is `{0,1}^3`, so there are exactly
eight states:

```text
(0,0,0) shell 0
(0,0,1) shell 1
(0,1,0) shell 1
(0,1,1) shell 2
(1,0,0) shell 1
(1,0,1) shell 2
(1,1,0) shell 2
(1,1,1) shell 3
```

The reversal `rho` preserves the center:

```text
pi_C(rho(L, C, R)) = pi_C(R, C, L) = C = pi_C(L, C, R).
```

It is also an involution:

```text
rho(rho(L, C, R)) = (L, C, R).
```

The fixed states under reversal are exactly the states with `L = R`:

```text
(0,0,0), (0,1,0), (1,0,1), (1,1,1).
```

The non-fixed states form two reversal pairs:

```text
(0,0,1) <-> (1,0,0)
(0,1,1) <-> (1,1,0)
```

This is the first useful correction surface for Paper 01. The state
`(1,0,1)` is fixed under reversal and has shell 2. Therefore the statement
"all shell-2 states have unequal boundary values" is false. The correct
statement is that all states have two addressable boundary directions, and
some states assign equal values to those two directions.

## Relation to Rule 30 Readout

Rule 30 uses the same local window form. Its Boolean update rule can be written
as

```text
f(L, C, R) = L xor (C or R).
```

Paper 01 does not claim to solve Rule 30. It establishes the carrier on which
later Rule 30 and Jordan-algebra arguments can be expressed. In this role, LCR
is the local chart: every update reads a center and two relative boundaries.
The shell grading supplies a compact inventory of the eight local states; the
reversal supplies the left-right symmetry operation that later papers compare
with Weyl or Jordan diagonal permutations.

## Relation to the Diagonal Jordan Carrier

The binary LCR state can be embedded into the diagonal subalgebra of the
exceptional Jordan algebra by

```text
phi(L, C, R) = diag(L, C, R).
```

At the level used in this paper, only the diagonal bookkeeping is required.
The map preserves the eight binary states, the shell/trace value, and the
left-right reversal as a swap of the first and third diagonal positions.

Paper 01 does not need the full off-diagonal octonionic structure. That
structure becomes relevant later when the corpus asks which additional
theorems can be transported through a verified structure-preserving map.

## Hand Reconstruction

The hand method is intentionally simple:

1. Draw three ordered cells labeled `L`, `C`, and `R`.
2. Place the center token in `C`.
3. Choose or roll binary values for all three cells.
4. Record the shell as the number of occupied cells.
5. Reverse the sheet by swapping the left and right positions.
6. Confirm that the center value did not move.
7. Mark whether the state is reversal-fixed or part of a reversal pair.
8. If a diagnostic claims `L != R`, test it against `(1,0,1)` before accepting
   it.

This hand method is the analog twin of the finite verifier. It is not a
metaphor for the verifier; it is the same finite enumeration performed with
physical tokens.

## Code Reconstruction

The paper requires a verifier that checks:

```text
1. There are exactly eight binary LCR states.
2. The center projection is preserved under reversal.
3. Reversal is an involution.
4. The shell multiplicities are 1, 3, 3, 1.
5. The fixed and paired reversal orbits are exactly identified.
6. The false value-inequality claim is rejected by the counterexample (1,0,1).
7. The minimality proof is recorded as an address-count argument.
```

The production verifier for this polish pass is:

```text
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
```

It emits a JSON receipt that can be used by the paper-kernel suite.

## Validation and Hidden-Guess Layer

For non-math diagnostics, the training-mode honesty layer should ask for a
prediction before revealing the formal answer. For Paper 01, the useful hidden
guess prompts are:

```text
Does reversal preserve C for every binary LCR state?
How many reversal-fixed binary states are there?
Is every shell-2 state a state with L != R?
What counterexample tests the boundary-value mistake?
```

The answer to the third prompt must be "no"; `(1,0,1)` is the counterexample.
This makes Paper 01 a useful first diagnostic because it teaches the system not
to confuse structural direction with observed value.

## Open Obligations

1. Connect this finite verifier to the installable `cqe_engine.formal`
   interface rather than leaving it as a standalone production verifier.
2. Update older workbook language that equates opposed directions with
   unequal boundary values.
3. Carry the corrected distinction into Paper 03, where left-right reversal is
   compared with diagonal permutation and triality language.
4. Add a peer-review bibliography pass for Rule 30, elementary cellular
   automata, transport of structure, and Jordan-algebra background.

## Conclusion

Paper 01 establishes the smallest local carrier used by the active CQECMPLX
suite. Its proof is finite and elementary, but not optional: without the
ordered three-address carrier, later papers have no disciplined way to say
what a center is, what its two boundaries are, what reversal preserves, or
which failures are real correction data. The corrected formal statement is
therefore:

```text
LCR is the minimal ordered carrier preserving one center and two addressable
boundary directions. Directional opposition is structural; boundary-value
inequality is not guaranteed.
```
