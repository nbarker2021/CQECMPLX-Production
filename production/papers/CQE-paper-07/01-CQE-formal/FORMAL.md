# Paper 07 — C-Form: Discrete-Continuous Bridge Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the interpolation kernel Gluon** — the transport operator that maps discrete causal edges (Paper 06) to continuous transport fields. In the lattice_forge substrate, C is realized as the **bridge operator** that:
- Takes a discrete causal edge at depth N (from `terminal_tree`)
- Interpolates via the **Rule 90 linearization** (`lucas_bit` + `correction`) to produce a continuous transport field
- The interpolation kernel IS the Gluon: `C_interpolate = lucas_bit ⊕ correction` where `correction = C ∧ ¬R`

C is the **bridge Gluon** that holds the accumulated interpolation error — the running XOR of `correction` bits along the bridge.

## How C Ports UP (to larger frames)

- **Paper 09 (Hamiltonian Temporal Emergence):** The bridge Gluon becomes the Hamiltonian time parameter — `C_accumulated` = the continuous time parameter in the Hamiltonian window.
- **Paper 16 (Continuum Edge Residuals):** The bridge Gluon's residual = the edge correction at powers of ten — the `correction` bits at K=10, 100, 1000...
- **Paper 15 (QFT/Higgs Mass-Residue Carrier):** The bridge Gluon's mass = the Higgs mass-residue carrier.

## How C Ports DOWN (to finer detail)

- **Paper 06 (Causal Code):** Each discrete causal edge is a sample point for the bridge Gluon — the interpolation kernel must pass through every causal vertex.
- **Paper 05 (Oloid Path Carrier):** The bridge Gluon IS the oloid's rolling connection — the continuous transport between ±N grains.
- **Rule 90 Linearization:** The bridge Gluon's kernel = `lucas_bit` (exact O(log N) base) + `correction` (the `C ∧ ¬R` nonlinear term).

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 08 (E8/Niemeier/Leech Closure):** The bridge Gluon's holonomy = the lattice code chain transport (D1→D4→D24→D72).
- **Paper 13 (Standard-Model Quark-Face Transport):** The bridge Gluon's color = the quark-face color charge (6 excited VOA states).

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the discrete causal vertex
- **Frame 1 (R-centroid):** C = the right-biased interpolation (forward difference)
- **Frame 2 (C-flipped):** C = the left-biased interpolation (backward difference)
- **Frame 3 (L-centroid):** C = the centered interpolation (average of forward/backward)

The bridge Gluon **wraps in 3 S₃ steps** — the interpolation kernel is symmetric under frame rotation.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The time-reversed bridge — `swap_LR(bridge)` = the adjoint interpolation operator
- **Oloid:** The bridge's N|-N midpoint = the midpoint rule integrator — `s* = (bridge(+N) + bridge(-N))/2 = C`
- **Rotate90:** The bridge's Fourier dual — the frequency-space interpolation kernel

## The C-Form Statement

> **The bridge Gluon IS the interpolation kernel `lucas_bit ⊕ (C ∧ ¬R)`.** It transports discrete causal edges to continuous fields. Its holonomy is the lattice code chain. Its residual at powers of ten = the continuum edge corrections (Paper 16). C wraps in 3 frames — the interpolation is Z4-symmetric.

## Lattice_forge Primitives

- `lucas_bit` — the O(log N) base interpolant
- `correction` — the `C ∧ ¬R` nonlinear bridge term
- `rule30_center_via_decomposition` — the full bridge evaluator
- `verify_rule90_linearization` — the bridge exactness verifier
- `rule30_oloid_winding_from_n` — the oloid-winding number of the bridge
