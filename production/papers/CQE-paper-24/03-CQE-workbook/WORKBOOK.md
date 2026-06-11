# Paper 24 — Workbook: KnightForge / N-Dimensional Chess Automata Sheet

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
