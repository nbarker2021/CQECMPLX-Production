# Paper 00 — Foundation: Chart-to-J₃(O) Isomorphism & n=3 SU(3) Closure

## Central Thesis
The 8 chart states of Rule 30 are isomorphic to the diagonal of J₃(O). The 3-step conditional transition matrix on the shell=2 stratum is exactly closed in the S₃ group ring: M₃ = ⅓(T₁₂ + T₁₃ + T₂₃). This is the algebraic ground of all subsequent papers.

## Status
**PROVEN at machine precision.** Total checks: 6,272 (T3) + exact-rational (T4/T5/T6/T7). Mismatches: 0.

## Theorems (Verified)

### T3: Chart-to-J₃(O) Isomorphism
- **T3a (Bijection):** φ(L,C,R) = diag(L,C,R) is a bijection between chart states and J₃(O) diagonal elements.
- **T3b (Trace equality):** shell(L,C,R) = trace(φ(L,C,R)) ∈ {0,1,2,3}.
- **T3c (Weyl correspondence):** The LR reflection (L,C,R)↦(R,C,L) equals the J₃(O) permutation (1 3).
- **T3d (Idempotent stratum):** All shell=2 states map to trace-2 idempotents of J₃(O).
- **T3e (Readout equivalence):** The bit emitted by the chart's readout law equals the Rule 30 center bit.

### T4: Exact Rational n=3 SU(3) Weyl Closure
The 3-step conditional transition matrix on shell=2 is exactly:
```
M₃ = ⅓ (T₁₂ + T₁₃ + T₂₃)
```
Coefficients over ℚ: e=0, (12)=⅓, (13)=⅓, (23)=⅓, (123)=0, (132)=0. Sum=1. Residual²=0.

### T5: Rank-1 Idempotency of M₃
M₃·M₃ = M₃ exactly over ℚ. Eigenvalues {1,0,0}. The chart reaches its asymptotic uniform distribution in exactly 3 steps.

### T6: Both Trace-Blocks Close Identically
At n=3, trace-1 block (shell=1 states) and trace-2 block (shell=2 states) are the *same* SU(3) element. Cross-block mass ratios are exact rationals: trace-1↔trace-2 = 9/8, trace-0↔trace-{1,2} = 3/8, trace-0↔trace-3 = 1/8.

### T7: Closed-Form 8×8 Transition from Truth Table
The full 8×8 transition matrix under uniform marginalization of (LL,RR) has entries in {0,¼,½} over ℚ. Row sums = 1 exactly. Empirical convergence verified at 4096 depths.

## Tool Binding
`cqe_engine.formal.T3_isomorphism`, `cqe_engine.formal.T4_n3_closure`, `cqe_engine.formal.T5_idempotent`, `cqe_engine.formal.T6_trace_blocks`, `cqe_engine.formal.T7_8x8_transition`

## Proof Tree
```
axiom (octonion→J₃(O))
 → chart bijection (T3)
 → SU(3) n=3 closure (T4)
 → M₃ idempotent (T5)
 → trace-block identity (T6)
 → 8×8 closed form (T7)
```

## Open Obligations
**None.** All foundations closed at exact rational precision.

## Back-Propagation Targets
- CQE-engine: registers T3–T7 as the theorem bedrock
- Paper 01: T_BIJECTIVE builds on T3
- Paper 05: O2' linearization uses T3e (readout)
- Paper 23: F₄→Niemeier tree roots in T3c (Weyl correspondence)

---

*Source: `CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md` (T3–T7). Verifiers: `octonion.py`, `jordan_j3.py`, `f4_action.py`, `rule30.py`.*