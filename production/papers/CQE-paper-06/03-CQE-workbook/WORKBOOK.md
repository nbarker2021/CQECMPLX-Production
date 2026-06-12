# Paper 06 — Workbook: Causal Code Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
6. Verify no hidden proof-support cycles; keep open obligations marked open
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
  required_fields: source,target,edge_type,receipt,status
  invalid_edges_rejected: true
  hidden_proof_cycles_rejected: true
  open_obligations_tracked: true
  human_verifiable: true (traceable edge-by-edge)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*

## Correction Note

The causal workbook is a graph discipline, not a declaration that the entire
32-paper corpus is closed. Open obligations must remain open until a verifier
or receipt closes them.
