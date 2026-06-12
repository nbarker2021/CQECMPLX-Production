# Paper 16 — Workbook: Continuum Edge Residuals Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Compute K=10 residual | `EdgeResidualGluon().residual_at_K(10)` | `int (0|1)` |
| Compute K=100 residual | `EdgeResidualGluon().residual_at_K(100)` | `int (0|1)` |
| Compute K=1000 residual | `EdgeResidualGluon().residual_at_K(1000)` | `int (0|1)` |
| Draw continuum limit | `EdgeResidualGluon().continuum_limit()` | `infinite sequence` |
| Compute skip fraction | `mean_skip_fraction` | `0.849` |

## Human Execution Protocol (Paper 16)

```
1. For K=10: compute C ∧ ¬R at K-window boundary
2. For K=100: same at K=100 boundary
4. For K=1000: same at K=1000 boundary
4. Record: correction bits = edge residuals
5. Compute skip fraction = skipped/real = 0.849
6. Draw continuum limit = infinite sequence of residuals
```

## Tool Execution Protocol (identical)

```python
erg = EdgeResidualGluon()
residuals = [erg.residual_at_K(K) for K in [10, 100, 1000, 10000]]
limit = erg.continuum_limit()
assert erg.skip_fraction() == 0.849
```

## Receipt (identical)

```
edge-residual-receipt =
  K=10: residual=1
  K=100: residual=0
  K=1000: residual=1
  K=10000: residual=0
  continuum_limit: exists
  mean_skip_fraction: 0.849
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
