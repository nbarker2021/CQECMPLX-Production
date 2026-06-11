# Paper 11 — Workbook: Theory Admission Gate Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Write theory Gluon mass | `admit_theory(theory_C)` | `int` |
| Check trusted spectrum | `gate.spectrum()` | `Set[int]` |
| Compare mass to K=9 | `mass ≤ 9?` | `bool` |
| Classify result | `admit_theory()` | `"admitted\|boundary\|rejected"` |
| Batch verify | `gate.batch_verify()` | `List[result]` |

## Human Execution Protocol (Paper 11)
```
1. Write theory's Gluon mass (compute from its transport)
2. Look up trusted spectrum (from CmplxLookupCache)
3. If mass ∈ spectrum and mass ≤ 9: ADMITTED
4. If mass = 10: BOUNDARY (K=9 boundary)
5. Else: REJECTED
6. Record: theory, mass, result, K-window
```

## Tool Execution Protocol (identical)
```python
gate = AdmissionGate(trusted_spectrum=CmplxLookupCache().load())
result = gate.admit(theory_C)
# result ∈ {"admitted", "boundary", "rejected"}

# Batch
results = gate.batch_verify([theory_A, theory_B, ...])
```

## Receipt (identical)
```
admission-receipt =
  theory: <ID>
  C_mass: <int>
  trusted_match: <bool>
  K_window: 9
  result: admitted|boundary|rejected
  all_verified: true
  human_verifiable: true (mass = count 1s in binary)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
