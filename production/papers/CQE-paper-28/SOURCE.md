# Paper 28 - N-Dimensional Game Lattices

## Status

Applied / constructive paper. It extends the board-game local-rule reading of Paper 24 (KnightForge) into arbitrary-dimensional lattices, using proven substrate objects as the chart operators. The local-rule and lattice-dimension content is grounded; the claim that any specific real game is "solved" by these operators is bounded to the demonstrated finite enumeration. Proof-facing in form.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Abstract

A board game is a local update rule on a lattice: a piece reads its neighborhood and writes a move. This is exactly the corpus chart: a center `C`, opposed boundary directions `L` and `R`, and a readout law selecting the next state. This paper builds N-dimensional local-rule games as chart operators over lattices whose dimensions are the *forced* code-tower parameters `1, 3, 7, 8, 24, 72` (`lattice_codes.verify_lattice_code_chain`). The move operator is an elementary cellular-automaton rule (`rule30._rule_emit`), the symmetry layer is the S_3 transposition group on `(L, C, R)` together with the four-frame Z4 attractor structure (`centroid_voa`), and the conjugate attractors are the four Lie-conjugate fixed states `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}` toward which every state anneals in at most three steps. The piece's "legal move set" is the orbit of its chart state under the S_3 / F_4 trace-2 action (`f4_action.S3_PERMUTATIONS`). We demonstrate the construction on a non-toy example - a robot under N-axis movement constraints with forbidden straight carriers - and bound the claim to the finite enumeration the tool can produce. We do not claim a general N-dimensional game-solving theorem; that is logged as obligation.

## Central Thesis

Extend chess/board logic into arbitrary dimensional local-rule games and tool operators.

## Scope Boundary

This paper claims (i) that a local-rule game on a lattice of one of the forced code-tower dimensions is a chart operator, (ii) that the move-orbit structure is the S_3 / trace-2 action verified by `f4_action`, and (iii) that the annealing closure is bounded by three steps (`centroid_voa.verify_hamming_centroid_universality`). It does NOT claim to solve any specific game (chess, Go), nor a general N-dim solvability theorem. The dimensions `1,3,7,8,24,72` are used because they are forced by the code tower, not chosen for a game. Excess interpretation is obligation. Downstream of Paper 24 (KnightForge) and Paper 14/15 (D12 / lattice code chain).

## Definitions

- **C**: the active center of a piece's readout window; the move quantity invariant under the L-R reflection (`centroid_voa.gluon`).
- **L/R**: opposed boundary directions of the piece's neighborhood.
- **Local-rule game**: a tuple `(lattice, neighborhood, move-rule)` where the move-rule reads a neighborhood and emits the next occupancy bit.
- **Move operator**: an elementary CA rule `f: {0,1}^3 -> {0,1}` applied via `rule30._rule_emit(rule_number, L, C, R)`; the canonical operator is Rule 30.
- **Move orbit**: the S_3 orbit of a chart state under the three transpositions `swap_LR, swap_LC, swap_CR`, equivalently the trace-2 idempotent permutation under `f4_action.S3_PERMUTATIONS`.
- **Lattice dimension**: one of the forced code-tower values `1,3,7,8,24,72` (`lattice_codes`), each the unique perfect/extremal/self-dual code dimension at its scale.
- **Conjugate attractor**: one of the four Lie conjugates `{(0,0,0),(0,1,0),(1,0,1),(1,1,1)}` (`centroid_voa.LIE_CONJUGATES`).
- **Forbidden carrier**: a move direction excluded by the rule (e.g. a forbidden straight line), realized as a chart state outside the legal move orbit.
- **Transport row / Receipt / Supplemental workbook sheet / Tool binding**: as in Paper 00.

## Axioms

Axiom 28.1 - Locality: every legal move must be readable through a local `(L, C, R)` neighborhood before lifting to the board frame.

Axiom 28.2 - Receipt Preservation: every move logs its input neighborhood, output occupancy, and any forbidden-carrier residue.

Axiom 28.3 - Boundary Positivity: an illegal or forbidden move is data; it becomes a logged constraint, not a silent deletion.

Axiom 28.4 - Analog Exposure Equivalence: a main-corpus game has a physical workbook analogue (a board, tokens, and a move card).

## Lemmas

Lemma 28.1 - Every game state closes to a conjugate attractor in <= 3 moves. The S_3 transposition annealing reaches a Lie conjugate `(L = R)` in at most three steps for all eight chart states, independent of the move rule. (Basis: `centroid_voa.verify_hamming_centroid_universality`, status pass; bound `3 = C(3,2)`.)

Lemma 28.2 - The legal move set is the trace-2 S_3 orbit. The three `shell = 2` chart states are permuted by the six S_3 elements as the trace-2 idempotents of `J_3(O)`; the chart's L-R reflection is the `(1 3)` permutation. A piece's legal moves are its orbit under this action. (Basis: `f4_action.S3_PERMUTATIONS`, `_trace2_permutation_matrix`; IDENTITY_PAPER T3.)

Lemma 28.3 - The admissible lattice dimensions are forced. The dimensions `1,3,7,8,24,72` are the unique perfect/extremal/self-dual code dimensions at their scales; `8 = |chart states|`, `24 = 3 x 8`, `72 = 8 x 9`. An N-dim game lattice that is not one of these does not inherit the code-tower closure. (Basis: `lattice_codes.verify_lattice_code_chain`, status pass; Paper 15 Section 2.)

## Formalism / Calculus Sketch

A game state is a chart `P = (C, L, R, B, T, O)` on an N-dim lattice. A move:

