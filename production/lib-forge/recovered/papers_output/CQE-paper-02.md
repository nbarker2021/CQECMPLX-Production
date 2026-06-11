# P02 - Install Proofreading

**Paper ID**: CQE-paper-02
**Step**: 02 of 33
**Status**: Verified (bilateral)

## 1. PHYSICAL OPERATION
Place correction token at gradient positions where C=1, R=0. Overlay clear sleeve to verify D4 axes. Mark black obligation for any firing position.

## 2. TOOLS USED (Cumulative Kit at This Step)
**Kit State**: 13 tools, 7 colors, 11 digital twins
**New Tools Added**: 3

### Tools Active at This Step:
- token:correction:01
- clear_sleeve:overlay:01
- obligation_sheet:black:01

## 3. FORMAL THEOREM
T_CORRECTION: Correction = C and not R fires at D4 axes {2,0},{3,1}; residue feeds next transport

## 4. VERIFIED THEOREMS (This Paper)
- **T_CORRECTION**: Correction = C and not R fires at D4 axes {2,0},{3,1}

## 5. BILATERAL VALIDATION
- **Kit at step**: 13 tools, 7 colors, 11 digital twins
- **New tools deployed**: 3
- **Verification**: bilateral validator

## 6. SUBSTITUTION RULES (Idempotent)
See Master Paper Appendix C for full 12-class substitution table.
All tools admit idempotent substitutes. Condition: read(action)->state; read(state)->same state

## 7. VERIFICATION COMMANDS
```bash
python -m cqe_engine.foundation T_CORRECTION
```

---
*Generated from MASTER PAPER at 2026-06-10T19:51:49.752303*