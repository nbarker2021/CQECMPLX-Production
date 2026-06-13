# Paper 30 — Tool: Grand Ribbon Meta-Framer Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.grand_ribbon`

## Public Surface
```python
from cqe_engine.grand_ribbon import (
    verify_grand_ribbon,
    verify_hamiltonian_corpus,
    GrandRibbonGluon,
)
```

## Verifiers

### verify_grand_ribbon()
Verifies the 31-paper corpus as single LCR ribbon:
```python
result = verify_grand_ribbon()
# Returns: {"status": "pass", "beads": 31, "sequence": "LCR", "root_hash": str}
```

### verify_hamiltonian_corpus()
Verifies Hamiltonian windows across all 31 papers.

### GrandRibbonGluon
```python
grg = GrandRibbonGluon()
grg.sequence()                # [C_0, C_1, ..., C_30]
grg.root_hash()               # hash(⊕ C_i)
grg.lcr_sequence()            # "LCR" per paper
grg.meta_framer()             # Paper 31 meta-coupling
```

## CLI
```bash
python -m cqe_engine.grand_ribbon                    # full verification
python -m cqe_engine.grand_ribbon hamiltonian       # Hamiltonian corpus
python -m cqe_engine.grand_ribbon sequence          # C-sequence
```

## Receipts
Written to `proof-receipts/CQE-paper-30/grand-ribbon-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-30",
  "beads": 31,
  "sequence": "LCR",
  "root_hash": "hash(⊕ C₀⋯C₃₀)",
  "sequence_verified": true
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
