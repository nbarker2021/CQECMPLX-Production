# Paper 24 — Tool: KnightForge / N-Dimensional Chess Automata Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
