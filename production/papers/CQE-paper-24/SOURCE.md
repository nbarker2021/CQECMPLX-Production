# Paper 24 - KnightForge / N-Dimensional Chess Automata

## Status

Applied / horizon layer. Connects a real combinatorial domain (greedy non-attacking piece placement on numbered boards) to the corpus substrate. The contribution is the registration of greedy red/black knight placement as an L-conjugate cellular automaton and its generalization to N-dimensional chart operators. The provable content is about the local-rule CA and its L-conjugate attractors (`centroid_voa.py`); the chessboard is the illustration that gives the CA a concrete shadow.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

A knight placed on a numbered board under a greedy non-attacking rule generates an integer sequence whose pattern (stripes, islands) is determined entirely by a local exclusion neighborhood - the L-shaped `(+-1, +-2)/(+-2, +-1)` move set [Knight], in the same spirit as the greedy queens-in-exile construction [QueensInExile] cataloged in [OEIS]. This is structurally the corpus move: a global pattern fixed by a local `(L, C, R)` window. We register greedy knight placement as a local-rule cellular automaton whose update is read through the chart and whose closure is governed by the L-conjugate (Lie-conjugate) attractor structure proven in `centroid_voa.py`: every chart state anneals to one of the four `L = R` attractors `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}` in at most three S3-transposition steps (`verify_hamming_centroid_universality`). The "L-conjugate" of the thesis is exactly this `L = R` conjugate plane; the "greedy knight" is the local exclusion rule that the chart reads. We then lift the CA to N-dimensional chess operators by treating each board axis as one of the S3 centroid frames (`three_conjugate_label`) and the move set as a chart operator acting on the joint label. No claim is made that an N-dimensional chess game is "solved"; the claim is that greedy placement is an L-conjugate CA whose attractor count and orbit split are the same finite chart identities the corpus already verifies, and that the N-dimensional generalization is a frame-indexed chart operator.

## Central Thesis

Generalize red/black greedy knight placement as an L-conjugate CA and then as N-dimensional chess operators.

## Scope Boundary

This paper claims (i) that greedy red/black knight placement can be written as a local-rule CA whose state closes under the L-conjugate attractor structure of `centroid_voa.py`, (ii) that the red/black coloring is the chart `side = sgn(R - L)` parity, and (iii) that the N-dimensional lift is a frame-indexed chart operator over the S3 centroid settings. It does NOT claim to solve N-dimensional chess, to enumerate any new OEIS sequence as a theorem, or that the greedy sequence is identical to any published one (that comparison is an obligation). The chess domain is the concrete shadow; the result is the CA / attractor structure. Excess interpretation is logged, not promoted.

## Definitions

- **C (active cell)**: the cell whose occupancy is being decided - the center of the local exclusion window, the chart center preserved under `L <-> R`.
- **L / R (opposed approaches)**: the two opposed directions from which a knight move can attack `C`; the chart boundary readouts. Red/black is `side = sgn(R - L)`.
- **Greedy placement rule**: place a piece at the next free numbered cell that attacks no earlier-placed piece; a deterministic local exclusion CA.
- **L-conjugate (Lie-conjugate) attractor**: a chart state with `L = R`; the four such states `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}` are `LIE_CONJUGATES` in `centroid_voa.py`.
- **Anneal step**: one S3 transposition (`swap_LR`, `swap_LC`, `swap_CR`); `anneal_to_lie_conjugate` reaches an attractor in `<= 3` steps.
- **N-dimensional chess operator**: a chart operator indexed by which S3 centroid frame plays the role of "board axis" (`three_conjugate_label` / `four_frame_label`).
- **Transport row / Receipt / Supplemental workbook sheet / Tool binding**: as defined in Paper 00.

## Axioms

Axiom 24.1 - Locality: a placement decision is admissible only if it is readable through a single `(L, C, R)` exclusion window before any board-wide pattern is asserted.

Axiom 24.2 - Receipt Preservation: no CA update is accepted unless its input window, output occupancy, anneal trajectory, and residue can be logged and replayed.

