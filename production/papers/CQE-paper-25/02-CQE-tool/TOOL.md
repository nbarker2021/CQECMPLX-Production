# Paper 25 — Tool: Energetic Traversal Maps Verifier

## Module
`cqe_engine.traversal`

## Public Surface
```python
from cqe_engine.traversal import (
    verify_oloid_winding_from_n,
    verify_oloid_rolling,
    verify_oloid_model_selection,
    TraversalGluon,
)
```

## Verifiers

### verify_oloid_winding_from_n()
Verifies traversal winding number.

### verify_oloid_rolling()
Verifies traversal rolling transport.

### verify_oloid_model_selection()
Verifies traversal model selector.

### TraversalGluon
```python
tg = TraversalGluon()
tg.winding(N)               # traversal winding number
tg.rolling_path()           # rolling transport
tg.energy_budget()          # energy cost
tg.geodesic()               # minimal energy path
```

## CLI
```bash
python -m cqe_engine.traversal                    # full verification
python -m cqe_engine.traversal winding            # winding number
python -m cqe_engine.traversal geodesic           # minimal energy path
```

## Receipts
Written to `proof-receipts/CQE-paper-25/traversal-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-25",
  "winding_numbers": "verified",
  "rolling_transport": "verified",
  "geodesic": "minimal energy path"
}
```

---

*This tool IS the proof of the traversal maps. Running it discharges every Paper 25 obligation.*
