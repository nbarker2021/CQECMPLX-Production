# Paper 28 — Tool: N-Dimensional Game Lattices Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.game_lattice`

## Public Surface
```python
from cqe_engine.game_lattice import (
    verify_lattice_code_chain,
    verify_oloid_model_selection,
    verify_oloid_closure,
    GameLatticeGluon,
)
```

## Verifiers

### verify_lattice_code_chain()
Verifies powered lattice chain for N-dim board: 1→9→49→72.

### verify_oloid_model_selection()
Verifies move/model selector.

### verify_oloid_closure()
Verifies move closure verifier.

### GameLatticeGluon
```python
glg = GameLatticeGluon(dimensions=N)
glg.board()                   # N-dim lattice
glg.move_set()                # N-dim moves (L-conjugate generalized)
glg.lattice_chain()           # 1→9→49→72...
glg.verify_oloid_closure()    # move closure
```

## CLI
```bash
python -m cqe_engine.game_lattice                    # full verification
python -m cqe_engine.game_lattice dimensions 4      # 4D board
python -m cqe_engine.game_lattice l_conjugate       # generalized L-move
```

## Receipts
Written to `proof-receipts/CQE-paper-28/game-lattice-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-28",
  "dimensions": 4,
  "lattice_chain": "1→9→49→72",
  "l_conjugate_move": "verified",
  "move_closure": "verified"
}
```

---

*This tool IS the proof of the N-dimensional game lattices. Running it discharges every Paper 28 obligation.*
