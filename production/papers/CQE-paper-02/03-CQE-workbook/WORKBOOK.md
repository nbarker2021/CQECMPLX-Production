# Paper 02 — Workbook: Correction Surface Sheet (v1 — isomorphic to tool)

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token at local center | `verify_correction_surface()` | `chart_state = (L,C,R)` |
| Mark correction surface | `correction = C & (1-R)` | `int` |
| Draw residue as black follow-up | `residue = correction_surface(state)` | `dict` |
| Verify residue feeds next transport | `next_transport(residue)` | `bool` |

## Human Execution Protocol (Paper 02)

```
1. Roll 3d2 → (L,C,R)  [coin flip ×3 = chart state]
2. Compute correction = C ∧ ¬R
3. If correction ≠ 0: draw black token (residue)
4. Record residue as correction surface data
5. Feed residue to next transport step
6. Receipt: correction surface logged, not erased
```

## Tool Execution Protocol (identical)

```python
from lattice_forge.rule90_linearization import correction, correction_from_chart
states = [(L,C,R) for L in (0,1) for C in (0,1) for R in (0,1)]
corrections = {s: correction(s[0], s[1], s[2]) for s in states}
# correction fires at D4 axes {(2,0), (3,1)}

assert {s for s, value in corrections.items() if value} == {(0,1,0), (1,1,0)}
assert all((value == 1) == (correction_from_chart(s) == 1) for s, value in corrections.items())
```

## Receipt (identical for human and tool)

```
correction-receipt =
  T_CORRECTION: correction = C ∧ ¬R verified ✓
  T_CORRECTION: D4 axes {2,0}, {3,1} match ✓
  T_CORRECTION: residue feeds next transport ✓
  human_verifiable: true
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.

## Correction Note

The correction surface is not permission to accept a failed route as proof.
Nonzero correction is positive data only when it is recorded as typed,
replayable residue and routed into the next obligation.
