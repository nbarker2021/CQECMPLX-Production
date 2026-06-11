# Paper 12 — C-Form: CA Prediction Surface Gluon

## What C Is at This Dimension
**C = the CA prediction Gluon** — the local rule transducer that converts any CA candidate into a prediction surface tied to its local readout law. In the lattice_forge substrate, C is realized as the **CA prediction surface** (`rule30_readout_ribbon_machine`, `rule30_sheet_operator`) that:

- Takes any radius-1 Boolean rule `f : {0,1}³ → {0,1}` (256 ECAs)
- Decomposes `f = prior ⊕ correction` where `prior` is the transport structure (Rule 90, Rule 150, etc.)
- The prediction surface = the `correction` field over the light cone
- C = the `correction` field's Gluon at each lattice site

C is the **prediction Gluon** — the local `correction` field that distinguishes a CA from its transport prior.

## How C Ports UP (to larger frames)
- **Paper 13 (Quark-Face Transport):** The CA prediction Gluon's color = the quark-face color charge.
- **Paper 18 (VOA/Moonshine):** The CA prediction Gluon's VOA weight = the Moonshine representation.
- **Paper 24 (KnightForge/N-Dim Chess):** The CA prediction Gluon's move set = the chess operator algebra.

## How C Ports DOWN (to finer detail)
- **Paper 00 (Foundation T7):** The 8×8 transition matrix = the CA prediction surface's single-step kernel.
- **Paper 07 (Discrete-Continuous Bridge):** The bridge Gluon interpolates the discrete CA prediction to continuous fields.
- **Rule 90 Linearization:** The CA prediction Gluon = `correction = C ∧ ¬R` at each site.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 11 (Theory Admission):** The CA prediction Gluon is admitted iff its Gluon mass matches the trusted spectrum.
- **Paper 13 (Quark-Face Transport):** The CA prediction Gluon's 6 excited states = the 6 quark faces.
- **Paper 14 (GR Curvature):** The CA prediction Gluon's curvature = the Einstein tensor of the discrete manifold.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the local correction field at the lattice site
- **Frame 1 (R-centroid):** C = the right-shifted correction (causality direction)
- **Frame 2 (C-flipped):** C = the time-reversed correction (adjoint CA)
- **Frame 3 (L-centroid):** C = the left-shifted correction (anti-causality direction)

The CA prediction Gluon wraps in the **CA Z4 cycle** — the 256 ECAs partition into 64 silent-boundary rules that close at n=3.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The adjoint CA — `swap_LR(CA)` = the time-reversed rule
- **Oloid:** The CA's N|-N midpoint = the rule's fixed point (glider gun, still life, etc.)
- **Rotate90:** The rule's spatial rotation — `rotate90(CA)` = the rotated neighborhood rule

## The C-Form Statement
> **The CA prediction Gluon IS the local `correction` field over the light cone.** It is the `C ∧ ¬R` term that distinguishes a CA from its transport prior. The 64 silent-boundary rules are the confirmed predictions (exact n=3 closure). C = the local correction field.

## Lattice_forge Primitives
- `rule30_readout_ribbon_machine` — the CA prediction engine
- `rule30_sheet_operator` — the sheet operator for any ECA
- `rule30_vignette_algebra` — the local readout algebra
- `verify_rule30_vignette_algebra` — the local algebra verifier
- `verify_universal_ca` — the 256 ECA closure verifier (64 silent-boundary rules)
ENDOFFILE
