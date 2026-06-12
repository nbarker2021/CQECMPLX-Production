# Paper 28 — C-Form: N-Dimensional Game Lattices Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the game lattice Gluon** — the N-dimensional board Gluon that generalizes the chess automata Gluon (Paper 24) to arbitrary dimensional local-rule games. In the lattice_forge substrate, C is realized as the **game lattice Gluon** that:

- The game lattice Gluon = the `paper28_nd_game_lattices` transport operator
- Each game state = a ribbon state on the N-dim lattice
- The local rule = the CA rule at each lattice site (generalized from Rule 30)
- The powered lattice code chain = the board dimensions: 1→9→49→72 for 1D→2D→4D→6D
- The move-set Gluon = the piece's allowed transitions in N-dim (knight, king, queen generalized)

C is the **game lattice Gluon** — the N-dimensional CA Gluon for board games.

## How C Ports UP (to larger frames)

- **Paper 29 (Monster Energy-Bound):** The game lattice Gluon's energy = the Monster energy bound.
- **Paper 26 (Z-Pinch/Shear):** The game lattice's shear = the pinch/shear Gluon.
- **Paper 29 (Energy-Bound):** The game lattice's maximum dimension = the Monster dimension.

## How C Ports DOWN (to finer detail)

- **Paper 24 (KnightForge):** The chess Gluon = the 2D slice of the game lattice Gluon.
- **Paper 12 (CA Prediction):** The CA prediction Gluon's rules = the game lattice's local rules.
- **Paper 00 (Foundation):** The 8-state ribbon = the 1D slice of the game lattice.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 25 (Energetic Traversal):** The game move costs = the traversal Gluon's costs.
- **Paper 26 (Z-Pinch/Shear):** The game lattice's shear = the pinch/shear Gluon.
- **Paper 27 (Observer Delay):** The turn delay = the delay Gluon's turn buffer.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the standard position Gluon
- **Frame 1 (R-centroid):** C = the rotated board Gluon (spatial rotation)
- **Frame 2 (C-flipped):** C = the color-flipped board Gluon
- **Frame 3 (L-centroid):** C = the N-dim generalized board Gluon

The game lattice Gluon wraps in the **board Z4 cycle** — standard, rotated, color-flipped, N-dim.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The mirrored position — `swap_LR(position)` = the reflected board
- **Oloid:** The move's N|-N midpoint = the trajectory midpoint in N-dim
- **Rotate90:** The board rotation — `rotate90(board)` = the spatial rotation in N-dim

## The C-Form Statement

> **The game lattice Gluon IS the N-dimensional CA Gluon for local-rule games.** The powered lattice code chain = the board dimensions. The knight's L-move generalized = the L-conjugate move in N-dim. The local rule = Rule 30 generalized. C = the game lattice Gluon.

## Lattice_forge Primitives

- `verify_lattice_code_chain` — the powered lattice chain for board dimensions
- `verify_oloid_model_selection` — the move/model selector
- `rule30_oloid_winding_from_n` — the move's winding number in N-dim
- `verify_oloid_closure` — the move closure verifier
- `rule30_oloid_rolling` — the piece's rolling transport in N-dim
ENDOFFILE