Axiom 24.3 - Boundary Positivity: a blocked cell (a greedy rejection) is data - it becomes an exclusion record, never a silent deletion.

Axiom 24.4 - Analog Exposure Equivalence: the CA has a physical workbook analogue (a numbered token grid with red/black markers and a flip operation).

## Lemmas

Lemma 24.1 - A placement window that preserves its center `C` and records its `L/R` approach parity can be transported into the placement ledger without erasing the rejected (attacked) alternatives, which are kept as exclusion rows. (Basis: greedy exclusion is a local-window predicate; `morphonics` `BOUNDARY_ASYMMETRY` would flag a lost approach.)

Lemma 24.2 - The greedy CA closes: every chart state of the exclusion window anneals to an L-conjugate (`L = R`) attractor in at most three S3-transposition steps, and the four attractors are universal across all 256 elementary rules. (Basis: `verify_hamming_centroid_universality`, `anneal_to_lie_conjugate`.)

Lemma 24.3 - The red/black two-coloring of the board is exactly the chart `side` invariant: `side = +1` (red), `side = -1` (black), `side = 0` (pivot). The knight's color-alternation property [Knight] is the `swap_LR` involution on the `shell = 2` stratum (Paper 01, Lemma 01.3). The eight chart states split as 2 vacua + 6 excited (`verify_voa_sector_decomposition`), which is the candidate orbit structure of the placement classes - offered as a structural correspondence, not a proof that the greedy sequence equals any named OEIS entry.

## Formalism / Calculus Sketch

A placement state is `P = (C, L, R, B, T, O)`. The greedy CA transform `T` reads the exclusion window, decides occupancy, and records the anneal trajectory:

```text
exclusion window (L,C,R)
-> greedy decision B: occupy C iff no L/R approach hits an earlier piece
-> anneal_to_lie_conjugate(state) -> attractor in <= 3 S3 steps
-> red/black label = side = sgn(R - L)
-> N-dim lift: frame-indexed operator three_conjugate_label(state) = (w1,w2,w3)
-> receipt {occupancy, attractor, side, frame label, residue}
```

