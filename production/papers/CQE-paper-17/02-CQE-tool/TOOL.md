# Paper 17 — Tool: E6-E8 Error-Correction Tower Verifier

## Module
`cqe_engine.tower`

## Public Surface
```python
from cqe_engine.tower import (
    verify_tower_gluon,
    verify_glue_vectors,
    TowerGluon,
)
```

## Verifiers

### verify_tower_gluon()
Verifies Gluon transport up E6→E7→E8 tower:
```python
result = verify_tower_gluon()
# Returns: {"status": "pass", "levels": ["E6","E7","E8"], "C_E8_dim": 248}
```

### verify_glue_vectors()
Verifies E6→E7→E8 glue vectors from `g2_f4_t5_conjugate`.

### TowerGluon
```python
tower = TowerGluon()
tower.C_E6()          # E6 Gluon
tower.C_E7()          # E7 Gluon
tower.C_E8()          # E8 Gluon (dim 248)
tower.transport_E6_E7()  # C_E7 = C_E6 ⊕ corr_E6
tower.transport_E7_E8()  # C_E8 = C_E7 ⊕ corr_E7
tower.C_E8_dim()      # 248
```

## CLI
```bash
python -m cqe_engine.tower                        # full verification
python -m cqe_engine.tower glue                    # glue vectors
python -m cqe_engine.tower E8                      # E8 verification
```

## Receipts
Written to `proof-receipts/CQE-paper-17/tower-<level>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-17",
  "tower_verified": ["E6","E7","E8"],
  "C_E8_dim": 248,
  "glue_vectors_valid": true,
  "Z4_wrap": true
}
```

---

*This tool IS the proof of the tower theorems. Running it discharges every Paper 17 obligation.*
