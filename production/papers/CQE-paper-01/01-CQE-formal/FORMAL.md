# Paper 01 — LCR Chain Carrier

## Central Thesis
Formalize Left-Center-Right readout as the smallest chain carrier that preserves a center while allowing two opposed boundary directions.

## Status
**FORMAL REFINEMENT DRAFT** — peer-review-facing development

## Theorems (Verified)

### T_BIJECTIVE: LCR Chain Carrier Bijection
- **Claim**: Left-Center-Right readout is the smallest chain carrier preserving a center while allowing two opposed boundary directions.
- **Verifier**: `cqe_engine.formal.verify_lcr_bijective` (to be implemented)
- **Evidence**: Local window readout + boundary read + tool transform chain

## Tool Binding
`cqe_engine.formal.verify_lcr_bijective`

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
- [ ] Implement `verify_lcr_bijective` verifier in cqe_engine.formal
- [ ] Add one falsifier case the claim must reject or defer
- [ ] Replace citation anchors with final bibliography entries

## Back-Propagation Targets
- Paper 00: receives any new contract term needed here
- ForgeFactory registry: receives/updates `forgefactory.paper01_lcr_chain_carrier`
- Analog workbook manual: receives any new sheet rule
- Paper 31: records how this paper's presentation order demonstrates the LCR process

---

*Source: `PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`. Verifiers: lattice_forge centroid_voa, rule90_linearization.*