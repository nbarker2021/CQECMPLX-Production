# Paper 00 — Workbook: Foundation Sheet (v2 — isomorphic to tool)

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token at local center | `verify_T3_chart_j3o_isomorphism()` | `chart_state = (L,C,R)` |
| Mark 8 states in 2×4 grid | `STATES = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]` | `list[tuple[int,int,int]]` |
| Label each with shell = trace | `shell = L+C+R` | `int ∈ {0,1,2,3}` |
| Draw red φ arrow to J₃(O) diag | `phi = diag(L,C,R)` | `J3O_diagonal` |
| Green highlight shell=2 row | `LIE_CONJUGATES = frozenset({(0,1,1),(1,0,1),(1,1,0)})` | `frozenset` |
| Write M₃ matrix with 1/3 entries | `verify_T4_n3_closure_exact()` → `M3 = ⅓(T₁₂+T₁₃+T₂₃)` | `Matrix over ℚ` |
| Circle M₃²=M₃ | `verify_T5_M3_idempotent()` | `bool` |
| Write cross-mass 9/8 | `verify_T6_trace_blocks()` | `rational` |
| Write 8×8 entries {0,¼,½} | `verify_T7_8x8_transition_exact()` | `Matrix over ℚ` |

## Human Execution Protocol (Paper 00)
```
1. Roll 3d2 → (L,C,R)  [coin flip ×3 = chart state]
2. Compute shell = L+C+R  [sum of bits]
3. Look up in 8-state table:
       shell 0: (0,0,0) → true vacuum
       shell 1: (0,0,1),(0,1,0),(1,0,0)
       shell 2: (0,1,1),(1,0,1),(1,1,0) ← SU(3) stratum
       shell 3: (1,1,1) → true vacuum
4. Trace φ(L,C,R) = diag(L,C,R) on J₃(O) paper
5. Verify M₃ = ⅓(T₁₂+T₁₃+T₂₃) by counting transitions
6. Verify M₃² = M₃ by squaring
7. Verify trace-block identity by comparing blocks
8. Verify 8×8 entries ∈ {0,¼,½}
```

## Tool Execution Protocol (identical)
```python
# 1. Generate all 8 states (or sample 4096 depth window)
states = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]

# 2. Shell = trace = L+C+R
shells = {s: sum(s) for s in states}

# 3. Partition by shell
shell_strata = {k: [s for s,v in shells.items() if v==k] for k in range(4)}

# 4. φ: chart → J₃(O) diagonal
def phi(s): return diag(*s)

# 5. Verify T4: compute 3-step transitions on shell=2
M3 = compute_M3(shell_strata[2])  # exactly ⅓(T₁₂+T₁₃+T₂₃)

# 6. Verify T5: M3 @ M3 == M3 over ℚ

# 7. Verify T6: trace-1 block == trace-2 block

# 8. Verify T7: 8×8 entries in {0, 1/4, 1/2}
```

## Receipt (identical for human and tool)
```
foundation-receipt =
  T3: 8 states bijection ✓
  T4: M3 exact ℚ ✓
  T5: M3²=M3 ✓
  T6: blocks identical ✓
  T7: entries {0,¼,½} ✓
  human_verifiable: true  (every step is a coin-flip + lookup)
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.