The L-conjugate closure is the seed partition `Z(q) = 2q^0 + 6q^5` (the docstring VOA reading: 2 vacua at weight 0, 6 excited at weight 5; the code's `verify_voa_sector_decomposition` reports the same 2+6 split). The N-dimensional chess operator assigns each "board axis" to one of the three centroid frames; an N-axis board is a composite of N frame labels. Tool binding:

```text
cqe_engine  (centroid_voa: LIE_CONJUGATES, anneal_to_lie_conjugate, swap_LR,
             TRANSPOSITIONS, three_conjugate_label, voa_weight;
             f4_action: s3_permutation_matrices; rule30: rule30_bit)
```

## Proof Tree

```text
claim (greedy knight placement is an L-conjugate CA; N-dim chess = frame operator)
-> local (L,C,R) exclusion window
-> greedy decision (occupy / reject)
-> red/black = side parity (Lemma 24.3)
-> L-conjugate anneal closure in <= 3 steps (Lemma 24.2)
-> 2+6 vacuum/excited orbit split (verify_voa_sector_decomposition)
-> N-dim lift: three_conjugate_label frame operator
-> worked example (greedy knight stripes/islands)
-> supplemental workbook analogue (numbered token grid + flip)
-> receipt
-> proof (CA + attractors) / obligation (OEIS identity, N-dim playability)
```

## Practical Solved Example

**Domain:** greedy non-attacking knight placement on the numbered (boustrophedon) board, producing the stripe/island pattern of the spiral board game in the original scope note.

**Procedure:** sweep cells in numbered order; at each cell read the exclusion window `(L, C, R)` over the knight-approach parity; apply the greedy decision; label the cell red/black by `side`; run `anneal_to_lie_conjugate` on the window state and record which of the four `LIE_CONJUGATES` it reaches and in how many steps; emit the per-cell receipt. Then form the N-dimensional operator by computing `three_conjugate_label` for each occupied window.

**Solved Output (what is actually established):** the placement reproduces a deterministic red/black stripe/island pattern; every window state anneals to an L-conjugate in `<= 3` steps with the four universal attractors; the occupied-window states distribute over the 2+6 vacuum/excited split. The example is solved in the corpus sense: the attractor set, step counts, and 2+6 split reproduce identically from `verify_hamming_centroid_universality`, `verify_voa_sector_decomposition`, and the workbook token grid. What is NOT established: that the resulting integer sequence equals a specific OEIS entry, or that an N-dimensional chess variant built on these operators is playable or well-posed - both are obligations. The greedy-queens literature [QueensInExile] is the reference for the non-attacking greedy construction; [OEIS] is where any sequence identity must be checked.

## Tool Binding

- Module: `cqe_engine` (`centroid_voa.LIE_CONJUGATES`, `anneal_to_lie_conjugate`, `swap_LR`, `TRANSPOSITIONS`, `three_conjugate_label`, `voa_weight`; `f4_action.s3_permutation_matrices`; `rule30.rule30_bit`).
- Verifiers: `verify_hamming_centroid_universality`, `verify_voa_sector_decomposition`, `verify_centroid_voa_chain`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: run greedy placement over a finite board, emit one receipt showing a window annealing to an L-conjugate in `<= 3` steps, and one obligation row (OEIS-identity check). Smoke test produces at least one proof-like row (attractor closure) and one obligation-like row.

## Analog Workbook Sheet

- Start with grey loose substrate; lay a numbered token grid.
- Place the `C` token at the cell under decision; place `L` and `R` tokens at the two opposed knight approaches.
- Color red when `side = +1`, black when `side = -1`, grey pivot when `side = 0`.
- Use string to bind the anneal route: at most three beads (one per S3 transposition) until the strip reaches an `L = R` (flipped-symmetric) state.
- White follow-up = a window that closed to an L-conjugate; black follow-up = a rejection / exclusion record or an unverified OEIS-identity claim.
- Bind the finished sheet into the matching color notebook.

## IRL Citation Anchors

- [Knight] Knight movement in chess: L-shaped move and color alternation. URL: https://en.wikipedia.org/wiki/Knight_(chess) Use: knight neighborhood `(+-1, +-2)/(+-2, +-1)` and color-parity analog (the `side` invariant).
- [QueensInExile] Chaffin, Sloane, et al. Queens in exile: non-attacking queens on infinite boards. URL: https://arxiv.org/abs/1907.09120 Use: greedy chess-piece placement on numbered infinite boards.
- [OEIS] OEIS Foundation / On-Line Encyclopedia of Integer Sequences. URL: https://oeis.org/ Use: integer-sequence repository where any greedy-sequence identity must be checked.

## Open Obligations

- **OEIS-identity obligation (with falsifier).** Compute the greedy-knight sequence to depth N and search [OEIS]. Falsifier: if the sequence matches no known greedy non-attacking entry and the CA-derived recurrence fails to reproduce it, the "L-conjugate CA generates a named sequence" reading is downgraded to `SPEC`.
- **N-dimensional playability obligation.** The frame-indexed operator is defined; that it yields a well-posed, terminating N-dimensional chess variant is unproven - carry as `MODEL`.
- The 2+6 orbit-to-placement-class correspondence (Lemma 24.3) is a structural candidate; validate by checking that placement classes match the Z3 frame orbit, else log `INVARIANT_NOT_PRESERVED`.
- Add one domain-expert (combinatorial game theory) critique pass.
- Replace citation anchors with final bibliography entries during peer-review preparation.

## Back-Propagation Targets

- Paper 00 receives the "L-conjugate CA closure" term if not already present.
- Paper 01 receives the red/black = `side` parity / `swap_LR`-on-`shell=2` correspondence.
- Paper 21 (MorphForge) receives the local-rule-as-ribbon reading specialized to greedy exclusion.
- The lattice_forge registry records the greedy-CA surface over `centroid_voa`.
- The analog workbook manual receives the numbered-token-grid sheet rule.
- Paper 31 records how this paper's presentation order (window -> greedy decision -> anneal -> frame lift) enacts the same `(L, C, R)` process.
