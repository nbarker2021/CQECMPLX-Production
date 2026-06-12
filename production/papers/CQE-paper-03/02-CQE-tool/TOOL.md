# Paper 03 — Tool: D4/J3 Triality Verifier

## Tool Binding
- Module: `forgefactory.paper03_d4_j3_triality` (lineage)
- CQE Engine: `cqe_engine.formal.verify_triality` (white-room)

## Required Outputs
- `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`

## Minimum Test
Smoke test producing at least one proof-like row and one obligation-like row.

## Verifier Specification
```python
def verify_triality() -> dict:
    """Verify the local D4/J3 triality surface.

    Checks:
    1. Axis/sheet encoding is bijective over the eight LCR states.
    2. Axis pairs are antipodal complements.
    3. Paper 02 correction states land at (2,0) and (3,1).
    4. Diagonal J3 carrier preserves shell as trace.
    5. Shell-2 diagonal carriers are idempotent.

    Scope boundary: this verifier does not prove full D4 triality or a full
    F4/J3(O) action.
    """
    pass
```

## Usage
```python
from cqe_engine import verify_triality
result = verify_triality()
assert result["status"] == "pass"
```
