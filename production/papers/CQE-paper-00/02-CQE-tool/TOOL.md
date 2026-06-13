# Paper 00 — Tool: Foundation Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.foundation`

## Public Surface
```python
from cqe_engine.foundation import (
    verify_T3_chart_j3o_isomorphism,    # max_depth: int → dict
    verify_T4_n3_closure_exact,         # → dict
    verify_T5_M3_idempotent,            # → dict
    verify_T6_trace_blocks,             # → dict
    verify_T7_8x8_transition_exact,     # → dict
    verify_all_foundations,             # → dict
)
```

## Verifiers

### verify_T3_chart_j3o_isomorphism(max_depth=4096)
Runs the full chart/J₃(O) bijection check at every depth ≤ max_depth.
Returns: `{"status": "pass"|"fail", "total_checks": int, "mismatches": int, "claim": str}`
At max_depth=4096: 6,272 checks, 0 mismatches, ~30s runtime.

### verify_T4_n3_closure_exact()
Computes M₃ from the 3-step conditional counts on shell=2, verifies exact rational coefficients.
Returns: `{"status": "pass", "coefficients": {perm: rational}, "residual_squared_ℚ": 0}`

### verify_T5_M3_idempotent()
Verifies M₃·M₃ = M₃ over ℚ, eigenvalues {1,0,0}.
Returns: `{"status": "pass", "M3_squared_equals_M3": True, "eigenvalues": [1,0,0]}`

### verify_T6_trace_blocks()
Verifies trace-1 and trace-2 blocks close to the same SU(3) element at n=3.
Returns: `{"status": "pass", "cross_block_masses": {str: rational}}`

### verify_T7_8x8_transition_exact()
Constructs the full 8×8 transition matrix from Rule 30 truth table with (LL,RR) uniform marginalization.
Returns: `{"status": "pass", "entry_set": {0, 1/4, 1/2}, "row_sums_all_one": True}`

### verify_all_foundations()
Runs T3–T7 sequentially, returns consolidated status.
```json
{
  "status": "pass",
  "T3": {"status": "pass", "total_checks": 6272, "mismatches": 0},
  "T4": {"status": "pass", "residual_ℚ": 0},
  "T5": {"status": "pass", "idempotent": true},
  "T6": {"status": "pass", "blocks_identical": true},
  "T7": {"status": "pass", "entries_in_Q": true}
}
```

## CLI
```bash
python -m cqe_engine.foundation                         # runs verify_all_foundations
python -m cqe_engine.foundation T3 128                  # T3 at depth 128
python -m cqe_engine.foundation T4 T5 T6 T7             # specific theorems
```

## Receipts
Written to `proof-receipts/CQE-paper-00/foundation-<theorem>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-00",
  "theorems": ["T3", "T4", "T5", "T6", "T7"],
  "all_passed": true,
  "T3_checks": 6272,
  "T4_residual_Q": 0,
  "T5_idempotent": true,
  "T6_blocks_identical": true,
  "T7_entry_set": [0, 0.25, 0.5]
}
```

---

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*