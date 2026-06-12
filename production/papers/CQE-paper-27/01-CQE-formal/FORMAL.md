# Paper 27 — C-Form: Observer Delay and Shared Reality Gluon

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## What C Is at This Dimension

**C = the delay/shared Gluon** — the sampling buffer and shared-state Gluon that transports observer delay and shared reality constraints. In the lattice_forge substrate, C is realized as the **delay/shared Gluon** that:

- The delay Gluon = the sampling buffer operator: `delay(C) = buffer[C, depth]` where `depth` is the observer's sampling delay
- The shared Gluon = the shared-state operator: `shared(C_i, C_j) = C_i ⊕ C_j` (Gluon XOR for shared state)
- The observer delay = the frame lag in the Z4 cycle: `delay = frame_{t} - frame_{t-τ}`
- The shared reality = the Gluon overlap: `shared_reality = C_i ∧ C_j` (Gluon AND)

C is the **delay/shared Gluon** — the sampling buffer and shared-state transporter.

## How C Ports UP (to larger frames)

- **Paper 28 (N-Dim Game Lattices):** The delay Gluon's lag = the game turn delay.
- **Paper 29 (Energy-Bound):** The delay Gluon's energy cost = the Monster energy bound.
- **Paper 31 (Meta LCR):** The meta-walkthrough's enacted LCR = the delay/shared Gluon's enactment.

## How C Ports DOWN (to finer detail)

- **Paper 19 (Observer Face-Selection):** The observer's frame delay = the delay Gluon's buffer.
- **Paper 10 (T10 Master Receipt):** The master receipt's delay = the delay Gluon's timestamp.
- **Paper 06 (Causal Code):** The causal edge's delay = the delay Gluon's propagation time.

## How C Ports SIDEWAYS (adjacent papers, same scale)

- **Paper 26 (Z-Pinch/Shear):** The pinch Gluon's delay = the delay Gluon's compression time.
- **Paper 28 (N-Dim Game):** The game turn delay = the delay Gluon's turn buffer.
- **Paper 25 (Energetic Traversal):** The traversal time cost = the delay Gluon's energy-time.

## How C WRAPS (S₃ transposition / frame inversion)

- **Frame 0 (C-centroid):** C = the observer's current sample
- **Frame 1 (R-centroid):** C = the observer's delayed sample (one frame back)
- **Frame 2 (C-flipped):** C = the observer's predicted sample (one frame forward)
- **Frame 3 (L-centroid):** C = the shared state sample (synchronized)

The delay/shared Gluon wraps in the **observer Z4 cycle** — sample, delay, predict, synchronize.

## How C FOLDS (oloid/antipode/oloid operations)

- **Antipode:** The unsampled observer — `swap_LR(delay)` = the observer without buffer
- **Oloid:** The delay's N|-N midpoint = the shared state midpoint
- **Rotate90:** The delay's rotation = the shared state rotation

## The C-Form Statement

> **The delay/shared Gluon IS the sampling buffer and shared-state Gluon.** Delay = frame lag in Z4 cycle. Shared = Gluon XOR/AND for shared state. C = the delay/shared Gluon. The enacted LCR (Paper 31) IS the delay/shared Gluon's enactment.

## Lattice_forge Primitives

- `centroid_voa.four_frame_label` — the 4-frame observer frames
- `centroid_voa.verify_z4_period_template` — the observer Z4 period
- `centroid_voa.TRANSPOSITIONS` — the observer frame transpositions
- `centroid_voa.verify_z4_period_template` — the observer Z4 period verifier
- `verify_rule30_symmetry_environment` — the observer symmetry environment
ENDOFFILE
