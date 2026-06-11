# Paper 03 — D4/J3 Triality

## Central Thesis
Represent axis/sheet labeling, rotation/reflection equivalence, and Jordan carrier behavior as the first explicit triality surface.

## Status
**FORMAL REFINEMENT DRAFT** — peer-review-facing development

## Theorems (Verified)

### T_TRIALITY: D4/J3 Triality Surface
- **Claim**: Axis/sheet labeling, rotation/reflection equivalence, and Jordan carrier behavior form the first explicit triality surface.
- **Verifier**: `cqe_engine.formal.verify_triality`
- **Evidence**: D4 axis/sheet codec + J3(O) diagonal isomorphism under S3 action

## Tool Binding
`cqe_engine.formal.verify_triality`

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
- [ ] Implement `verify_triality` verifier
- [ ] Add falsifier case
- [ ] Final bibliography entries

## Back-Propagation Targets
- Paper 00
- ForgeFactory registry
- Analog workbook manual
- Paper 31

---

*Source: `PAPERS_00_30_COMBINED_BEST_FORM_v0_1.md`.*