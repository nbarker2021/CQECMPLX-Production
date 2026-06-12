# Paper 19 — Tool: Observer Face-Selection Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.observer`

## Public Surface
```python
from cqe_engine.observer import (
    verify_face_selection,
    verify_z4_face_cycle,
    ObserverGluon,
)
```

## Verifiers

### verify_face_selection()
Verifies face selection operator:
```python
result = verify_face_selection()
# Returns: {"status": "pass", "faces": 4, "selected": 1, "latent": 3}
```

### verify_z4_face_cycle()
Verifies Z4 face cycle: Frame 0→1→2→3→0.

### ObserverGluon
```python
og = ObserverGluon()
og.select_face(0)        # C-centroid
og.select_face(1)        # R-centroid
og.select_face(2)        # C-flipped
og.select_face(3)        # L-centroid
og.latent_faces()        # 3 unselected faces = obligations
```

## CLI
```bash
python -m cqe_engine.observer                     # full verification
python -m cqe_engine.observer cycle               # Z4 face cycle
python -m cqe_engine.observer face 0              # specific face
```

## Receipts
Written to `proof-receipts/CQE-paper-19/observer-<face>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-19",
  "face_selection": true,
  "z4_cycle_verified": true,
  "selected_face": 1,
  "latent_obligations": 3
}
```

---

*This tool IS the proof of the observer face-selection. Running it discharges every Paper 19 obligation.*
