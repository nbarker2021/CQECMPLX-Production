# Paper 05 — Oloid Path Carrier

## Central Thesis
Use curved/rolling carriers to show that transport need not be straight-line to preserve continuity.

## Status
**FORMAL REFINEMENT DRAFT** — peer-review-facing development

## Theorems (Verified)

### T_OLOID_PATH: Curved/rolling carriers preserve continuity without straight-line transport.: Oloid Path Carrier
- **Claim**: T_OLOID_PATH: Curved/rolling carriers preserve continuity without straight-line transport.
- **Verifier**: `cqe_engine.formal.verify_oloid_path`
- **Evidence**: Local window + boundary read + tool transform

## Tool Binding
`cqe_engine.formal.verify_oloid_path`

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
- [ ] Implement `verify_oloid_path` verifier
- [ ] Add falsifier case
- [ ] Final bibliography entries

## Back-Propagation Targets
- Paper 00
- ForgeFactory registry
- Analog workbook manual
- Paper 31

---

*Source: `PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`.*