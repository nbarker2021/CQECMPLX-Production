# Paper 04 — Tool: Boundary Repair Verifier

## Tool Binding
- Module: `forgefactory.paper04_boundary_repair` (lineage)
- CQE Engine: `cqe_engine.formal.verify_boundary_repair` (white-room)

## Required Outputs
- `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`

## Minimum Test
Smoke test producing at least one proof-like row and one obligation-like row.

## Verifier Specification
```python
def verify_boundary_repair() -> dict:
    """Verify T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route.."""
    pass
```

## Usage
```python
from cqe_engine import verify_boundary_repair
result = verify_boundary_repair()
assert result["status"] == "pass"
```