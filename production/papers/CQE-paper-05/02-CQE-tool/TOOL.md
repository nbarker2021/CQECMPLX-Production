# Paper 05 — Tool: Oloid Path Carrier Verifier

## Tool Binding
- Module: `forgefactory.paper05_oloid_path_carrier` (lineage)
- CQE Engine: `cqe_engine.formal.verify_oloid_path` (white-room)

## Required Outputs
- `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`

## Minimum Test
Smoke test producing at least one proof-like row and one obligation-like row.

## Verifier Specification
```python
def verify_oloid_path() -> dict:
    """Verify T_OLOID_PATH: Curved/rolling carriers preserve continuity without straight-line transport.."""
    pass
```

## Usage
```python
from cqe_engine import verify_oloid_path
result = verify_oloid_path()
assert result["status"] == "pass"
```