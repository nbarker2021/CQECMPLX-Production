# Paper 10 — Tool: T10 Master Receipt Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.master_receipt`

## Public Surface
```python
from cqe_engine.master_receipt import (
    compose_master_receipt,
    verify_master_receipt,
    MasterReceipt,
)
```

## Verifiers

### compose_master_receipt(papers: List[int] = range(10))
Composes master receipt from papers 00-09:
```python
receipt = compose_master_receipt(range(10))
# receipt.C = XOR of all 10 paper C-forms
```

### verify_master_receipt(receipt)
Verifies:
- All 10 papers have valid receipts
- XOR composition is correct
- No missing obligations
- C_accumulated = C₀ ⊕ C₁ ⊕ ... ⊕ C₉

### MasterReceipt
```python
mr = MasterReceipt()
mr.papers                      # [0..9]
mr.C_accumulated               # XOR of all C_i
mr.verify()                    # → {"valid": True}
```

## CLI
```bash
python -m cqe_engine.master_receipt                  # compose + verify
python -m cqe_engine.master_receipt verify           # verify existing
python -m cqe_engine.master_receipt 0 1 2 3 4 5 6 7 8 9  # custom papers
```

## Receipts
Written to `proof-receipts/CQE-paper-10/master-receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-10",
  "composed_papers": [0,1,2,3,4,5,6,7,8,9],
  "C_accumulated": "XOR_of_all_C_forms",
  "all_obligations_resolved": true,
  "valid": true
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
