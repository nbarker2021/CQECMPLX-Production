# Paper 01 - LCR Chain Carrier

## Status

Foundational paper. Establishes the `(L, C, R)` chain as the smallest carrier that preserves a center while admitting two opposed boundary directions, and proves the single-tape bijective doublet. Proof-facing.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

We establish the Left-Center-Right readout window as the minimal chain carrier of the corpus: the smallest local object that preserves a center `C` while admitting two opposed boundary directions `L` and `R`. We prove that the three `shell = 2` chart states `(1,1,0)`, `(1,0,1)`, `(0,1,1)` carry the complete SU(2) spin-1/2 doublet within a single forward tape, via the side-flip bijection `(1,1,0) <-> (0,1,1)` fixing `(1,0,1)`. The negative-chirality state is structurally present in the forward tape; no antipodal counter-sheet, second tape, or inverted-frame construction is required. This obviates the cross-page `-N` mechanism of earlier framework drafts and explains why the `shell = 2` transition matrix carries the full doublet as a single object. The construction is verified at machine precision against Rule 30's canonical center column.

## Central Thesis

Formalize Left-Center-Right readout as the smallest chain carrier that preserves a center while allowing two opposed boundary directions, and show that its `shell = 2` stratum already encodes the complete SU(2) doublet on one tape.

## Scope Boundary

This paper claims the minimality of the `(L, C, R)` carrier and the single-tape bijective doublet, both reproducible by the executable verifier. It does not claim the wider universality results (those are Paper 07) nor the `J_3(O)` isomorphism in full (that is Paper 03); it uses only the diagonal registration needed for the doublet. Excess interpretation is logged as obligation.

## Definitions

- **Chain carrier**: a local window that carries a center plus its immediate boundary context; the `(L, C, R)` triple is the minimal such carrier over a binary tape.
- **Chart state**: `(L, C, R)` in `{0,1}^3`; 8 states total.
- **Shell**: `L + C + R`. The `shell = 2` stratum has exactly three states.
- **Side / chirality**: `sgn(R - L)`; `+` when `R > L`, `-` when `L > R`, `0` when equal.
- **Side-flip bijection** `b`: the involution `(1,1,0) <-> (0,1,1)`, fixing `(1,0,1)` — the chart's `L <-> R` reflection restricted to `shell = 2`.
- **SU(2) doublet**: the two-state spin-1/2 system `(|up>, |down>)` with its null pivot.

## Axioms

Axiom 01.1 - Locality: a carrier is admissible only if its readout depends solely on its own `(L, C, R)` content.

Axiom 01.2 - Receipt Preservation: every carrier transition logs its input state, output state, and residue.

Axiom 01.3 - Boundary Positivity: a chirality flip is information (a spin direction), not an error.

Axiom 01.4 - Analog Exposure Equivalence: the doublet has a physical workbook analogue (a three-token strip with a flip operation).

## Lemmas

Lemma 01.1 - Minimality: no carrier smaller than three cells can simultaneously hold a center and two distinguishable opposed boundaries. A two-cell window has no fixed center; a one-cell window has no boundary. Hence `(L, C, R)` is minimal.

Lemma 01.2 - Readout equivalence: the readout law `bit(L,C,R) = 1 iff shell=1 or (shell=2 and R>L)` equals Rule 30 `L XOR (C OR R)`, by enumeration of all 8 states.

Lemma 01.3 - The side-flip `b` is an involution on `shell = 2` with exactly one fixed point `(1,0,1)`; it realizes the `L <-> R` Weyl reflection on that stratum.

## Formalism / Calculus Sketch

The 8 chart states, their Rule 30 output, shell, and side:

```text
(L,C,R)  Rule30  shell  side   readout
(0,0,0)    0       0      0       0
(0,0,1)    1       1      +       1
(0,1,0)    1       1      0       1
(0,1,1)    1       2      +       1
(1,0,0)    1       1      -       1
(1,0,1)    0       2      0       0
(1,1,0)    0       2      -       0
(1,1,1)    0       3      0       0
```

The `shell = 2` stratum carries the doublet:

```text
(1,1,0)  side -   = +spin   (J_3(O) idempotent E_11 + E_22)
(1,0,1)  side 0   = null    (E_11 + E_33, the b-fixed pivot)
(0,1,1)  side +   = -spin   (E_22 + E_33, the b-image of +spin)
```

`b` carries `+spin <-> -spin` within the forward tape. The `2pi`/`4pi` double-cover behavior of SU(2) is realized by the order of `b` composed with the chart step, with no second tape. Tool binding:

```text
cqe_engine  (centroid_voa: gluon, swap_LR, TRANSPOSITIONS; the shell=2 stratum)
```

## Proof Tree

```text
claim (LCR is the minimal carrier; shell=2 = single-tape SU(2) doublet)
-> minimality argument (Lemma 01.1)
-> readout = Rule 30 (Lemma 01.2)
-> shell=2 three-state stratum
-> side-flip involution b (Lemma 01.3)
-> doublet assignment (+spin / null / -spin)
-> worked example (Rule 30 center column)
-> supplemental workbook analogue (three-token flip strip)
-> receipt
```

## Practical Solved Example

**Domain:** the `shell = 2` substream of Rule 30's center-column chart.

**Procedure:** extract all `shell = 2` chart states along the center column; apply `b` to each; confirm `b` permutes `+spin` and `-spin` and fixes `null`; confirm the three states are exactly the three trace-2 idempotents under `phi`.

**Solved Output:** the three `shell = 2` states close under `b` as a single-tape doublet; the construction matches the `J_3(O)` trace-2 idempotents with zero deviation (`IDENTITY_PAPER` Theorem T_BIJECTIVE; Paper 01 of the PROOF set). The example is solved when the doublet assignment reproduces identically from the formal table, the `cqe_engine` stratum routine, and the workbook flip strip.

## Tool Binding

- Module: `cqe_engine` (`centroid_voa`: `gluon`, `swap_LR`, `TRANSPOSITIONS`, the `shell = 2` stratum).
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: enumerate the three `shell = 2` states, apply `b`, confirm one fixed point and one transposed pair; confirm each maps to a distinct trace-2 idempotent.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a three-cell strip `L | C | R`.
- Place tokens for a `shell = 2` state (two set, one clear).
- The flip operation `b` swaps the `L` and `R` tokens — physically turning the strip over.
- White follow-up = a closed doublet pair; black follow-up = any state that fails to return under `b`.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Wolfram1983] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55(3), 601-644. Use: Rule 30 readout.
- [JordanVonNeumannWigner1934] Jordan, von Neumann, Wigner, On an algebraic generalization of the quantum mechanical formalism, Ann. of Math. 35, 29-64. Use: trace-2 idempotents of `J_3(O)`.
- [Baez2002] J. Baez, The Octonions, Bull. AMS 39(2), 145-205. Use: octonionic / SU(2) structure background.

## Open Obligations

- The full SU(2) double-cover phase accounting (the exact `2pi` sign and `4pi` return as a composition order) is stated structurally; a formal order computation is an obligation.
- Replace citation anchors with final bibliography entries.
- Add a falsifier: a `shell = 2` labeling that breaks closure under `b`, which the tool must reject.

## Back-Propagation Targets

- Paper 00 receives the carrier-minimality term.
- Paper 03 receives the `shell = 2` -> trace-2 idempotent correspondence used by the full isomorphism.
- The analog workbook manual receives the three-token flip-strip rule.
- Paper 31 records how the doublet's single-tape construction recurs in the corpus presentation order.
