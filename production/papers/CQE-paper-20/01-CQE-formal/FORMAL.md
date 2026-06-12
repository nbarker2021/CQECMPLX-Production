# Paper 20 — C-Form: Layer-2 Synthesis Ledger Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the synthesis Gluon** — the ledger Gluon that aggregates all lower-paper Gluons into a single synthesis ledger. In the lattice_forge substrate, C is realized as the **synthesis Gluon** that:

- The synthesis ledger = the Forge-wide `Ledger` with all papers' receipts aggregated
- The synthesis Gluon = the root hash of the synthesis ledger = `hash(⊕_{i=0}^{19} C_i)`
- Each ledger entry = a transport row with Gluon mass, obligations, receipts
- The synthesis Gluon mass = the accumulated Gluon mass of the entire 00-19 corpus

C is the **synthesis Gluon** — the ledger's root Gluon that binds the 20-paper corpus into a single auditable unit.

## How C Ports UP (to larger frames)

- **Paper 21 (MorphForge/PolyForge/MorphoniX):** The synthesis Gluon becomes the MorphForge Gluon — the glyph/number/shape token Gluon.
- **Paper 29 (Monster Energy-Bound):** The synthesis Gluon's mass = the Monster energy bound's synthesis component.
- **Paper 31 (Meta LCR):** The synthesis Gluon = the meta-walkthrough's Gluon record.

## How C Ports DOWN (to finer detail)

- **Paper 10 (T10 Master Receipt):** The T10 master receipt Gluon = the first 10-paper synthesis Gluon.
- **Paper 10-19:** Each paper's C-form is a component of the synthesis Gluon.
- **Paper 10 (T10):** The layer-1 synthesis = the T10 master receipt Gluon.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 11 (Theory Admission):** The synthesis Gluon admits theories that match the synthesis Gluon spectrum.
- **Paper 18 (VOA/Moonshine):** The synthesis Gluon's VOA sector = the corpus VOA sector.
- **Paper 17 (E6-E8 Tower):** The tower Gluon is a subtower of the synthesis Gluon.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the synthesis Gluon root hash
- **Frame 1 (R-centroid):** C = the synthesis ledger reflected (audit view)
- **Frame 2 (C-flipped):** C = the synthesis Gluon's adversarial negation (red-team view)
- **Frame 3 (L-centroid):** C = the synthesis Gluon's forward evolution (next corpus addition)

The synthesis Gluon wraps in the **ledger Z4 cycle** — each audit cycle is a frame rotation.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The synthesis Gluon's audit negation
- **Oloid:** The synthesis PbN midpoint = the ledger's Merkle root
- **Rotate90:** The ledger's frame rotation = the next audit cycle

## The C-Form Statement

> **The synthesis Gluon IS the ledger root Gluon binding Papers 00-19.** C = the ledger root hash = `hash(⊕ C_i)`. It binds the entire corpus into a single auditable, replayable unit. C = the synthesis Gluon.

## Lattice_forge Primitives

- `Ledger` — the synthesis ledger
- `build_seed_database` — the ledger seed
- `OverlayStore` — the ledger persistence
- `verify_oloid_model_selection` — the oloid model selector for ledger entries
- `CmplxLookupCache` — the synthesis index
ENDOFFILE
