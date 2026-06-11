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
    """Verify D4/J3 triality: axis/sheet, rotation/reflection, Jordan carrier."""
    pass
```

## Usage
```python
from cqe_engine import verify_triality
result = verify_triality()
assert result["status"] == "pass"
```