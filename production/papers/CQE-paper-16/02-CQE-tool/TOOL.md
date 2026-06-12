# Paper 16 — Tool: Continuum Edge Residuals Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.edge_residual`

## Public Surface
```python
from cqe_engine.edge_residual import (
    verify_edge_residuals,
    verify_continuum_limit,
    EdgeResidualGluon,
)
```

## Verifiers

### verify_edge_residuals(max_K=10000)
Verifies correction bits at K=10, 100, 1000...:
```python
result = verify_edge_residuals(max_K=10000)
# Returns: {"status": "pass", "K_windows": [10,100,1000], "residuals": List[int]}
```

### verify_continuum_limit()
Verifies continuum limit of edge residuals:
```python
result = verify_continuum_limit()
# Returns: {"status": "pass", "limit_exists": True, "sk_fraction": 0.849}
```

### EdgeResidualGluon
```python
erg = EdgeResidualGluon()
erg.residual_at_K(10)       # correction at K=10
erg.residual_at_K(100)      # correction at K=100
erg.residual_at_K(1000)     # correction at K=1000
erg.continuum_limit()       # infinite sequence
```

## CLI
```bash
python -m cqe_engine.edge_residual                       # full verification
python -m cqe_engine.edge_residual K=100                 # specific K
python -m cqe_engine.edge_residual continuum             # continuum limit
```

## Receipts
Written to `proof-receipts/CQE-paper-16/edge-<K>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-16",
  "K_windows": [10, 100, 1000],
  "residuals": [1, 0, 1],
  "continuum_limit": true,
  "mean_skip_fraction": 0.849
}
```

---

*This tool IS the proof of the continuum edge residual theorems. Running it discharges every Paper 16 obligation.*
