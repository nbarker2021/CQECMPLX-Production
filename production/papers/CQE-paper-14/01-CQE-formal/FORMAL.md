# Paper 14 — C-Form: GR Boundary-Repair Curvature Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the curvature Gluon** — the boundary repair operator that frames Einstein-Cartan curvature as a boundary repair demand. In the lattice_forge substrate, C is realized as the **curvature Gluon** that:

- Takes a boundary repair (Paper 04) and maps it to the Einstein-Cartan curvature tensor
- The boundary repair Gluon (Paper 04) = the torsion tensor `T^λ_μν`
- The curvature Gluon = the Riemann tensor `R^ρ_σμν` derived from torsion via `R = dT + T∧T`
- Einstein's equation: `G_μν = κ T_μν` where `T_μν` is the boundary repair residue (ErrorWall)

C is the **curvature Gluon** — the Riemann tensor that emerges from the boundary repair torsion.

## How C Ports UP (to larger frames)

- **Paper 15 (Higgs Mass-Residue):** The curvature Gluon's mass = the Higgs mass-residue carrier.
- **Paper 17 (E6-E8 Error-Correction Tower):** The curvature Gluon at each tower level = the tower's curvature Gluon.
- **Paper 29 (Monster Energy-Bound):** The curvature Gluon's scalar = the Monster energy bound.

## How C Ports DOWN (to finer detail)

- **Paper 04 (Boundary Repair):** The ErrorWall's Gluon = the torsion tensor source for curvature.
- **Paper 08 (E8/Niemeier/Leech):** The curvature Gluon's holonomy = the lattice code chain transport.
- **Paper 13 (Quark-Face):** The color Gluon's torsion = the quark-face torsion.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 13 (Quark-Face):** The quark-face Gluon's torsion = the color torsion.
- **Paper 15 (Higgs Mass-Residue):** The curvature Gluon's scalar = the Higgs field.
- **Paper 16 (Continuum Edge Residuals):** The curvature Gluon's edge residual = the continuum boundary repair.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the Riemann tensor `R^ρ_σμν`
- **Frame 1 (R-centroid):** C = the dual Riemann tensor `*R^ρ_σμν`
- **Frame 2 (C-flipped):** C = the torsion tensor `T^λ_μν` (the boundary repair)
- **Frame 3 (L-centroid):** C = the Einstein tensor `G_μν`

The curvature Gluon wraps in the **Riemann Z4 cycle** — the sequence Riemann→Dual→Torsion→Einstein is the 4-frame rotation.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The dual curvature — `swap_LR(Riemann)` = the dual tensor
- **Oloid:** The curvature Gluon's midpoint = the Einstein-Cartan connection (C = the connection)
- **Rotate90:** The curvature Gluon's rotation = the chamber reflection

## The C-Form Statement

> **The curvature Gluon IS the Riemann tensor derived from boundary repair torsion.** `R = dT + T∧T` where T is the boundary repair Gluon (Paper 04). Einstein's equation is the boundary repair budget: `G_μν = κ T_μν` where T is the ErrorWall residue. C = the curvature Gluon.

## Lattice_forge Primitives

- `verify_rule30_oloid_antipodal_winding` — the boundary repair winding verifier
- `rule30_oloid_winding_from_n` — the curvature winding number
- `rule30_oloid_antipodal_winding` — the curvature duality verifier
- `verify_oloid_closure` — the oloid closure = the Einstein-Cartan closure
- `rule30_oloid_rolling` — the rolling curvature = the parallel transport
ENDOFFILE
