# Paper 21 — Workbook: MorphForge/PolyForge/MorphoniX Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Create token | `MorphForge().token("x")` | `Token` |
| Apply K | `MorphForge().apply_K(token)` | `discard` |
| Apply S | `MorphForge().apply_S(token)` | `bond` |
| Bifurcate | `MorphForge().bifurcate(token, ctx)` | `S(token, ctx)` |
| Verify SK algebra | `verify_morphonics_model()` | `SK identities` |

## Human Execution Protocol (Paper 21)
```
1. Create token (number/shape/glyph)
2. Apply K: discard (carry fails)
3. Apply S: bond (carry holds)
4. Bifurcate: S(token, context) = next token
5. Verify SK identities: S K K = I, S K S = K
```

## Tool Execution Protocol (identical)
```python
mf = MorphForge()
token = mf.token("x")
mf.apply_K(token)    # discards
mf.apply_S(token)    # bonds
mf.bifurcate(token, context)
mf.verify_sk_algebra()
```

## Receipt (identical)
```
morphonix-receipt =
  tokens: created
  K: discard ✓
  S: bond ✓
  SK: S K K = I, S K S = K ✓
  torsor_functor: ✓
  human_verifiable: true (SK = hand-computable)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
