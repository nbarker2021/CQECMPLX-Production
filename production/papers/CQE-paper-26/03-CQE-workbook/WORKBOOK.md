# Paper 26 — Workbook: Z-Pinch and Shear Horizon Sheet

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
