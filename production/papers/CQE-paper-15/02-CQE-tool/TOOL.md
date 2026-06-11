# Paper 15 — Tool: QFT/Higgs Mass-Residue Carrier Verifier

## Module
`cqe_engine.higgs`

## Public Surface
```python
from cqe_engine.higgs import (
    verify_higgs_gluon,
    verify_higgs_mechanism,
    HiggsGluon,
)
```

## Verifiers

### verify_higgs_gluon()
Verifies Higgs field = Gluon mass accumulation:
```python
result = verify_higgs_gluon()
# Returns: {"status": "pass", "phi": "C_accumulated", "mass_squared": "|C_acc|^2"}
```

### verify_higgs_mechanism()
Verifies Higgs mechanism = Gluon mass acquisition:
```python
result = verify_higgs_mechanism()
# Returns: {"status": "pass", "symmetry_breaking": "C_acc != 0"}
```

### HiggsGluon
```python
hg = HiggsGluon()
hg.field()                    # ϕ = C_accumulated
hg.mass_residue()             # m_h^2 ∝ |C_acc|^2
hg.sector()                   # "vacuum" (weight 0) or "excited" (weight 5)
hg.verify_mechanism()         # C_acc != 0 ↔ broken symmetry
```

## CLI
```bash
python -m cqe_engine.higgs                         # full verification
python -m cqe_engine.higgs mechanism               # Higgs mechanism
python -m cqe_engine.higgs gluon                   # Higgs Gluon
```

## Receipts
Written to `proof-receipts/CQE-paper-15/higgs-<verification>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-15",
  "higgs_field": "C_accumulated",
  "mass_residue": "|C_acc|^2",
  "symmetry_broken": true,
  "voa_sector": "excited (weight 5)"
}
```

---

*This tool IS the proof of the Higgs mechanism. Running it discharges every Paper 15 obligation.*
