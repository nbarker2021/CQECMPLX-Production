# Paper 22 — Workbook: MetaForge Applied Materials Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Token → material | `MetaForge().materialize(token)` | `Material` |
| Verify oloid form | `verify_cayley_dickson_oloid_normal_form()` | `normal_form` |
| Select model | `verify_oloid_model_selection()` | `selected_model` |
| Compute energy | `formation_energy(material)` | `Gluon mass = energy` |

## Human Execution Protocol (Paper 22)
```
1. Token (glyph/number/shape) from Paper 21
2. Materialize: add physical properties
3. Verify oloid normal form
4. Select best model (Pareto frontier)
4. Compute formation energy = Gluon mass
```

## Tool Execution Protocol (identical)
```python
mf = MetaForge()
material = mf.materialize(token)
mf.verify_oloid_normal_form()
best = mf.select_model([m1, m2, m3])
energy = mf.formation_energy(best)
```

## Receipt (identical)
```
metaforge-receipt =
  materials: 5 candidates
  oloid_form: verified
  selected: Pareto optimal
  formation_energy: Gluon mass
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
