# Paper 24 — Workbook: KnightForge / N-Dimensional Chess Automata Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw N-dim board | `KnightForge(dimensions=N).board()` | `N-dim lattice` |
| Draw L-conjugate move | `kf.move_set()` | `L-conjugate moves` |
| Draw powered chain | `verify_lattice_code_chain()` | `1→9→49→72` |
| Verify closure | `verify_oloid_closure()` | `move closure` |

## Human Execution Protocol (Paper 24)

```
1. Draw N-dim board: 1D→2D→4D→6D (1→9→49→72)
2. Place knight piece (L-conjugate)
3. Draw move set: L-conjugate moves
4. Verify move closure
```

## Tool Execution Protocol (identical)

```python
kf = KnightForge(dimensions=2)
moves = kf.move_set()
assert verify_lattice_code_chain()  # 1→9→49→72

assert kf.verify_oloid_closure()
```

## Receipt (identical)

```
knightforge-receipt =
  dimensions: 2
  l_conjugate_move: verified
  powered_chain: 1→9→49→72 ✓
  move_closure: verified
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
