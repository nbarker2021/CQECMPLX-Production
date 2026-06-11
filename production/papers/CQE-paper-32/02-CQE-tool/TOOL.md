# Paper 32 — Tool: PermForge Verifier

## Module
`GraphStax.permforge` (lib-forge, ChromaBlend Studio)

## Public Surface
```python
from GraphStax.permforge import (
    # Cursor strings (lookup tables, import-time)
    SUPERPERM_N4, SUPERPERM_N5, N5_OCTAD, N5_OCTAD_LAYOUT,
    N5_REVERSAL_ORBIT, N5_REVERSAL_FIXED, N5_REVERSAL_PAIRS,
    superperm, load_record,
    # Coverage verification
    coverage_check, coverage_checksum,
    # The C normal form
    enumeration_request, c_normal_form,
    # The N+1 chart walk
    visit_order, recursive_step, recursive_construction,
    # Bounds ladder
    lower_bound, chart_walk_upper, egan_upper,
    # Paper 32 verifiers
    verify_record, n8_attempt, power_of_ten_walk,
    action_graph_compression, dimensional_split,
    # Scheduler
    SuperPermScheduler,
)
```

## Verifiers

### coverage_check(s, n)
True iff every permutation of 1..n appears as a length-n substring of s.
At n=8: 40320 needed permutations against ~46k windows — runs in milliseconds.

### recursive_construction(n)
Builds the chart-walk cursor from scratch, 1 → n, via `recursive_step`
(thread symbol k+1 through every visited chart of scale k, merge overlaps).
Verified live: every rung 1→8 has length Σk! and full coverage.
```
lift 1→2: len 3      coverage True
lift 2→3: len 9      coverage True
lift 3→4: len 33     coverage True
lift 4→5: len 153    coverage True
lift 5→6: len 873    coverage True
lift 6→7: len 5913   coverage True
lift 7→8: len 46233  coverage True     (walk time: 0.04 s)
```

### verify_record(n)
Loads the shipped record (n=4,5 embedded; n=6,7,8 from field data at
`CMPLX-PartsFactory-main/data/superpermutations/`, walk-up located) and
verifies coverage + position in the bounds ladder.

### n8_attempt()
The Paper 32 exhibit, executed live (0.06 s total):
```json
{
  "chart_walk":   {"length": 46233, "matches": true, "coverage_valid": true},
  "record":       {"length": 46205, "coverage_valid": true,
                   "lower_bound": 46085, "gap_to_lower": 120},
  "egan_construction": {"formula": "n! + (n-1)! + (n-2)! + (n-3)! + n - 3",
                        "value": 46205, "record_is_egan": true,
                        "saves_vs_chart_walk": 28},
  "open_window":  {"gap": 120, "gap_identity": "(n-3)! = 5! = 120"}
}
```

### power_of_ten_walk()
The full ladder N=1..8 with length, log10 position, bounds, solution
counts, chart status, and MDHG rung per N.

### action_graph_compression(n)
The N=D claim with live numbers: n! readings, n·n! naive symbols,
superperm length, compression ratio, coverage validity.

### dimensional_split()
The n=4→n=5 exhibit: 24-cell/D4 uniqueness, octad = E8 lanes, reversal
orbit (4 fixed + 2 pairs), torsor statement, gluon-orbit correspondence.

## Scheduler
```python
s = SuperPermScheduler(n=4)
s.step()                      # fire one enumeration request
list(s.schedule([a, b, c, d]))  # dispatch 4 items in cursor order (33 steps)
```
`GraphStaxEngine.enumerate_ribbon(ribbon_id, bits)` resolves a ribbon under
cursor supervision: first request per position creates the Stax (the
C-production), repeats are idempotent lookups.

## Receipts
ChromaForge composite path: `engine.resolve(content)` mints a PROCESS
receipt (`operation="graphstax.resolve"`) and reports ΔΦ = −κ to
conservation per resolution.

## Example Result
```json
{
  "paper_id": "CQE-paper-32",
  "verifiers_run": ["coverage_1_to_8", "n8_attempt", "octad_orbit"],
  "all_passed": true,
  "n8_record": 46205,
  "n8_lower_bound": 46085,
  "open_window": 120,
  "octad_orbit": {"fixed": [0, 1, 4, 6], "pairs": [[2, 5], [3, 7]]}
}
```
