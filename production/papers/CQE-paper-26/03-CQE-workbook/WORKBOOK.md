# Paper 26 — Workbook: Z-Pinch and Shear Horizon Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Compute pinch winding | `ZPinchGluon().winding(N)` | `int` |
| Trace rolling transport | `ZPinchGluon().rolling_transport()` | `List[step]` |
| Draw shear components | `ZPinchGluon().shear_components()` | `off-diagonal` |
| Find mirror partner | `ZPinchGluon().mirror_partner()` | `Grain` |

## Human Execution Protocol (Paper 26)

```
1. Compute pinch winding number
2. Trace rolling transport (N|-N)
3. Draw shear components (off-diagonal)
4. Find mirror partner (-k)
5. Record: pinch = C/||C||, shear = off-diagonal
```

## Tool Execution Protocol (identical)

```python
zpg = ZPinchGluon()
w = zpg.winding(128)
path = zpg.rolling_transport()
shear = zpg.shear_components()
mirror = zpg.mirror_partner()
```

## Receipt (identical)

```
zpinch-receipt =
  winding: verified
  rolling: verified
  shear: off-diagonal
  mirror: -k partner found
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
