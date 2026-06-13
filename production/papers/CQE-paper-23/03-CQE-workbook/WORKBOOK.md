# Paper 23 — Workbook: FoldForge Protein Folding Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Propose fold | `FoldForge().hypothesis(fold_path)` | `FoldHypothesis` |
| Draw contact map | `FoldForge().contact_map()` | `ContactMap` |
| Draw homology barcode | `FoldForge().homology_barcode()` | `Barcode` |
| Verify closure | `verify_oloid_closure()` | `bool` |

## Human Execution Protocol (Paper 23)

```
1. Propose fold hypothesis (amino acid sequence)
2. Draw contact map: residue i ↔ residue j
3. Compute homology barcode (persistent homology)
4. Verify oloid closure: native state = oloid midpoint
```

## Tool Execution Protocol (identical)

```python
ff = FoldForge()
hyp = ff.hypothesis(path)
cm = ff.contact_map()
hb = ff.homology_barcode()
assert ff.verify_oloid_closure()
```

## Receipt (identical)

```
foldforge-receipt =
  hypotheses: 3
  contact_maps: verified
  homology_barcodes: verified
  oloid_closure: verified
  human_verifiable: true
```

---

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
