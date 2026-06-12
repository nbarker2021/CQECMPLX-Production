# Paper 04 — Workbook: Boundary Repair Sheet (v1 — isomorphic to tool)

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token | `verify_boundary_repair()` | `chart_state = (L,C,R)` |
| Detect failed join | `failed_join = detect_failure(state)` | `bool` |
| Convert to typed constraint | `constraint = repair(failed_join)` | `dict` |
| Feed to next transport | `next_transport(constraint)` | `bool` |

## Human Execution Protocol (Paper 04)
```
1. Roll 3d2 → (L,C,R)
2. Detect failed join (correction ≠ 0 with no next state)
3. Draw red X at failure point
4. Convert to typed constraint (black token)
5. Feed constraint to next transport
6. Receipt: boundary repaired
```

## Tool Execution Protocol (identical)
```python
# Uses verify_boundary_repair with lattice_forge primitives
```

## Receipt
```
boundary-repair-receipt =
  T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route.: T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route. ✓
  human_verifiable: true
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.

## Correction Note

Boundary repair does not mean "the failure is now proven." A repaired boundary
row is a typed constraint with state, axis/sheet coordinate, reason, status,
source, target, and next legal route. Untyped failures remain rejected.
