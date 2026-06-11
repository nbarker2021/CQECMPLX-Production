# Paper 15 — Workbook: QFT/Higgs Mass-Residue Carrier Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw Higgs field | `HiggsGluon().field()` | `ϕ = C_accumulated` |
| Compute mass | `HiggsGluon().mass_residue()` | `m_h² ∝ |C_acc|²` |
| Draw sector | `HiggsGluon().sector()` | `"vacuum" \| "excited"` |
| Verify mechanism | `verify_higgs_mechanism()` | `{"symmetry_broken": true}` |

## Human Execution Protocol (Paper 15)
```
1. Draw C_accumulated = XOR of all correction bits
2. If C_acc = 0: sector = vacuum (weight 0) → symmetry intact
3. If C_acc ≠ 0: sector = excited (weight 5) → symmetry broken
4. Compute m_h² ∝ |C_acc|²
5. Record: Higgs field = ϕ = C_acc
```

## Tool Execution Protocol (identical)
```python
hg = HiggsGluon()
assert hg.field() == gluon.C_accumulated
assert hg.mass_residue() == abs(hg.field())**2
assert hg.sector() in ("vacuum", "excited")
assert hg.sector() == "excited" == (hg.field() != 0)
```

## Receipt (identical)
```
higgs-receipt =
  field_phi: C_accumulated
  mass_squared: |C_acc|^2
  sector: excited (weight 5)
  symmetry_broken: true
  human_verifiable: true (C_acc = running XOR of bits)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
