# Paper 17 — Workbook: E6-E8 Error-Correction Tower Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw E6 Gluon | `TowerGluon().C_E6()` | `GluonState` |
| Draw E7 Gluon | `TowerGluon().C_E7()` | `GluonState` |
| Draw E8 Gluon | `TowerGluon().C_E8()` | `GluonState (dim 248)` |
| Draw E6→E7 glue | `TowerGluon().transport_E6_E7()` | `glue_vector` |
| Draw E7→E8 glue | `TowerGluon().transport_E7_E8()` | `glue_vector` |
| Draw E8 top | `TowerGluon().C_E8_dim()` | `248` |

## Human Execution Protocol (Paper 17)

```
1. Draw E6 Gluon (C_E6)
2. Apply E6→E7 glue vector → C_E7 = C_E6 ⊕ corr_E6
3. Apply E7→E8 glue vector → C_E8 = C_E7 ⊕ corr_E7
2. Verify E8 dim = 248
4. Verify Z4 wrap: E6→E7→E8→return
```

## Tool Execution Protocol (identical)

```python
tower = TowerGluon()
assert tower.C_E8_dim() == 248
assert tower.transport_E6_E7().valid
assert tower.transport_E7_E8().valid
```

## Receipt (identical)

```
tower-receipt =
  E6: verified
  E7: verified
  E8: dim=248 ✓
  glue_vectors: valid ✓
  Z4_wrap: E6→E7→E8→return ✓
  human_verifiable: true (E6/E7 glues = hand-verifiable)
```

---

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
