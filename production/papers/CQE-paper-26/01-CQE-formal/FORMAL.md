# Paper 26 — C-Form: Z-Pinch and Shear Horizon Gluon

## What C Is at This Dimension
**C = the Z-pinch/shear Gluon** — the first-shear/pinch Gluon that examines friction-like generation at the horizon of proven layers. In the lattice_forge substrate, C is realized as the **Z-pinch Gluon** that:

- The Z-pinch Gluon = the `paper26_zpinch_shear` transport operator
- The pinch = the gluon compression operator: `pinch(C) = C / ||C||` (normalization)
- The shear = the off-diagonal Gluon transport: `shear(C) = C_xy + C_yx` (off-diagonal components)
- The horizon = the K=9 boundary where the Z-pinch/shear Gluon operates
- The Z-pinch Gluon's compression = the gluon mass concentration at the boundary

C is the **pinch/shear Gluon** — the boundary Gluon that compresses and shears at the K=9 horizon.

## How C Ports UP (to larger frames)
- **Paper 29 (Monster Energy-Bound):** The pinch/shear Gluon's maximum = the Monster energy bound.
- **Paper 27 (Observer Delay):** The pinch/shear Gluon's delay = the observer's shear delay.
- **Paper 27 (Shared Reality):** The pinch/shear Gluon's shared state = the shared reality Gluon.

## How C Ports DOWN (to finer detail)
- **Paper 25 (Energetic Traversal):** The traversal Gluon's shear = the pinch/shear Gluon's off-diagonal.
- **Paper 16 (Continuum Edge Residuals):** The edge residual Gluon at K>9 = the pinch/shear Gluon.
- **Paper 14 (GR Curvature):** The curvature Gluon's shear = the pinch/shear Gluon.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 27 (Observer Delay):** The pinch Gluon's delay = the delay Gluon's compression time.
- **Paper 27 (Shared Reality):** The shared Gluon's pile = the pinch/shear Gluon.
- **Paper 24 (KnightForge):** The chess Gluon's shear move = the pinch/shear Gluon.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the axial pinch Gluon (compression)
- **Frame 1 (R-centroid):** C = the shear Gluon (off-diagonal)
- **Frame 2 (C-flipped):** C = the torsion Gluon (twist)
- **Frame 3 (L-centroid):** C = the relief Gluon (release)

The pinch/shear Gluon wraps in the **shear Z4 cycle** — pinch, shear, torsion, relief.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The expansion — `swap_LR(pinch)` = the anti-pinch (expansion)
- **Oloid:** The pinch's N|-N midpoint = the shear center
- **Rotate90:** The pinch's rotation = the shear rotation

## The C-Form Statement
> **The pinch/shear Gluon IS the boundary Gluon compressing and shearing at K=9.** `pinch = C / ||C||`, `shear = off-diagonal(C)`. The horizon = K=9 boundary. C = the pinch/shear Gluon.

## Lattice_forge Primitives
- `rule30_oloid_winding_from_n` — the pinch winding number
- `rule30_oloid_rolling` — the pinch rolling transport
- `verify_oloid_model_selection` — the pinch model selector
- `verify_oloid_closure` — the pinch closure verifier
- `rule30_mandelbrot_boundary_scalar` — the Mandelbrot boundary scalar at the pinch
ENDOFFILE
