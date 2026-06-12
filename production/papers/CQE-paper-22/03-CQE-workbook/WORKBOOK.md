# Paper 22 — Workbook: MetaForge Applied Materials Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
