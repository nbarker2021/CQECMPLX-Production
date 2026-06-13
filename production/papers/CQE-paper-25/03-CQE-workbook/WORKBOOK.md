# Paper 25 — Workbook: Energetic Traversal Maps Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
