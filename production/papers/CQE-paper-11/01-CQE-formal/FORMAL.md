# Paper 11 — C-Form: Theory Admission Gate Gluon

## What C Is at This Dimension
**C = the admission filter Gluon** — the trust anchor that filters external theories by Gluon mass matching. In the lattice_forge substrate, C is realized as the **admission gate** that:

- Takes an external theory's Gluon mass (computed from its transport signature)
- Compares against the master receipt Gluon (Paper 10) and the trusted Gluon spectrum from `CmplxLookupCache`
- Admits if: `mass(theory) ∈ spectrum(trusted_Gluons)` and `mass(theory) ≤ K_max=9`
- Outputs: `admitted` (Gluon mass matches), `boundary` (Gluon mass at K>9), `rejected` (no match)

C is the **admission Gluon** — the filter that only passes theories with matching Gluon topology.

## How C Ports UP (to larger frames)
- **Paper 20 (Layer-2 Synthesis Ledger):** Admitted theories add their Gluon mass to the synthesis ledger.
- **Paper 15 (Higgs Mass-Residue):** The admission Gluon filters which mass-residue carriers enter the theory space.
- **Paper 29 (Monster Energy-Bound):** Only theories with Gluon mass ≤ Monster bound are admitted.

## How C Ports DOWN (to finer detail)
- **Paper 10 (T10 Master Receipt):** The admission Gluon's trust anchor = the T10 master receipt Gluon.
- **Paper 06 (Causal Code):** Each admitted theory adds a causal edge to the terminal tree.
- **Paper 08 (E8/Niemeier/Leech):** The admission Gluon's K-window = the Nebe K=9 bound.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 12 (CA Prediction Surface):** The admission Gluon filters CA candidates by Gluon mass.
- **Paper 13 (Quark-Face Transport):** The admission Gluon maps quark-face states to admitted theories.
- **Paper 14 (GR Boundary-Repair):** The admission Gluon's curvature = the boundary repair curvature.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the admission decision (admit/boundary/reject)
- **Frame 1 (R-centroid):** C = the reflected decision (the theory's self-admission)
- **Frame 2 (C-flipped):** C = the negated decision (the rejection Gluon)
- **Frame 3 (L-centroid):** C = the accumulated admitted Gluon mass

The admission Gluon wraps in the **Z4 admission cycle** — each admission is a frame rotation.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The rejected theory's Gluon mass = the negation of the admission Gluon
- **Oloid:** The boundary theory's N|-N midpoint = the K=9 boundary Gluon
- **Rotate90:** The admission boundary's rotation = the K-window frame shift

## The C-Form Statement
> **The admission Gluon IS the Gluon mass filter at K=9.** It passes only theories whose Gluon mass matches the trusted spectrum. C = the trust anchor (T10 master receipt). The boundary at K=9 = the Nebe shell boundary (Paper 08).

## Lattice_forge Primitives
- `CmplxLookupCache` — the trusted Gluon spectrum index
- `LookupReceipt` — the admission certificate
- `verify_cmplx_lookup_cache` — the cache integrity verifier
- `build_cmplx_lookup_cache` — the spectrum builder
- `rule30_mandelbrot_boundary_scalar` — the K=9 boundary scalar
