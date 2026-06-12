# Paper 11 — Tool: Theory Admission Gate Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.admission`

## Public Surface
```python
from cqe_engine.admission import (
    admit_theory,
    verify_admission,
    AdmissionGate,
)
```

## Verifiers

### admit_theory(theory_C, trusted_spectrum, K_max=9)
Filters external theory by Gluon mass:
```python
result = admit_theory(theory_C, trusted_spectrum)
# result: "admitted" | "boundary" | "rejected"
```

### verify_admission(gate, theory_list)
Batch admission verification:
```python
results = verify_admission(gate, [theory_A, theory_B, ...])
# Returns: List[{"theory": str, "result": "admitted|boundary|rejected", "C_mass": int}]
```

### AdmissionGate
```python
gate = AdmissionGate(trusted_spectrum=CmplxLookupCache)
gate.admit(theory_C)                    # single
gate.batch_verify([theory_A, ...])      # batch
gate.spectrum()                         # trusted spectrum
```

## CLI
```bash
python -m cqe_engine.admission theory_C.json           # single admission
python -m cqe_engine.admission --batch theories.json  # batch
python -m cqe_engine.admission --spectrum             # show trusted spectrum
```

## Receipts
Written to `proof-receipts/CQE-paper-11/admission-<theory>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-11",
  "theory": "External_Theory_X",
  "result": "admitted",
  "C_mass": 5,
  "K_window": 9,
  "trusted_match": true
}
```

---

*This tool IS the proof of the admission gate. Running it discharges every Paper 11 obligation.*
