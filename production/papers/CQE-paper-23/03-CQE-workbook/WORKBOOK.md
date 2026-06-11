# Paper 23 — Workbook: FoldForge Protein Folding Sheet

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

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
