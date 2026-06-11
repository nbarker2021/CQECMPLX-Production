# Paper 14 — Workbook: GR Boundary-Repair Curvature Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw torsion tensor | `CurvatureGluon().torsion_tensor()` | `T^λ_μν` |
| Compute Riemann | `verify_curvature_from_torsion()` | `R^ρ_σμν = dT + T∧T` |
| Compute Einstein | `verify_einstein_equation()` | `G_μν = κ T_μν` |
| Draw T tensor | `ErrorWall.residue` | `T_μν` |

## Human Execution Protocol (Paper 14)
```
1. Draw torsion tensor T^λ_μν from Paper 04 ErrorWall
2. Compute R = dT + T∧T (exterior derivative + wedge)
3. Compute dual *R
4. Compute G_μν = R_μν - ½g_μν R
4. Verify G_μν = κ T_μν (T = ErrorWall residue)
5. Record: R, *R, G, T all match
```

## Tool Execution Protocol (identical)
```python
cg = CurvatureGluon()
assert cg.verify_riemann_from_torsion()
assert cg.verify_einstein_equation()
```

## Receipt (identical)
```
gr-curvature-receipt =
  R_from_T: true
  Einstein_eq: true
  torsion_source: Paper-04-ErrorWall
  T_source: ErrorWall-residue
  human_verifiable: true (T = hand-drawable from ErrorWall)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