```text
read neighborhood (L, C, R) of the active piece
emit next occupancy: bit = _rule_emit(rule_number, L, C, R)   (Rule 30 canonical)
legal moves = S_3 orbit of (L, C, R) under {swap_LR, swap_LC, swap_CR}
forbidden carrier = a chart state outside the legal orbit -> logged in O
anneal: every state reaches a Lie conjugate in <= 3 steps
```

Admissible lattice dimension N in `{1, 3, 7, 8, 24, 72}` (code-tower forced). The knight analog (Paper 24): the L-shaped move is the `(+-1, +-2)` neighborhood; in N dimensions the analog is the move orbit under the N-dim lattice automorphism that fixes the center occupancy `C`.

Tool binding:

```text
cqe_engine  (lattice_forge: rule30._rule_emit, centroid_voa S_3 transpositions /
             anneal_to_lie_conjugate, f4_action.S3_PERMUTATIONS, lattice_codes)
```

## Proof Tree

```text
claim (N-dim local-rule game as chart operator)
-> local (L,C,R) neighborhood
-> move operator = elementary CA rule (Rule 30 canonical)
-> legal moves = S_3 / trace-2 orbit          [PROVEN: f4_action, T3]
-> closure in <= 3 anneal steps               [PROVEN: verify_hamming_centroid_universality]
-> admissible dimension forced (1,3,7,8,24,72)[PROVEN: verify_lattice_code_chain]
-> worked example (N-axis robot, forbidden straights)
-> "general N-dim game solver"                [OBLIGATION + falsifier]
-> supplemental workbook analogue (board + move card)
-> receipt
```

## Practical Solved Example

**Domain:** a warehouse robot on an 8-cell lattice (dimension 8 = `|chart states|`, the E8 / extended-Hamming scale) moving under axis constraints with forbidden straight carriers - the exact intent of the original stub, made concrete on the forced dimension 8.

**Procedure:** place the robot at chart state `(1, 0, 1)`; enumerate the legal move orbit under `S3_PERMUTATIONS`; mark the straight carrier (the identity move) as forbidden and log it; apply `anneal_to_lie_conjugate` to confirm the robot reaches a conjugate attractor in <= 3 moves; confirm dimension 8 is code-tower admissible via `verify_extended_hamming_8`; emit a receipt.

**Solved Output:** the example is solved because (a) the legal move orbit reproduces from `S3_PERMUTATIONS` and the workbook board identically, (b) the forbidden straight carrier is logged not silently dropped (Axiom 28.3), and (c) the closure bound of 3 holds with zero exceptions (Lemma 28.1). The robot's reachable set on the 8-cell lattice is exactly the move orbit; the general N-dim solver claim is not solved and remains obligation.

## Tool Binding

- Module: `cqe_engine` re-exporting `lattice_forge.rule30`, `lattice_forge.centroid_voa`, `lattice_forge.f4_action`, `lattice_forge.lattice_codes`.
- Functions: `_rule_emit`, `anneal_to_lie_conjugate`, `verify_hamming_centroid_universality`, `S3_PERMUTATIONS`, `verify_extended_hamming_8`, `verify_lattice_code_chain`.
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: enumerate the move orbit of one chart state, log one forbidden carrier, confirm <= 3-step closure, and confirm the chosen dimension is code-tower admissible; emit one proof row and one obligation row.

## Analog Workbook Sheet

- Start with grey loose substrate; lay an N-cell board (use 8 cells for the worked example).
- Place the piece token at the active center `C`; place `L` and `R` neighborhood tokens.
- Draw the legal move orbit as colored arrows (one color per S_3 transposition).
- Mark the forbidden straight carrier with a black bar (logged, not erased).
- Use string to bind the chosen move route to its conjugate attractor; count the knots (<= 3).
- White follow-up = a move that closes to an attractor; black follow-up = a forbidden or non-admissible-dimension move.
- Bind into the matching color notebook.

## IRL Citation Anchors

- [Knight] Knight movement in chess: L-shaped move and color alternation. URL: https://en.wikipedia.org/wiki/Knight_(chess) Use: the `(+-1, +-2)` neighborhood and color parity, generalized to N dimensions.
- [QueensInExile] Chaffin, Sloane, et al. Queens in exile: non-attacking queens on infinite boards. URL: https://arxiv.org/abs/1907.09120 Use: greedy chess-piece placement on numbered infinite boards.
- [ConwayLife] Conway's Game of Life. URL: https://conwaylife.com/wiki/Conway%27s_Game_of_Life Use: 2D local-rule game with emergent structure.
- [ConwaySloane1999] J. H. Conway, N. J. A. Sloane, Sphere Packings, Lattices and Groups (3rd ed.), Springer. Use: the lattice dimensions `8, 24` (E8, Leech) as game boards.

## Open Obligations

- The general "N-dimensional game solver" is not proven; only the finite move-orbit / closure structure is. Falsifier: a local-rule game on an admissible dimension whose state fails to anneal to a Lie conjugate in <= 3 steps (would break `verify_hamming_centroid_universality`).
- Games on non-admissible dimensions (not in `1,3,7,8,24,72`) are out of scope; their closure is unverified. Falsifier: a demonstrated closure on a non-code-tower dimension that the tool cannot reproduce.
- The mapping from a real game's piece geometry to the trace-2 orbit is asserted by analogy for the knight (Paper 24); other pieces are obligations.
- Replace citation anchors with final bibliography entries.

## Back-Propagation Targets

- Paper 00 receives the term "local-rule game" and "move orbit".
- Paper 24 (KnightForge) receives the N-dim generalization of the knight neighborhood.
- Paper 14/15 receive the use of the forced code-tower dimensions as game boards.
- The analog workbook manual receives the N-cell board + move-card sheet.
- Paper 31 records how the move-read-then-anneal loop is itself an enacted `(L, C, R)` process.
