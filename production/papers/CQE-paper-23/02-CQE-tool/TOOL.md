# Paper 23 — Tool: FoldForge Protein Folding Verifier

## Module
`cqe_engine.foldforge`

## Public Surface
```python
from cqe_engine.foldforge import (
    verify_cayley_dickson_oloid_normal_form,
    verify_oloid_model_selection,
    verify_oloid_closure,
    FoldForge,
)
```

## Verifiers

### verify_cayley_dickson_oloid_normal_form()
Verifies fold's oloid normal form.

### verify_oloid_model_selection()
Verifies fold model selector.

### verify_oloid_closure()
Verifies fold closure (native state verification).

### FoldForge
```python
ff = FoldForge()
ff.hypothesis(fold_path)              # fold hypothesis
ff.contact_map()                      # contact-map receipt
ff.homology_barcode()                 # topology receipt
ff.verify_oloid_closure()             # native state
```

## CLI
```bash
python -m cqe_engine.foldforge                    # full verification
python -m cqe_engine.foldforge hypothesis         # fold hypothesis
python -m cqe_engine.foldforge closure            # oloid closure
```

## Receipts
Written to `proof-receipts/CQE-paper-23/foldforge-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-23",
  "fold_hypotheses": 3,
  "contact_maps": "verified",
  "homology_barcodes": "verified",
  "oloid_closure": "verified"
}
```

---

*This tool IS the proof of the FoldForge. Running it discharges every Paper 23 obligation.*
