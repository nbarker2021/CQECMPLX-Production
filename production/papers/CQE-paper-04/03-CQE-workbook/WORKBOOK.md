# Paper 04 — Workbook: Boundary Repair Sheet (v1 — isomorphic to tool)

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Place C token | `verify_boundary_repair()` | `chart_state = (L,C,R)` |
| Detect failed join | `failed_join = detect_failure(state)` | `bool` |
| Convert to typed constraint | `constraint = repair(failed_join)` | `dict` |
| Feed to next transport | `next_transport(constraint)` | `bool` |

## Human Execution Protocol (Paper 04)

```
1. Roll 3d2 → (L,C,R)
2. Detect failed join (correction ≠ 0 with no next state)
3. Draw red X at failure point
4. Convert to typed constraint (black token)
5. Feed constraint to next transport
6. Receipt: boundary repaired
```

## Tool Execution Protocol (identical)

```python
# Uses verify_boundary_repair with lattice_forge primitives

```

## Receipt

```
boundary-repair-receipt =
  T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route.: T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route. ✓
  human_verifiable: true
```

---

This is the pattern for ALL papers: **the workbook IS the tool spec**. Every analog operation has its exact digital twin.

## Correction Note

Boundary repair does not mean "the failure is now proven." A repaired boundary
row is a typed constraint with state, axis/sheet coordinate, reason, status,
source, target, and next legal route. Untyped failures remain rejected.
