# Paper 07 — Tool: Discrete-Continuous Bridge Verifier

## Module
`cqe_engine.bridge`

## Public Surface
```python
from cqe_engine.bridge import (
    verify_bridge_exactness,
    interpolate_discrete_to_continuous,
    verify_rule90_linearization,
    BridgeInterpolator,
)
```

## Verifiers

### verify_bridge_exactness(max_depth=4096)
Verifies the discrete→continuous interpolation at every depth ≤ max_depth.
Returns: `{"status": "pass"|"fail", "total_depths": int, "max_error": Fraction, "claim": str}`
At max_depth=4096: 4096 depths, max_error = 0 (exact).

### verify_rule90_linearization()
Verifies Rule 30 = Rule 90 ⊕ correction at all 8 states + all depths.
Returns: `{"status": "pass", "identity_holds": True, "lucas_matches": True}`

### BridgeInterpolator
Interpolates discrete causal edges to continuous transport fields:
```python
interp = BridgeInterpolator()
field = interp.interpolate(causal_edge, resolution=0.001)
# field: continuous transport field
```

## CLI
```bash
python -m cqe_engine.bridge                          # runs verify_bridge_exactness
python -m cqe_engine.bridge interpolate 128          # bridge at depth 128
python -m cqe_engine.bridge l90                      # verifies R90 linearization
```

## Receipts
Written to `proof-receipts/CQE-paper-07/bridge-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-07",
  "theorems": ["T_BRIDGE", "T_R90_LINEARIZATION", "T_R30_DECOMP"],
  "all_passed": true,
  "max_interpolation_error": 0,
  "lucas_exactness": true
}
```

---

*This tool IS the proof of the bridge theorems. Running it discharges every Paper 07 obligation.*
