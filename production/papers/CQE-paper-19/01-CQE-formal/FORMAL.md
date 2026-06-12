# Paper 19 — C-Form: Observer Face-Selection Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the observer frame Gluon** — the face-selection operator that chooses which face of the local chart state is the active center. In the lattice_forge substrate, C is realized as the **observer Gluon** that:

- Takes the 8 chart states and selects the active C-face via the readout law: `bit = NOT L if C=1 else L⊕R`
- The face selection IS the Gluon's frame choice: Frame 0 (C-centroid), Frame 1 (R-centroid), Frame 2 (C-flipped), Frame 3 (L-centroid)
- Each face selection = a different Gluon component: `C_face = {C_C, C_R, C_L, C_C_flipped}`
- The latent alternatives (the 3 unselected faces) are the obligations (Paper 00: O slot)

C is the **observer Gluon** — the frame selector that chooses which boundary is the active center.

## How C Ports UP (to larger frames)

- **Paper 20 (Layer-2 Synthesis Ledger):** The observer Gluon's face choice = the synthesis ledger's perspective frame.
- **Paper 27 (Observer Delay):** The observer Gluon's delay = the sampling buffer's frame lag.
- **Paper 31 (Meta LCR):** The meta-walkthrough's enacted LCR = the observer Gluon's enacted face sequence.

## How C Ports DOWN (to finer detail)

- **Paper 00 (Foundation T3):** The readout law IS the observer Gluon's face selection.
- **Paper 01 (Side-flip):** The side-flip = the face selection's antipode.
- **Paper 03 (Triality Center):** The 4 Lie conjugates = the 4 frame choices the observer can make.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 18 (VOA/Moonshine):** The observer's frame = the Moonshine Gluon's D12 frame.
- **Paper 17 (E6-E8 Tower):** The observer's frame at each tower level = the tower's observer Gluon.
- **Paper 20 (Layer-2 Synthesis):** The observer's face selection = the synthesis perspective.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the C-centroid face (standard observer)
- **Frame 1 (R-centroid):** C = the R-centroid face (right-boundary observer)
- **Frame 2 (C-flipped):** C = the C-flipped face (antipodal observer)
- **Frame 3 (L-centroid):** C = the L-centroid face (left-boundary observer)

The observer Gluon wraps in the **Z4 face cycle** — each frame rotation is a face selection.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The antipodal observer — `swap_LR(observer)` = the antipodal face selection
- **Oloid:** The observer's N|-N midpoint = the frame's canonical midpoint
- **Rotate90:** The frame rotation — `rotate90(observer)` = the next face selection

## The C-Form Statement

> **The observer Gluon IS the face-selector that chooses the active C-face from the 4-frame Z4 cycle.** The 3 unselected faces are the latent obligations (O slot). C = the selected face's Gluon. The Z4 face cycle = the enacted LCR process (Paper 31).

## Lattice_forge Primitives

- `centroid_voa.four_frame_label` — the 4-frame face labels
- `centroid_voa.z4_period` — the Z4 face period
- `centroid_voa.verify_z4_period_template` — the face period verifier
- `centroid_voa.TRANSPOSITIONS` — the face selection transpositions
- `centroid_voa.verify_z4_period_template` — the Z4 face cycle verifier
ENDOFFILE
