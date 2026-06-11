# Paper 23 — C-Form: FoldForge Protein Folding Gluon

## What C Is at This Dimension
**C = the protein fold Gluon** — the contact-map/topo Gluon that transports protein chain fold hypotheses through contact-map and topology receipts. In the lattice_forge substrate, C is realized as the **fold Gluon** that:

- The fold Gluon = the `foldforge` transport operator
- Each fold hypothesis = a ribbon path with contact-map receipts (tempus fugit)
- The fold transport = `fold_{n+1} = foldforge_hypothesis(fold_n, contact_map)`
- The fold Gluon's topology = the contact-map persistent homology barcode
- The fold Gluon's topology receipt = the homology barcode certificate

C is the **fold Gluon** — the contact-map/topo Gluon for protein folding.

## How C Ports UP (to larger frames)
- **Paper 24 (KnightForge):** The chess Gluon's board = the protein's fold board.
- **Paper 25 (Energetic Traversal):** The fold Gluon's energy landscape = the traversal Gluon's map.
- **Paper 29 (Energy-Bound):** The fold Gluon's energy = the Monster energy bound.

## How C Ports DOWN (to finer detail)
- **Paper 22 (MetaForge):** The material Gluon's fold constraints = the fold Gluon's constraints.
- **Paper 21 (MorphForge):** The morphic Gluon's bifurcations = the fold Gluon's fold logic.
- **Paper 20 (Layer-2 Synthesis):** The synthesis Gluon's protein candidates = the fold Gluon's hypotheses.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 24 (KnightForge):** Chess automata = protein fold paths with contact-map receipts.
- **Paper 25 (Energetic Traversal):** Energy landscape = fold energy landscape.
- **Paper 26 (Z-Pinch/Shear):** Z-pinch = protein shear fold.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the native fold Gluon (native state)
- **Frame 1 (R-centroid):** C = the unfolded Gluon (denatured)
- **Frame 2 (C-flipped):** C = the kinetic intermediate Gluon (transition state)
- **Frame 3 (L-centroid):** C = the misfolded Gluon (amyloid)

The fold Gluon wraps in the **folding Z4 cycle** — native, denatured, intermediate, misfolded.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The inverse fold — `swap_LR(fold)` = the unfolding path
- **Oloid:** The fold's N|-N midpoint = the transition state ensemble
- **Rotate90:** The fold's rotation = the Ramachandran rotation

## The C-Form Statement
> **The fold Gluon IS the contact-map/topo Gluon with homology barcode receipts.** Each fold hypothesis = a ribbon path with contact-map receipt. C = the fold's Gluon = the contact-map/topo invariant. C = the fold Gluon.

## Lattice_forge Primitives
- `verify_cayley_dickson_oloid_normal_form` — the fold's oloid normal form
- `verify_oloid_model_selection` — the fold model selector
- `rule30_oloid_rolling` — the fold's rolling transport (folding pathway)
- `rule30_oloid_winding_from_n` — the fold's winding number (topological invariant)
- `verify_oloid_closure` — the fold closure verifier (native state verification)
ENDOFFILE
