# Paper 13 — C-Form: Standard-Model Quark-Face Transport Gluon

## What C Is at This Dimension
**C = the quark-face color Gluon** — the color charge that transports the 6 excited VOA states (the 6 quark faces) across the color-triality surface. In the lattice_forge substrate, C is realized as the **quark-face transport operator** that:

- Maps the 6 excited VOA states (from centroid_voa: weight-5 states) to the 6 quark faces: R, G, B and anti-R, anti-G, anti-B
- The 2 true vacua (weight-0) = the lepton pair (e, ν_e) — color neutral
- The transport rule: `C_transport = C_quark ⊗ C_gluon` where C_gluon is the gluon from Paper 00

C is the **color Gluon** — the SU(3) color charge that transports quark faces through the color-triality surface.

## How C Ports UP (to larger frames)
- **Paper 14 (GR Boundary-Repair Curvature):** The color Gluon's holonomy = the Einstein-Cartan torsion tensor.
- **Paper 15 (Higgs Mass-Residue):** The color Gluon's mass = the Higgs mass-residue carrier.
- **Paper 17 (E6-E8 Error-Correction Tower):** The color Gluon at E6/E7/E8 levels = the tower's colorGluon.

## How C Ports DOWN (to finer detail)
- **Paper 03 (Triality Center):** The 6 excited VOA states = the 6 color states at shell=2 (D4).
- **Paper 01 (Side-flip):** The side-flip is one edge of the triality triangle. (1,1,0) ↔ (0,1,1) is the (1 3) permutation — one transposition in the triality cycle.
- **Paper 02 (Correction Surface):** The correction surface's MIRROR_REQUIRED gate fires when the ±k pair are both Lie conjugates (L=R states) — the triality attractor surface.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 11 (Theory Admission):** The quark-face Gluon is admitted iff its color charge matches the trusted spectrum.
- **Paper 14 (GR Boundary-Repair):** The color Gluon's curvature = the torsion-induced curvature.
- **Paper 15 (Higgs Mass-Residue):** The color Gluon's mass = the Higgs mechanism.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the color charge (R, G, B, anti-R, anti-G, anti-B)
- **Frame 1 (R-centroid):** C = the rotated color (R→G→B→R under su(3) cycle)
- **Frame 2 (C-flipped):** C = the conjugate color (color ↔ anticolor)
- **Frame 3 (L-centroid):** C = the CU(3) invariant (baryon number)

The color Gluon wraps in the **SU(3) Z3 cycle** — the color rotation is the triality rotation.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** Color conjugation — `swap_LR(quark)` = the antiquark face
- **Oloid:** The color Gluon's midpoint = the gluon mediator (the gluon IS the oloid midpoint)
- **Rotate90:** The color rotation — `rotate90(color)` = the next color in the cycle

## The C-Form Statement
> **The quark-face Gluon IS the SU(3) color charge transporting the 6 excited VOA states.** The 2 true vacua = color-neutral leptons. The color Gluon wraps in the SU(3) Z3 triality cycle. The gluon IS the oloid midpoint between color and anticolor.

## Lattice_forge Primitives
- `centroid_voa` — the 2+6 VOA split (2 true vacua = leptons, 6 excited = quarks)
- `verify_voa_sector_decomposition` — the color/orbit verifier
- `verify_rule30_color_chirality_cipher` — the color chirality transport
- `verify_z4_period_template` — the Z4 period on the color-triality surface
- `verify_rule30_spinor_oloid_model` — the spinor-oloid color model
ENDOFFILE
