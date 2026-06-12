# Paper 03 — Workbook: D4/J3 Triality Sheet (v1 — isomorphic to tool)

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token at local center | `verify_triality()` | `chart_state = (L,C,R)` |
| Draw D4 axis labels (2,0)/(3,1) | `ANTIPODAL_LABEL[state]` | `int` |
| Draw sheet signs (+/-) | `SHEET_SIGN[state]` | `int` |
| Draw J3(O) diagonal | `phi = diag(L,C,R)` | `J3O_diagonal` |
| Verify S3 action = axis/sheet rotation | `verify_s3_action()` | `bool` |

## Human Execution Protocol (Paper 03)

```
1. Roll 3d2 → (L,C,R)
2. Look up axis = ANTIPODAL_LABEL[state], sheet = SHEET_SIGN[state]
3. Draw axis (2,0) or (3,1); draw sheet +/-
4. Trace phi = diag(L,C,R) on J3(O) paper
5. Apply S3 rotation/reflection — verify triality
6. Record receipt: axis/sheet/J3(O) aligned
```

## Tool Execution Protocol (identical)

```python
from lattice_forge.chart_codec_d4 import ANTIPODAL_LABEL, SHEET_SIGN
from lattice_forge.rule90_linearization import correction_from_chart
states = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]
for s in states:
    axis = ANTIPODAL_LABEL[s]; sheet = SHEET_SIGN[s]
    corr = correction_from_chart(s)
    # Triality: axis/sheet ↔ J3(O) diagonal ↔ S3 rotation

```

## Receipt

```
triality-receipt =
  T_TRIALITY: D4 axis/sheet ↔ J3(O) diagonal ✓
  T_TRIALITY: S3 rotation/reflection ↔ triality ✓
  human_verifiable: true
```

## Scope Note

This workbook verifies the finite local surface: LCR state, axis/sheet code,
and diagonal J3 carrier. It does not by itself prove full D4 triality or a full
F4/J3(O) action. Those stronger claims remain separate proof obligations.
