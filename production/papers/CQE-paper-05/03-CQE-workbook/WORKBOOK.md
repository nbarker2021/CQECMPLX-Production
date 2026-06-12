# Paper 05 — Workbook: Oloid Path Carrier Sheet (v1 — isomorphic to tool)

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token | `verify_oloid_path()` | `chart_state = (L,C,R)` |
| Draw oloid rolling path | `oloid_path = rolling_path(state)` | `list[tuple]` |
| Verify continuity preserved | `continuous = check_continuity(path)` | `bool` |
| No straight-line requirement | `straight = False` | `bool` |

## Human Execution Protocol (Paper 05)
```
1. Roll 3d2 → (L,C,R)
2. Trace oloid rolling path (curved)
3. Verify continuity at each step
4. Note: no straight-line segments
5. Receipt: curved transport verified
```

## Tool Execution Protocol (identical)
```python
# Uses verify_oloid_path with lattice_forge primitives
```

## Receipt
```
oloid-path-carrier-receipt =
  T_OLOID_PATH: Curved/rolling carriers preserve continuity without straight-line transport.: T_OLOID_PATH: Curved/rolling carriers preserve continuity without straight-line transport. ✓
  human_verifiable: true
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.

## Scope Note

This workbook verifies structural rolling continuity. It does not prove that
the Oloid carrier predicts Rule 30 future bits without enumeration. Prediction
remains a separate open obligation until its own verifier closes it.
