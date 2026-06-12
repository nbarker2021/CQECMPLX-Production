# Paper 32 — Workbook: The Cursor Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet <-> Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Write the cursor string on the sheet | `superperm(n)` | `str` (lookup table) |
| Slide a length-n window along it | `enumeration_request(cursor, n)` | `{cursor, slot, window, is_permutation}` |
| Mark each new permutation seen | `visit_order(s, n)` | `List[str]` (first-visit charts) |
| Check every permutation got marked | `coverage_check(s, n)` | `bool` |
| Thread symbol n+1 through each mark | `recursive_step(s, n)` | `str` (the lifted cursor) |
| Tally the bounds ladder | `lower_bound / chart_walk_upper / egan_upper` | `int` |
| Flip the sheet (read backward) | `s[::-1]` + canonical relabel | `N5_REVERSAL_ORBIT` |
| Read a bit's C when (and only when) requested | `c_normal_form(L, C, R, cursor)` | `{expression, gluon, emission_bit}` |

## Human Execution Protocol (Paper 32)

```
1. Write "1" on the sheet. This is the n=1 cursor (one chart, trivial).
2. LIFT: for each permutation you have marked, in the order you marked
   them, write it again with the new symbol between two copies
   (p · n+1 · p), overlapping shared characters with what's already
   written. Do not invent an order — the visit order IS the order.
3. Slide a window of the new size along the result. Mark every distinct
   permutation the window shows you. When every permutation of the new
   alphabet is marked exactly once, the rung is complete.
4. Tally the length. It must equal 1!+2!+...+n!. (1, 3, 9, 33, 153,
   873, 5913, 46233.)
5. Repeat steps 2-4 until n=8. You have walked the power-of-ten ladder:
   each rung's log10 is one step up (0, 0.48, 0.95, 1.52, 2.18, 2.94,
   3.77, 4.67).
6. At n=4, attempt any rearrangement that shortens the sheet: none
   exists (33 is unique, and the string reads the same backward).
7. At n=5, the published exhaustive search gives all 8 minimal sheets.
   Flip each one: 4 read the same (up to renaming), the other 4 swap
   in pairs. Compare with the 8 chart states under L-R swap: 4 fixed,
   2 pairs. Same orbit shape.
8. At n=8, place the Egan-construction sheet (46205) beside your
   chart-walk sheet (46233): it saves exactly 28 symbols. Below it,
   the proven floor is 46085. The open strip is exactly 120 = 5! wide.
```

## Tool Execution Protocol (identical)

```python
from GraphStax import permforge as pf

# 1-5. The ladder

s = "1"
for k in range(1, 8):
    s = pf.recursive_step(s, k)
    assert len(s) == pf.chart_walk_upper(k + 1)
    assert pf.coverage_check(s, k + 1)

# 6-7. The split

d = pf.dimensional_split()
assert d["n4"]["solution_count"] == 1 and d["n4"]["palindromic"]
assert d["n5"]["solution_count"] == 8
assert d["n5"]["reversal_fixed"] == [0, 1, 4, 6]

# 8. The n=8 attempt

r = pf.n8_attempt()
assert r["record"]["coverage_valid"]
assert r["egan_construction"]["record_is_egan"]
assert r["open_window"]["gap"] == 120
```

## Receipt (identical for human and tool)

```
cursor-receipt =
  rungs_walked: 8                       (1 → 8, all coverage-verified)
  chart_walk_lengths: [1,3,9,33,153,873,5913,46233]   (= Σk! at every rung)
  n8_record: 46205                      (= Egan formula, coverage-verified)
  n8_floor: 46085                       (Houston-Pantone-Vatter bound)
  open_window: 120 = (n-3)!
  octad_orbit: 4 fixed + 2 pairs        (= swap_LR orbit on chart states)
  human_verifiable: true (window-by-window, mark-by-mark)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
