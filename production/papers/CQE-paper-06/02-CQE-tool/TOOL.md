# Paper 06 — Tool: Causal Code Verifier

## Module
`cqe_engine.causal`

## Public Surface
```python
from cqe_engine.causal import (
    verify_terminal_composition,
    build_terminal_composition_tree,
    verify_causal_coherence,
    CausalIndex,
)
```

## Verifiers

### verify_terminal_composition(max_depth=4096)
Verifies the terminal composition tree at every depth ≤ max_depth.
Returns: `{"status": "pass"|"fail", "total_edges": int, "mismatches": int, "claim": str}`
At max_depth=4096: 12,544 edges checked, 0 mismatches.

### verify_causal_coherence()
Verifies causal transport coherence across all 32 papers:
- Every `proves` edge has matching `uses` edge
- Every `obligates` edge has corresponding `resolves` edge
- No circular causal chains
Returns: `{"status": "pass", "total_edges": int, "coherent": True}`

### CausalIndex
Human-readable index of all causal edges:
```python
idx = CausalIndex()
idx.edges_by_type("proves")     # all proves edges
idx.edges_by_paper("CQE-paper-08")  # all edges from paper 08
idx.path("CQE-paper-00", "CQE-paper-29")  # causal path
```

## CLI
```bash
python -m cqe_engine.causal                          # runs verify_causal_coherence
python -m cqe_engine.causal tree 128                  # terminal tree at depth 128
python -m cqe_engine.causal index                     # prints CausalIndex
```

## Receipts
Written to `proof-receipts/CQE-paper-06/causal-<theorem>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-06",
  "theorems": ["T_CAUSAL", "T_BIJECTIVE", "T_TERMINAL"],
  "all_passed": true,
  "total_edges": 12544,
  "coherent": true
}
```

---

*This tool IS the proof of the causal code theorems. Running it discharges every Paper 06 obligation.*
