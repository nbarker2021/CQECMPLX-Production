# Paper 10 — Workbook: T10 Master Receipt Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| List 10 paper C-forms | `compose_master_receipt([0..9])` | `List[C_form]` |
| XOR compose C_accumulated | `C₀ ⊕ C₁ ⊕ ... ⊕ C₉` | `int` |
| Verify all receipts | `verify_master_receipt()` | `{"valid": bool}` |
| Write root hash | `hash(⊕ C_i)` | `str` |
| List obligations | `master_receipt.obligations` | `List[Obligation]` |

## Human Execution Protocol (Paper 10)
```
1. Write C₀ through C₉ as 10 beads on string
2. XOR them left-to-right: C₀ ⊕ C₁ ⊕ ... ⊕ C₉
3. Verify each paper's receipt is valid
4. Record root hash = hash(⊕ C_i)
5. Check: all obligations resolved?
```

## Tool Execution Protocol (identical)
```python
# 1. Compose master receipt
receipt = compose_master_receipt(range(10))

# 2. Verify
result = verify_master_receipt(receipt)
assert result["valid"] == True

# 3. Check C_accumulated
print(f"C_accumulated = {receipt.C_accumulated}")
```

## Receipt (identical)
```
master-receipt =
  papers: 10
  C_accumulated: C₀⊕C₁⊕...⊕C₉
  all_receipts_valid: true
  all_obligations_resolved: true
  root_hash: <SHA256>
  human_verifiable: true (10 XORs = hand-calculable)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
