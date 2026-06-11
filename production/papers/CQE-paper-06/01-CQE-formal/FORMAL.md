# Paper 06 — C-Form: Causal Code Gluon

## What C Is at This Dimension
**C = the causal edge Gluon** — the typed causal edge that transports dependency structure across papers, tools, and proofs. In the lattice_forge substrate, C is realized as the **terminal composition tree** (`build_terminal_composition_tree`) where each node is a causal edge carrying:
- `source`: the originating paper/tool/proof
- `target`: the dependent paper/tool/proof
- `edge_type`: `proves` | `uses` | `refines` | `obligates` | `transports`
- `receipt`: the `LookupReceipt` certifying the edge

C is the **causal Gluon** that holds the accumulated causal color — the XOR of all causal edge types along the transport path.

## How C Ports UP (to larger frames)
- **Paper 10 (T10 Master Receipt):** The causal Gluon becomes the master receipt's bonding agent — the `LookupReceipt` that certifies the entire 00-09 stack as a single causal unit.
- **Paper 11 (Theory Admission Gate):** C is the gate Gluon — the causal edge that classifies external theories by their admission status (`admitted` | `boundary` | `rejected`).
- **Paper 20 (Layer-2 Synthesis Ledger):** C accumulates into the synthesis ledger — the causal Gluon mass = XOR of all admitted theory edges.

## How C Ports DOWN (to finer detail)
- **Paper 05 (Oloid Path Carrier):** The causal edge IS the oloid's Dust bond — the mediator C = the causal Gluon of the N|-N dyad.
- **Paper 04 (Boundary Repair):** The causal edge classifies the ErrorWall type — CAPACITY_EXCEEDED = causal edge to Paper 08; MIRROR_REQUIRED = causal edge to oloid dual path.
- **Paper 03 (Triality Center):** The causal edge IS the triality rotation — σ₁σ₂σ₃σ₂ = the causal Gluon's Z4 cycle.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 07 (Discrete-Continuous Bridge):** The causal edge IS the bridge — the interpolation kernel mapping discrete causal edges to continuous transport fields.
- **Paper 06 (Causal Code) IS the side-flip of Paper 11:** Theory admission gates are the causal inverse of internal causal edges.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = causal edge source→target
- **Frame 1 (R-centroid):** C = causal edge reflected — the reverse dependency
- **Frame 2 (C-flipped):** C = the negated causal edge (adversarial witness)
- **Frame 3 (L-centroid):** C = the causal Gluon's mass = XOR of all edge types

The causal Gluon **wraps in ≤3 S₃ steps** to a Lie conjugate (Paper 03) — every causal chain terminates at a fixed point.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The negated causal edge — the "not-proves" witness
- **Oloid:** The causal Dust pair — (proves, disproves) bonded with C = the adjudication Gluon
- **Rotate90:** The frame rotation that swaps source↔target while preserving C

## The C-Form Statement
> **The causal Gluon IS the terminal composition tree.** Every dependency is a typed edge with a LookupReceipt. The C-accumulated mass = XOR of all edge types along the path. C wraps to Lie conjugates in ≤3 S₃ steps. The oloid midpoint s* = C is the adjudication Gluon for adversarial pairs.

## Lattice_forge Primitives
- `build_terminal_composition_tree` — the causal Gluon structure
- `LookupReceipt` — the edge certificate
- `CmplxLookupCache` — the causal index
- `verify_terminal_trees` — the causal coherence verifier
- `terminal_tree` — the causal spine of the 32-paper corpus
