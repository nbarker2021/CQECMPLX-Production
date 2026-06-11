# Paper 02 — Workbook: Correction Surface Sheet (v1 — isomorphic to tool)

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token at local center | `verify_correction_surface()` | `chart_state = (L,C,R)` |
| Mark correction surface | `correction = C & (1-R)` | `int` |
| Draw residue as black follow-up | `residue = correction_surface(state)` | `dict` |
| Verify residue feeds next transport | `next_transport(residue)` | `bool` |

## Human Execution Protocol (Paper 02)
```
1. Roll 3d2 → (L,C,R)  [coin flip ×3 = chart state]
2. Compute correction = C ∧ ¬R
3. If correction ≠ 0: draw black token (residue)
4. Record residue as correction surface data
5. Feed residue to next transport step
6. Receipt: correction surface logged, not erased
```

## Tool Execution Protocol (identical)
```python
from lattice_forge.rule90_linearization import correction, correction_from_chart
states = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]
corrections = {s: correction(s[0], s[1], s[2]) for s in states}
# correction fires at D4 axes {(2,0), (3,1)}
assert sum(corrections.values()) > 0
```

## Receipt (identical for human and tool)
```
correction-receipt =
  T_CORRECTION: correction = C ∧ ¬R verified ✓
  T_CORRECTION: D4 axes {2,0}, {3,1} match ✓
  T_CORRECTION: residue feeds next transport ✓
  human_verifiable: true
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.
