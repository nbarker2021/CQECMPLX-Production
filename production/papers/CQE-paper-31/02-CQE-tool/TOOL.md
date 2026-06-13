# Paper 31 — Tool: Meta LCR Enactment Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.meta_lcr`

## Public Surface
```python
from cqe_engine.meta_lcr import (
    verify_meta_lcr,
    verify_hamiltonian_corpus,
    MetaLCRGluon,
)
```

## Verifiers

### verify_meta_lcr()
Verifies the 31-paper corpus as enacted LCR process:
```python
result = verify_meta_lcr()
# Returns: {"status": "pass", "papers": 31, "enacted_LCR": True, "root_hash": str}
```

### verify_hamiltonian_corpus()
Verifies Hamiltonian windows across all 31 papers as meta-walkthrough.

### MetaLCRGluon
```python
mlg = MetaLCRGluon()
mlg.enactment()               # the 31-paper walkthrough
mlg.grand_ribbon()            # Paper 30 as object
mlg.actor_object_distinction() # LCR distinction
mlg.meta_receipt()            # final certificate
```

## CLI
```bash
python -m cqe_engine.meta_lcr                    # full verification
python -m cqe_engine.meta_lcr hamiltonian       # Hamiltonian corpus
python -m cqe_engine.meta_lcr enactment         # enacted LCR
```

## Receipts
Written to `proof-receipts/CQE-paper-31/meta-lcr-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-31",
  "enacted_LCR": true,
  "papers": 31,
  "grand_ribbon": "Paper 30",
  "actor_object_distinction": "verified",
  "meta_receipt": "issued"
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
