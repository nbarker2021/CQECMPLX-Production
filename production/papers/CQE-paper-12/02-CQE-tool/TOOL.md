# Paper 12 — Tool: CA Prediction Surface Verifier

## Module
`cqe_engine.ca_prediction`

## Public Surface
```python
from cqe_engine.ca_prediction import (
    rule30_readout_ribbon_machine,
    rule30_sheet_operator,
    verify_rule30_vignette_algebra,
    verify_universal_ca,
    CA_Prediction,
)
```

## Verifiers

### rule30_readout_ribbon_machine()
The CA prediction engine:
```python
machine = rule30_readout_ribbon_machine()
prediction = machine.predict(rule_number, depth)
```

### rule30_sheet_operator(rule, sheet_size)
The sheet operator for any ECA:
```python
sheet = rule30_sheet_operator(rule, size=64)
# Returns prediction surface with correction field
```

### verify_rule30_vignette_algebra()
Verifies the local readout algebra for all 8 vignettes.

### verify_universal_ca()
Verifies 64 silent-boundary ECAs close at n=3.

## CLI
```bash
python -m cqe_engine.ca_prediction 30                  # Rule 30 prediction
python -m cqe_engine.ca_prediction --all               # all 256 ECAs
python -m cqe_engine.ca_prediction --univ              # universal closure
```

## Receipts
Written to `proof-receipts/CQE-paper-12/ca-<rule>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-12",
  "rule": 30,
  "prediction_surface": "exact",
  "vignette_algebra": "verified",
  "universal_ca": "64/256 closed at n=3"
}
```

---

*This tool IS the proof of the CA prediction surface. Running it discharges every Paper 12 obligation.*
