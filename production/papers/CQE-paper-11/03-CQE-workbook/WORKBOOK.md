# Paper 11 — Workbook: Theory Admission Gate Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
