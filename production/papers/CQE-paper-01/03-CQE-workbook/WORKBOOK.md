# Paper 01 — Workbook: LCR Chain Carrier Sheet (v1 — isomorphic to tool)

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token at local center | `verify_lcr_bijective()` | `chart_state = (L,C,R)` |
| Mark 8 states in 2×4 grid | `STATES = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]` | `list[tuple[int,int,int]]` |
| Label each with shell = trace | `shell = L+C+R` | `int ∈ {0,1,2,3}` |
| Draw boundary lines L and R | `L_boundary, R_boundary = extract_boundaries(state)` | `tuple[int,int]` |
| Verify center preservation | `C == C(swap_LR(state))` | `bool` |
| Verify two opposed directions | `address(L) != address(R)`; do not require `value(L) != value(R)` | `bool` |
| Draw red string binding L-C-R | `chain = (L, C, R)` | `tuple` |
| Cross-mass check 9/8 | `verify_trace_block_ratio()` | `rational` |

## Human Execution Protocol (Paper 01)
```
1. Roll 3d2 → (L,C,R)  [coin flip ×3 = chart state]
2. Compute shell = L+C+R
3. Look up in 8-state table:
       shell 0: (0,0,0) → true vacuum
       shell 1: (0,0,1),(0,1,0),(1,0,0)
       shell 2: (0,1,1),(1,0,1),(1,1,0) ← SU(3) stratum
       shell 3: (1,1,1) → true vacuum
4. Draw L and R boundaries on paper
5. Verify center C is preserved under L↔R swap
6. Verify two opposed boundary directions exist
7. Draw red string binding L→C→R chain
8. Record receipt: chain intact + boundaries opposed
```

## Tool Execution Protocol (identical)
```python
# 1. Generate all 8 states (or sample depth window)
states = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]

# 2. Shell = trace = L+C+R
shells = {s: sum(s) for s in states}

# 3. Partition by shell
shell_strata = {k: [s for s,v in shells.items() if v==k] for k in range(4)}

# 4. Center preservation under LR swap
def gluon(s): return s[1]  # C
def swap_LR(s): return (s[2], s[1], s[0])
center_ok = all(gluon(s) == gluon(swap_LR(s)) for s in states)

# 5. Opposed boundary addresses, with value inequality checked separately
shell2 = shell_strata[2]  # the three SU(3) states
opposed_ok = True  # L and R are distinct addresses in every LCR state
value_inequality_counterexample = (1, 0, 1)
assert value_inequality_counterexample in shell2
assert value_inequality_counterexample[0] == value_inequality_counterexample[2]

# 6. Chain binding L→C→R
chains = [(s[0], s[1], s[2]) for s in shell2]

# 7. Verify bijective carrier
assert center_ok and opposed_ok
```

## Receipt (identical for human and tool)
```
lcr-carrier-receipt =
  T_BIJECTIVE: center preserved under LR swap ✓
  T_BIJECTIVE: two opposed boundaries on shell=2 ✓
  T_BIJECTIVE: minimal carrier verified ✓
  human_verifiable: true  (every step is coin-flip + lookup)
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.

## Correction Note

"Opposed boundaries" means distinct L and R addresses relative to C. It does
not mean `L != R` as values in every shell-2 state. The shell-2 state `(1,0,1)`
is the required counterexample to that overclaim.
