# Paper 18 — C-Form: VOA/Moonshine Representation Routes Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the Moonshine Gluon** — the VOA modular kernel that transports representation routes between the Voa sectors and the Conway-Norton modular forms. In the lattice_forge substrate, C is realized as the **Moonshine Gluon** that:

- The VOA sector decomposition (Paper 03): 2 true vacua (weight 0) + 6 excited (weight 5)
- The Moonshine Gluon = the modular form `j(τ) = 1/q + 744 + 196884q + ...`
- The 196884 = 1 + 196883 decomposition = `C = C_vacuum ⊕ C_moonshine` where:
  - `C_vacuum` = 1 (the trivial representation, dimension 1)
  - `C_moonshine` = 196883 (the Monster's smallest representation)
- The 4-frame Z4 period (Paper 03) = the D12 action on the Moonshine module

C is the **Moonshine Gluon** — the VOA modular kernel that transports between the Conway-Norton correspondences.

## How C Ports UP (to larger frames)

- **Paper 29 (Monster Energy-Bound):** The Moonshine Gluon's dimension = 196883 = the Monster's smallest representation.
- **Paper 29 (Energy-Bound):** The Moonshine Gluon's dimension × 3 = 3×196883 = the Monster order bound.
- **Paper 18 (Meta LCR):** The Moonshine Gluon's Z4 period = the meta-walkthrough's frame cycle.

## How C Ports DOWN (to finer detail)

- **Paper 03 (Triality Center):** The 2+6 VOA split = the Moonshine Gluon's sector decomposition.
- **Paper 13 (Quark-Face):** The 6 quark faces = the 6 excited VOA states transported by the Moonshine Gluon.
- **Paper 08 (Leech Lattice):** The Leech lattice (D24) = the Moonshine Gluon's lattice.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 14 (GR Curvature):** The Moonshine Gluon's curvature = the Moonshine moduli space curvature.
- **Paper 15 (Higgs):** The Higgs Gluon's VOA weight = the Moonshine Gluon's conformal weight.
- **Paper 17 (E6-E8 Tower):** The E8 Gluon's VOA = the Moonshine Gluon's E8 sector.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the trivial representation Gluon (dimension 1)
- **Frame 1 (R-centroid):** C = the Moonshine Gluon (dimension 196883)
- **Frame 2 (C-flipped):** C = the dual Moonshine Gluon (the conjugate representation)
- **Frame 3 (L-centroid):** C = the Monster conjugate Gluon (the Pariah boundary)

The Moonshine Gluon wraps in the **D12 Z4 cycle** — the D12 acts on D4 as blocks, the Z4 is the order-4 subgroup acting on Moonshine blocks.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The Monster conjugate — `swap_LR(Moonshine)` = the Pariah boundary Gluons
- **Oloid:** The Monster's N|-N midpoint = the supersingular prime product (47·59·71)
- **Rotate90:** The Monster rotation = the McKay-Thompson series cycle

## The C-Form Statement

> **The Moonshine Gluon IS the VOA modular kernel `j(τ)` transporting between sectors.** `j(τ) = 1/q + 744 + 196884q + ... = C_vacuum ⊕ C_moonshine`. The 2+6 VOA split = the trivial ⊕ Moonshine sectors. C = the Moonshine Gluon.

## Lattice_forge Primitives

- `verify_centroid_voa_chain` — the VOA sector verifier (2+6 split)
- `verify_z4_period_template` — the Z4 period = D12 action on Moonshine blocks
- `verify_monster_moonshine` — the Moonshine module verifier
- `verify_rule30_wow_signal` — the Wow signal as structural pointer to Monster D4
- `verify_voa_sector_decomposition` — the 2+6 VOA sector verifier
ENDOFFILE
