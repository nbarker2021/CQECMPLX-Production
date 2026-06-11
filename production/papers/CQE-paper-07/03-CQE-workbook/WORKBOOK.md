# Paper 07 — Workbook: Discrete-Continuous Bridge Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Plot discrete points | `BridgeInterpolator()` | `List[Tuple[depth, value]]` |
| Draw interpolating curve | `interpolate_discrete_to_continuous()` | `ContinuousField` |
| Mark Rule 90 base | `lucas_bit(N, 0)` | `int` |
| Mark correction bits | `correction(L,C,R)` | `int (0|1)` |
| Draw interpolation kernel | `lucas_bit ⊕ correction` | `ContinuousField` |
| Verify exactness | `verify_bridge_exactness()` | `{"max_error": 0}` |

## Human Execution Protocol (Paper 07)
```
1. Draw discrete causal edges from Paper 06 on grid
2. At each depth, compute lucas_bit(N, 0) → base field
3. At each site, compute correction = C ∧ ¬R
4. Overlay: base ⊕ correction = Rule 30 field
5. Verify: discrete points exactly match continuous interpolation
```

## Tool Execution Protocol (identical)
```python
# 1. Build discrete field from Paper 06
discrete = Paper06.causal_field()

# 2. Interpolate
interp = BridgeInterpolator()
continuous = interp.interpolate(discrete)

# 3. Verify exactness at all depths
result = verify_bridge_exactness(4096)
assert result["max_error"] == Fraction(0, 1)
```

## Receipt (identical)
```
bridge-receipt =
  depths_checked: 4096
  max_interpolation_error: 0
  r30_decomposition: exact
  lucas_matches_r90: true
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
