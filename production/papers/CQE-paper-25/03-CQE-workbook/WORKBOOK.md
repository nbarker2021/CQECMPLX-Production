# Paper 25 — Workbook: Energetic Traversal Maps Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Compute winding | `TraversalGluon().winding(N)` | `int` |
| Trace rolling path | `TraversalGluon().rolling_path()` | `List[step]` |
| Compute energy | `TraversalGluon().energy_budget()` | `energy_cost` |
| Find geodesic | `TraversalGluon().geodesic()` | `minimal path` |

## Human Execution Protocol (Paper 25)
```
1. Compute winding number for traversal
2. Trace rolling transport path
3. Compute energy cost along path
4. Find geodesic (minimal energy)
5. Record: traversal Gluon = energy/ledger
```

## Tool Execution Protocol (identical)
```python
tg = TraversalGluon()
w = tg.winding(128)
path = tg.rolling_path()
energy = tg.energy_budget()
geodesic = tg.geodesic()
```

## Receipt (identical)
```
traversal-receipt =
  winding: verified
  rolling: verified
  geodesic: minimal energy
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
