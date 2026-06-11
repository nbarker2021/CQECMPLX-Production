# P05 - Install Carrier

**Paper ID**: CQE-paper-05
**Step**: 05 of 33
**Status**: Verified (bilateral)

## 1. PHYSICAL OPERATION
Place carrier token. Thread neon string along path. Record transport receipt.

## 2. TOOLS USED (Cumulative Kit at This Step)
**Kit State**: 22 tools, 8 colors, 20 digital twins
**New Tools Added**: 3

### Tools Active at This Step:
- token:carrier:01
- string:path:01
- receipt_sheet:transport:01

## 3. FORMAL THEOREM
T_OLOID_PATH: Curved/rolling carriers preserve continuity; C_accumulated = XOR of correction bits

## 4. VERIFIED THEOREMS (This Paper)
- **T_OLOID_PATH**: (claimed)

## 5. BILATERAL VALIDATION
- **Kit at step**: 22 tools, 8 colors, 20 digital twins
- **New tools deployed**: 3
- **Verification**: bilateral validator

## 6. SUBSTITUTION RULES (Idempotent)
See Master Paper Appendix C for full 12-class substitution table.
All tools admit idempotent substitutes. Condition: read(action)->state; read(state)->same state

## 7. VERIFICATION COMMANDS
```bash
python -m cqe_engine.foundation T_OLOID_PATH
```

---
*Generated from MASTER PAPER at 2026-06-10T19:51:49.752303*