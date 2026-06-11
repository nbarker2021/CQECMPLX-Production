# Paper 06 — Workbook: Causal Code Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw causal vertex | `build_terminal_composition_tree()` | `CausalVertex(source, target, edge_type)` |
| Draw typed edge | `CausalEdge(to, edge_type, receipt)` | `dict[str, List[CausalEdge]]` |
| Label edge type | `edge_type ∈ {proves, uses, refines, obligates, transports}` | `Enum` |
| Attach receipt | `LookupReceipt(edge_id, timestamp)` | `LookupReceipt` |
| Trace causal path | `CausalIndex.path(src, dst)` | `List[CausalEdge]` |
| Verify coherence | `verify_causal_coherence()` | `{"coherent": bool}` |

## Human Execution Protocol (Paper 06)
```
1. List all 32 papers as vertices on grid
2. For each paper, list its dependencies from INTENT.md
3. Draw typed edges (proves/uses/refines/obligates/transports)
4. Attach receipt IDs to each edge
5. Trace path from Paper 00 → Paper 31
4. Verify no circular chains, all obligations resolved
```

## Tool Execution Protocol (identical)
```python
# 1. Build terminal composition tree
tree = build_terminal_composition_tree()

# 2. Verify causal coherence
result = verify_causal_coherence()
assert result["coherent"] == True

# 3. Query specific causal paths
idx = CausalIndex()
path = idx.path("CQE-paper-00", "CQE-paper-29")
```

## Receipt (identical for human and tool)
```
causal-receipt =
  vertices: 32
  edges: 12544
  circular_chains: 0
  all_obligations_resolved: true
  human_verifiable: true (traceable edge-by-edge)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
