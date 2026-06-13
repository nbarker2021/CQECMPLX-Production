# Paper 12 — Workbook: CA Prediction Surface Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Write Rule 30 truth table | `rule30_readout_ribbon_machine()` | `8 entries` |
| Compute correction | `correction(L,C,R) = C ∧ ¬R` | `int (0\|1)` |
| Draw prediction surface | `rule30_sheet_operator(30, 64)` | `64×64 grid` |
| Mark 64 silent-boundary rules | `verify_universal_ca()` | `64 rules` |

## Human Execution Protocol (Paper 12)

```
1. Write Rule 30 truth table (8 rows)
2. For each state, compute: bit = NOT L if C=1 else L⊕R
3. Decompose: Rule 30 = Rule 90 ⊕ (C ∧ ¬R)
4. Draw prediction surface: correction field over light cone
5. Verify: 64 silent-boundary rules close at n=3
```

## Tool Execution Protocol (identical)

```python
# 1. Rule 30 prediction

machine = rule30_readout_ribbon_machine()
pred = machine.predict(30, 128)

# 2. Verify vignette algebra

verify_rule30_vignette_algebra()

# 3. Universal CA

verify_universal_ca()  # 64 rules close at n=3

```

## Receipt (identical)

```
ca-receipt =
  rule: 30
  prediction_surface: exact (0 defects)
  vignette_algebra: verified
  silent_boundary_rules: 64/256
  n=3_closure: exact for 64
  human_verifiable: true (truth table = 8 rows)
```

---

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
