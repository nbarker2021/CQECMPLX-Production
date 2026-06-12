# Paper 16 — C-Form: Continuum Edge Residuals Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the edge residual Gluon** — the Gluon that transports the residual correction bits at powers of ten (K=10, 100, 1000...). In the lattice_forge substrate, C is realized as the **edge residual Gluon** that:

- At each power of ten (K=10^k), the lattice code chain has a boundary where the K-window is exceeded
- The edge residual Gluon = the `correction` bits at the K-window boundary: `C_residual = C ∧ ¬R` at K=10, 100, 1000...
- The continuum limit = the infinite sequence of edge residuals `C_residual(10), C_residual(100), C_residual(1000)...`
- The continuum edge = the accumulation point of edge residuals in the L_p norm

C is the **edge residual Gluon** — the Gluon that lives at the boundary of each K-window.

## How C Ports UP (to larger frames)

- **Paper 17 (E6-E8 Tower):** The edge residual Gluon at each tower level = the tower's edge residual.
- **Paper 29 (Monster Energy-Bound):** The continuum edge Gluon = the Monster energy bound's edge residual.
- **Paper 29 (Energy-Bound):** The edge residual Gluon's limit = the universal energy bound.

## How C Ports DOWN (to finer detail)

- **Paper 08 (E8/Niemeier/Leech):** The K-window boundary is the Nebe shell (K=9). The edge residual at K=10 is the first off-shell correction.
- **Paper 09 (Hamiltonian Temporal):** The edge residual Gluon = the Hamiltonian time derivative at powers of ten.
- **Paper 07 (Discrete-Continuous Bridge):** The bridge Gluon's derivative at K=10^k = the edge residual Gluon.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 15 (Higgs):** The Higgs Gluon's edge residual = the mass gap at the boundary.
- **Paper 14 (GR Curvature):** The curvature Gluon's edge residual = the boundary stress tensor.
- **Paper 17 (E6-E8 Tower):** The tower's edge residual = the continued fraction of the tower.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the edge residual at K=10
- **Frame 1 (R-centroid):** C = the edge residual at K=100
- **Frame 2 (C-flipped):** C = the edge residual at K=1000
- **Frame 3 (L-centroid):** C = the edge residual at K=10000

The edge residual Gluon wraps in the **powers-of-ten Z4 cycle** — each frame is a decade.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The interior residual — `swap_LR(edge)` = the interior correction
- **Oloid:** The edge N|-N midpoint = the K-window boundary operator `s* = C`
- **Rotate90:** The scale rotation — `rotate90(edge)` = the next decade's edge residual

## The C-Form Statement

> **The continuum edge Gluon IS the sequence of `correction` bits at powers of ten.** `C(10^k) = C ∧ ¬R` at the K-window boundary. The continuum limit = the infinite sequence. C = the edge residual Gluon at the K-window boundary.

## Lattice_forge Primitives

- `rule30_center_via_decomposition` — the edge residual evaluator at depth N
- `rule30_oloid_winding_from_n` — the winding number at depth N
- `verify_oloid_model_selection` — the Oloid model selector for edge residuals
- `verify_lattice_code_chain` — the lattice chain at K=9 boundary
- `rule30_mandelbrot_boundary_scalar` — the Mandelbrot boundary scalar at the edge
ENDOFFILE
