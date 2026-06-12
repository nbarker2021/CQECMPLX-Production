# Paper 20 — Tool: Layer-2 Synthesis Ledger Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.synthesis`

## Public Surface
```python
from cqe_engine.synthesis import (
    verify_synthesis_ledger,
    verify_gluon_synthesis,
    SynthesisLedger,
)
```

## Verifiers

### verify_synthesis_ledger()
Verifies synthesis ledger for papers 00-19:
```python
result = verify_synthesis_ledger()
# Returns: {"status": "pass", "papers": 20, "root_hash": "hash(⊕ C_i)"}
```

### verify_gluon_synthesis()
Verifies synthesis Gluon = hash(⊕ C_i):
```python
result = verify_gluon_synthesis()
# Returns: {"status": "pass", "root_hash": str, "all_C_i_verified": True}
```

### SynthesisLedger
```python
ledger = SynthesisLedger()
ledger.add_paper(0, C_0)
# ... add all 20
ledger.root_hash()           # hash(⊕ C_i)
ledger.verify_all()          # all receipts valid
```

## CLI
```bash
python -m cqe_engine.synthesis                    # full verification
python -m cqe_engine.synthesis hash               # root hash only
python -m cqe_engine.synthesis verify             # full verification
```

## Receipts
Written to `proof-receipts/CQE-paper-20/synthesis-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-20",
  "papers_synthesized": 20,
  "root_hash": "hash(⊕ C₀⋯C₁₉)",
  "all_verified": true
}
```

---

*This tool IS the proof of the synthesis ledger. Running it discharges every Paper 20 obligation.*
