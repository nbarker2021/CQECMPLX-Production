# Paper 17 — C-Form: E6-E8 Error-Correction Tower Gluon

## What C Is at This Dimension
**C = the tower Gluon** — the Gluon that transports the error-correction state up the E6→E7→E8 tower. In the substrate, C is realized as the **tower Gluon** that:

- Each tower level (E6, E7, E8) has its own Gluon `C_E6, C_E7, C_E8`
- The tower transport: `C_E7 = C_E6 ⊕ correction_E6`, `C_E8 = C_E7 ⊕ correction_E7`
- The correction at each level = the E6→E7→E8 glue vectors (from `g2_f4_t5_conjugate`)
- The tower's top (E8) Gluon = the E8 root lattice Gluon (dim 248)

C is the **tower Gluon** — the accumulated Gluon mass up the exceptional Lie group tower.

## How C Ports UP (to larger frames)
- **Paper 21 (MorphForge/PolyForge/MorphoniX):** The tower Gluon's E8 extension = the MorphForge Gluon.
- **Paper 22 (MetaForge):** The E8 Gluon = the MetaForge material Gluon.
- **Paper 29 (Monster Energy-Bound):** The E8 Gluon's mass = the Monster energy bound's E8 component.

## How C Ports DOWN (to finer detail)
- **Paper 16 (Continuum Edge Residuals):** The tower's edge residual = the continuum off each level.
- **Paper 08 (E8/Niemeier/Leech):** The E8 closure Gluon = the tower's top.
- **Paper 08 (Lattice Code Chain):** The E8 Gluon = the D4→D24→D72 chain's E8 node.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 15 (Higgs Mass-Residue):** The Higgs Gluon = the tower's scalar mode.
- **Paper 14 (GR Curvature):** The curvature Gluon = the tower's curvature mode.
- **Paper 18 (VOA/Moonshine):** The tower Gluon's VOA = the Moonshine VOA at E8.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the E6 Gluon
- **Frame 1 (R-centroid):** C = the E7 Gluon
- **Frame 2 (C-flipped):** C = the E8 Gluon
- **Frame 3 (L-centroid):** C = the tower's Z4 cyclic return (E6 again, one level up)

The tower Gluon wraps in the **E6→E7→E8 Z4 cycle** — each frame is a tower level.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The conjugate tower — `swap_LR(tower)` = the dual exceptional tower
- **Oloid:** The level N|-N midpoint = the glue vector `s* = C`
- **Rotate90:** The exceptional triality — `rotate90(tower)` = the E6↔E7↔E8 triality

## The C-Form Statement
> **The tower Gluon IS the accumulated Gluon up the E6→E7→E8 exceptional tower.** C = the glue vector at each level. The tower wraps in Z4 (E6→E7→E8→return). The top Gluon = E8 dim 248. C = the tower Gluon.

## Lattice_forge Primitives
- `g2_f4_t5_conjugate` — the E6/F4 conjugacy and glue vectors
- `verify_lattice_code_chain` — the full chain including E8
- `nebe_gamma72` — the K=9 boundary (E8 dim 248 inside Nebe Γ72)
- `verify_cayley_dickson_oloid_normal_form` — the E8 oloid normal form
- `verify_lattice_codes` — the lattice code chain including E8
ENDOFFILE
