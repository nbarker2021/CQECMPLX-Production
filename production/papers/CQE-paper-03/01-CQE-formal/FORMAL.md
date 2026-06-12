# Paper 03 — D4/J3 Triality

## Central Thesis

Represent axis/sheet labeling, rotation/reflection equivalence, and Jordan carrier behavior as the first explicit triality surface.

## Status

**FORMAL REFINEMENT DRAFT** — peer-review-facing development

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
  -> supplemental workbook analogue
  -> receipt
  -> proof result / audit residue split
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