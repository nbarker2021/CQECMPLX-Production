# Paper 07 - Workbook: Discrete-Continuous Bridge Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet / Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|---|---|---|
| Plot discrete points | `BridgeInterpolator()` | `List[Tuple[depth, value]]` |
| Draw interpolating curve | `interpolate_discrete_to_continuous()` | `ContinuousField` |
| Mark Rule 90 base | `rule90(L,R)` | `int` |
| Mark correction bits | `correction(L,C,R)` | `int (0 or 1)` |
| Draw interpolation kernel | `rule90 xor correction` | `ContinuousField` |
| Verify indexed sample exactness | `verify_bridge_exactness()` | `{"max_sample_error": 0}` |

## Human Execution Protocol

```text
1. Draw discrete causal edges from Paper 06 on a grid.
2. At each indexed sample, place the observed discrete value.
3. At each local state, compute correction = C and not R.
4. Overlay base xor correction to recover the Rule 30 local field.
5. Connect adjacent samples with straight bridge segments.
6. Verify that every discrete sample point exactly matches the interpolant.
7. Mark between-sample physical dynamics as an open obligation unless a later
   theorem closes that claim.
```

## Tool Execution Protocol

```python
from fractions import Fraction

discrete = Paper06.causal_field()

interp = BridgeInterpolator()
continuous = interp.interpolate(discrete)

result = verify_bridge_exactness(4096)
assert result["max_sample_error"] == Fraction(0, 1)
assert result["between_sample_dynamics_closed"] is False
```

## Receipt

```text
bridge-receipt =
  depths_checked: 4096
  max_sample_error: 0
  r30_decomposition: exact
  between_sample_dynamics_closed: false
  human_verifiable: true
```

---

*This is the sample-preserving bridge algorithm. The workbook is the hand
counterpart of the code spec, while between-sample physical dynamics remain a
separate proof obligation.*
