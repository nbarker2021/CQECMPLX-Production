# Paper 09 — Tool: Hamiltonian Window Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.hamiltonian`

## Public Surface
```python
from cqe_engine.hamiltonian import (
    iterative_hamiltonian,
    hamiltonian_read,
    BASE_C_FORMS,
    HamiltonianWindow,
)
```

## Verifiers

### iterative_hamiltonian(c_forms, order=2)
Runs 1-3 bar (2nd order), 1-5 bar (3rd), 1-7 bar (4th) Hamiltonian readings.
Returns: `{"status": "pass", "order": int, "windows": List[WindowRead], "global_C": str}`

### hamiltonian_read(order, c_sequence)
Single-window evaluator at given order (2=1-3, 3=1-5, 4=1-7).
Carries forward through sliding windows, reads backward to validate.

### BASE_C_FORMS
The 6 C-forms from Papers 0-5 for iterative Hamiltonian windows.

## CLI
```bash
python -m cqe_engine.hamiltonian                    # runs iterative_hamiltonian (order 2)
python -m cqe_engine.hamiltonian 3                  # 3rd order (1-5 bar)
python -m cqe_engine.hamiltonian 4                  # 4th order (1-7 bar)
```

## Receipts
Written to `proof-receipts/CQE-paper-09/hamiltonian-<order>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-09",
  "order": 2,
  "windows": 4,
  "global_C": "C_accumulated_XOR_chain",
  "all_validated": true
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
