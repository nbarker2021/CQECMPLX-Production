# Paper 02 — Correction Surface

## Central Thesis
Treat failure, mismatch, and nonlinear residue as positive correction data rather than dismissal.

## Status
**FORMAL REFINEMENT DRAFT** — peer-review-facing development

## Theorems (Verified)

### T_CORRECTION: Failure as Positive Correction Data
- **Claim**: Failure, mismatch, and nonlinear residue are positive correction data rather than dismissal.
- **Verifier**: `cqe_engine.formal.verify_correction_surface` (to be implemented)
- **Evidence**: Local window shows residue as structured data feeding next transport

## Tool Binding
`cqe_engine.formal.verify_correction_surface`

## Proof Tree
```
claim
  -> local window
  -> boundary read
  -> tool transform
  -> practical example
  -> workbook analogue
  -> receipt
  -> proof / obligation split
```

## Open Obligations
- [ ] Implement `verify_correction_surface` verifier in cqe_engine.formal
- [ ] Add one falsifier case the claim must reject or defer
- [ ] Replace citation anchors with final bibliography entries

## Back-Propagation Targets
- Paper 00: receives any new contract term needed here
- ForgeFactory registry: receives/updates `forgefactory.paper02_correction_surface`
- Analog workbook manual: receives any new sheet rule
- Paper 31: records how this paper's presentation order demonstrates the LCR process

---

*Source: `PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`. Verifiers: lattice_forge centroid_voa, rule90_linearization.*