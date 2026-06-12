# Paper 04 — Tool: Boundary Repair Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
    """Verify typed boundary repair.

    Checks:
    1. Paper 02 correction states are consumed.
    2. Paper 03 axis/sheet coordinates are preserved.
    3. Repaired rows contain state, coordinate, reason, status, source, target,
       and next legal routes.
    4. Repaired rows are constraints, not proofs.
    5. Repair is idempotent.
    6. Untyped failures are rejected.
    """
    pass
```

## Usage
```python
from cqe_engine import verify_boundary_repair
result = verify_boundary_repair()
assert result["status"] == "pass"
```
