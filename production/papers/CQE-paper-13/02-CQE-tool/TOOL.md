# Paper 13 — Tool: Quark-Face Transport Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.quark_face`

## Public Surface
```python
from cqe_engine.quark_face import (
    verify_color_transport,
    verify_chirality_cipher,
    QuarkFaceTransport,
)
```

## Verifiers

### verify_color_transport()
Verifies color transport across 6 quark faces:
```python
result = verify_color_transport()
# Returns: {"status": "pass", "faces": 6, "gluon_mediated": True}
```

### verify_chirality_cipher()
Verifies color chirality cipher (Paper 13 Theorem A).

### QuarkFaceTransport
```python
transport = QuarkFaceTransport()
transport.transport_face("R", "G")     # R → G via gluon
transport.color_charge("R")            # R = +1, anti-R = -1
transport.verify_su3_cycle()           # R→G→B→R Z3 cycle
```

## CLI
```bash
python -m cqe_engine.quark_face                    # full verification
python -m cqe_engine.quark_face transport R G      # R → G transport
python -m cqe_engine.quark_face chirality          # chirality cipher
```

## Receipts
Written to `proof-receipts/CQE-paper-13/quark-face-<face>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-13",
  "faces_transported": 6,
  "su3_cycle_verified": true,
  "color_charge_conserved": true,
  "gluon_mediated": true
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
