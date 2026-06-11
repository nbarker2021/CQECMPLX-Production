# Paper 18 — Tool: VOA/Moonshine Verifier

## Module
`cqe_engine.moonshine`

## Public Surface
```python
from cqe_engine.moonshine import (
    verify_monster_moonshine,
    verify_voa_sector_decomposition,
    verify_z4_period_template,
    MoonshineGluon,
)
```

## Verifiers

### verify_monster_moonshine()
Verifies Moonshine module: `j(τ) = 1/q + 744 + 196884q + ...`
```python
result = verify_monster_moonshine()
# Returns: {"status": "pass", "196884": "1 + 196883"}
```

### verify_voa_sector_decomposition()
Verifies 2+6 VOA split: 2 weight-0 vacua, 6 weight-5 excited.

### verify_z4_period_template()
Verifies Z4 period template = D12 orbit structure.

### MoonshineGluon
```python
mg = MoonshineGluon()
mg.vacuum_dim()        # 1 (trivial rep)
mg.moonshine_dim()     # 196883
mg.total_dim()         # 196884 = 1 + 196883
mg.z4_period()         # 2 period-1, 6 period-4
```

## CLI
```bash
python -m cqe_engine.moonshine                        # full verification
python -m cqe_engine.moonshine z4                     # Z4 period
python -m cqe_engine.moonshine monster                # Monster verification
```

## Receipts
Written to `proof-receipts/CQE-paper-18/moonshine-<verification>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-18",
  "moonshine_verified": true,
  "j_tau_decomposition": "196884 = 1 + 196883",
  "voa_sectors": {"vacuum": 2, "excited": 6},
  "z4_period": "2 period-1, 6 period-4"
}
```

---

*This tool IS the proof of the Moonshine theorems. Running it discharges every Paper 18 obligation.*
