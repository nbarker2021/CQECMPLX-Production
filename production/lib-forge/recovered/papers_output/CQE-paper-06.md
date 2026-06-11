# P06 - Install Causal Chain

**Paper ID**: CQE-paper-06
**Step**: 06 of 33
**Status**: Verified (bilateral)

## 1. PHYSICAL OPERATION
Lay causal edge cards as DAG. Thread white dependency strings. Record DAG proof tree.

## 2. TOOLS USED (Cumulative Kit at This Step)
**Kit State**: 25 tools, 8 colors, 23 digital twins
**New Tools Added**: 3

### Tools Active at This Step:
- playing_card:causal_edge:01
- string:dependency:01
- proof_tree_sheet:dag:01

## 3. FORMAL THEOREM
T_CAUSAL: Every dependency = typed causal edge (proves/uses/refines/obligates/transports) with LookupReceipt

## 4. VERIFIED THEOREMS (This Paper)
- **T_CAUSAL**: (claimed)

## 5. BILATERAL VALIDATION
- **Kit at step**: 25 tools, 8 colors, 23 digital twins
- **New tools deployed**: 3
- **Verification**: bilateral validator

## 6. SUBSTITUTION RULES (Idempotent)
See Master Paper Appendix C for full 12-class substitution table.
All tools admit idempotent substitutes. Condition: read(action)->state; read(state)->same state

## 7. VERIFICATION COMMANDS
```bash
python -m cqe_engine.foundation T_CAUSAL
```

---
*Generated from MASTER PAPER at 2026-06-10T19:51:49.753810*