# Paper 02 — Tool: Correction Surface Verifier

## Tool Binding
- Module: `forgefactory.paper02_correction_surface` (lineage)
- CQE Engine: `cqe_engine.formal.verify_correction_surface` (white-room)

## Required Outputs
- `receipt.json` — replayable transport record
- `workbook_sheet.json` — analog sheet encoding
- `example_result.json` — domain example output
- `obligation_ledger.csv` — unresolved residues

## Minimum Test
Smoke test producing at least one proof-like row and one obligation-like row.

## Verifier Specification
```python
def verify_correction_surface() -> dict:
    """Verify failure/mismatch/residue as positive correction data."""
    # 1. Local window: correction = C ∧ ¬R on chart states
    # 2. Nonlinear residue captured as structured data
    # 3. Residue feeds next transport as correction surface
    # Returns: {"status": "pass", "checked": [...]}
    pass
```

## Usage
```python
from cqe_engine import verify_correction_surface
result = verify_correction_surface()
assert result["status"] == "pass"
```