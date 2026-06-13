# Paper 26 — Tool: Z-Pinch and Shear Horizon Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.zpinch`

## Public Surface
```python
from cqe_engine.zpinch import (
    verify_oloid_winding_from_n,
    verify_oloid_rolling,
    verify_oloid_model_selection,
    ZPinchGluon,
)
```

## Verifiers

### verify_oloid_winding_from_n()
Verifies pinch winding number.

### verify_oloid_rolling()
Verifies pinch rolling transport.

### verify_oloid_model_selection()
Verifies pinch model selector.

### ZPinchGluon
```python
zpg = ZPinchGluon()
zpg.winding(N)              # pinch winding number
zpg.rolling_transport()     # rolling transport
zpg.shear_components()      # off-diagonal shear
zpg.mirror_partner()        # -k partner
```

## CLI
```bash
python -m cqe_engine.zpinch                    # full verification
python -m cqe_engine.zpinch winding            # pinch winding
python -m cqe_engine.zpinch shear              # shear components
```

## Receipts
Written to `proof-receipts/CQE-paper-26/zpinch-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-26",
  "pinch_winding": "verified",
  "rolling_transport": "verified",
  "shear_components": "off-diagonal"
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
