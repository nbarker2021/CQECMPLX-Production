# P04 - Install Boundary Repair

**Paper ID**: CQE-paper-04
**Step**: 04 of 33
**Status**: Verified (bilateral)

## 1. PHYSICAL OPERATION
Place oloid midpoint token at boundary. Roll on surface, trace curved path. Record curved receipt with neon marker.

## 2. TOOLS USED (Cumulative Kit at This Step)
**Kit State**: 19 tools, 8 colors, 17 digital twins
**New Tools Added**: 3

### Tools Active at This Step:
- token:oloid:01
- loose_paper:rolling_surface:01
- receipt_sheet:curved:01

## 3. FORMAL THEOREM
T_BOUNDARY_REPAIR: Failed joins become typed constraints; oloid midpoint s* = (N + -N)/2

## 4. VERIFIED THEOREMS (This Paper)
- **T_BOUNDARY_REPAIR**: (claimed)
- **T_WRAP**: Local rollout: all 8 states -> Lie conjugate in <=3 S3 steps

## 5. BILATERAL VALIDATION
- **Kit at step**: 19 tools, 8 colors, 17 digital twins
- **New tools deployed**: 3
- **Verification**: bilateral validator

## 6. SUBSTITUTION RULES (Idempotent)
See Master Paper Appendix C for full 12-class substitution table.
All tools admit idempotent substitutes. Condition: read(action)->state; read(state)->same state

## 7. VERIFICATION COMMANDS
```bash
python -m cqe_engine.foundation T_BOUNDARY_REPAIR
```

---
*Generated from MASTER PAPER at 2026-06-10T19:51:49.752303*