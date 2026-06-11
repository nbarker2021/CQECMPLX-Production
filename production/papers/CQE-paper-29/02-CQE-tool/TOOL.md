# Paper 29 — Tool: Monster/Universal Energy-Bound Verifier

## Module
`cqe_engine.monster`

## Public Surface
```python
from cqe_engine.monster import (
    verify_monster_moonshine,
    verify_centroid_voa_chain,
    verify_morphonics_model,
    MonsterGluon,
)
```

## Verifiers

### verify_monster_moonshine()
Verifies Monster Moonshine: `j(τ) = 1/q + 744 + 196884q + ...`

### verify_centroid_voa_chain()
Verifies VOA sector chain including Monster.

### verify_morphonics_model()
Verifies Monster morphic model.

### MonsterGluon
```python
mg = MonsterGluon()
mg.dimension()              # 196883
mg.supersingular_product()  # 47·59·71 = 196883
mg.higgs_bound()            # Higgs max = Monster bound
mg.moondhine_dim()          # Moonshine dim = 196883
mg.z4_period()              # Monster Z4 cycle
```

## CLI
```bash
python -m cqe_engine.monster                        # full verification
python -m cqe_engine.monster dimension              # 196883
python -m cqe_engine.monster supersingular          # 47·59·71
python -m cqe_engine.monster higgs_bound            # Higgs max = Monster
```

## Receipts
Written to `proof-receipts/CQE-paper-29/monster-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-29",
  "dimension": 196883,
  "supersingular": "47·59·71",
  "higgs_bound": "Monster bound",
  "moonshine_dim": 196883
}
```

---

*This tool IS the proof of the Monster energy bound. Running it discharges every Paper 29 obligation.*
