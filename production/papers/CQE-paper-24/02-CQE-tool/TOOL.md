# Paper 24 — Tool: KnightForge / N-Dimensional Chess Automata Verifier

## Module
`cqe_engine.knightforge`

## Public Surface
```python
from cqe_engine.knightforge import (
    verify_lattice_code_chain,
    verify_oloid_model_selection,
    verify_oloid_closure,
    KnightForge,
)
```

## Verifiers

### verify_lattice_code_chain()
Verifies powered lattice chain: 1→9→49→72 for N-dim board.

### verify_oloid_model_selection()
Verifies move model selector.

### verify_oloid_closure()
Verifies move closure verifier.

### KnightForge
```python
kf = KnightForge(dimensions=N)
kf.piece("knight")              # knight piece
kf.move_set()                   # L-conjugate moves
kf.board(dimensions)            # N-dim board (powered lattice)
kf.verify_oloid_closure()       # move closure
```

## CLI
```bash
python -m cqe_engine.knightforge                    # full verification
python -m cqe_engine.knightforge dimensions 2       # 2D chess
python -m cqe_engine.knightforge l_conjugate        # L-conjugate move
```

## Receipts
Written to `proof-receipts/CQE-paper-24/knightforge-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-24",
  "dimensions": 2,
  "l_conjugate_move": "verified",
  "powered_chain": "1→9→49→72",
  "move_closure": "verified"
}
```

---

*This tool IS the proof of the KnightForge. Running it discharges every Paper 24 obligation.*
