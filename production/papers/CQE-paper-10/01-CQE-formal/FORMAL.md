# Paper 10 — C-Form: T10 Master Receipt Gluon

## What C Is at This Dimension
**C = the master receipt Gluon** — the `LookupReceipt` that binds Papers 00-09 into a single inspectable, replayable causal unit. In the lattice_forge substrate, C is realized as the **master receipt** that:

- Composes all 10 paper receipts into a single `LookupReceipt` via `CmplxLookupCache`
- The master receipt's Gluon = the XOR of all 10 paper C-forms: `C_T10 = C₀ ⊕ C₁ ⊕ ... ⊕ C₉`
- The master receipt certifies: every claim in 00-09 has a receipt, every obligation is logged, every transport is replayable

C is the **master receipt Gluon** — the binding Gluon that makes the stack inspectable.

## How C Ports UP (to larger frames)
- **Paper 11 (Theory Admission Gate):** The master receipt Gluon is the admission authority — only theories with matching Gluon mass are admitted.
- **Paper 20 (Layer-2 Synthesis Ledger):** The master receipt Gluon becomes the synthesis ledger's root hash.
- **Paper 31 (Meta LCR):** The master receipt Gluon = the meta-walkthrough's enacted LCR certificate.

## How C Ports DOWN (to finer detail)
- **Paper 00-09:** Each paper's C-form is a component of the master receipt Gluon.
- **Paper 06 (Causal Code):** The master receipt Gluon = the causal edge that binds all 10 papers.
- **Paper 04 (Boundary Repair):** The master receipt Gluon = the repair certificate for the entire stack.

## How C Ports SIDEWAYS (adjacent papers, same scale)
- **Paper 11 (Theory Admission Gate):** The master receipt Gluon is the admission filter's trust anchor.
- **Paper 11 (Theory Admission Gate):** Theories with non-matching Gluon mass are rejected at the gate.

## How C WRAPS (S₃ transposition / frame inversion)
- **Frame 0 (C-centroid):** C = the composed receipt (all 10 papers)
- **Frame 1 (R-centroid):** C = the receipt reflected — the verification witness
- **Frame 2 (C-flipped):** C = the receipt's negation (the adversarial audit)
- **Frame 3 (L-centroid):** C = the receipt's forward evolution (the next master receipt)

The master receipt Gluon wraps in the **receipt composition Z4 cycle** — each composition is a frame rotation.

## How C FOLDS (oloid/antipode/oloid operations)
- **Antipode:** The audit trail = the master receipt's negation
- **Oloid:** The master receipt's N|-N midpoint = the composition operator `⊕`
- **Rotate90:** The receipt's rotation = the frame-shifted audit

## The C-Form Statement
> **The master receipt Gluon IS the composed receipt binding Papers 00-09.** C = `C₀ ⊕ C₁ ⊕ ... ⊕ C₉`. It certifies the entire stack as inspectable, replayable, and causally complete. The master receipt is the trust anchor for all higher papers.

## Lattice_forge Primitives
- `CmplxLookupCache` — the receipt index
- `LookupReceipt` — the edge certificate
- `verify_cmplx_lookup_cache` — the cache integrity verifier
- `build_cmplx_lookup_cache` — the receipt composer
- `OverlayStore` — the receipt persistence layer
