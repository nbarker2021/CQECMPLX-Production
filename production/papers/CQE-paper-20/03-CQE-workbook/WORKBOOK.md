# Paper 20 — Workbook: Layer-2 Synthesis Ledger Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| List 20 C-forms | `SynthesisLedger().papers` | `List[C_form]` |
| XOR compose | `hash(⊕ C_i)` | `root_hash` |
| Verify all receipts | `ledger.verify_all()` | `{"all_verified": True}` |
| List obligations | `ledger.obligations` | `List[Obligation]` |

## Human Execution Protocol (Paper 20)

```
1. List C₀ through C₁₉ as 20 beads
2. XOR compose: C₀ ⊕ C₁ ⊕ ... ⊕ C₁₉
3. Compute root hash = hash(⊕ C_i)
5. Verify all 20 receipts valid
6. List open obligations (none for 00-19)
```

## Tool Execution Protocol (identical)

```python
ledger = SynthesisLedger()
for i in range(20):
    ledger.add_paper(i, C_i)

assert ledger.verify_all()["all_verified"]
hash = ledger.root_hash()
```

## Receipt (identical)

```
synthesis-receipt =
  papers: 20
  root_hash: hash(⊕ C₀⋯C₁₉)
  all_receipts_valid: true
  open_obligations: 0
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
