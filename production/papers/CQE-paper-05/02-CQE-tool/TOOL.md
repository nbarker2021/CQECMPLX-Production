# Paper 05 — Tool: Oloid Path Carrier Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
    """Verify structural rolling path continuity.

    Checks:
    1. Valid binary input produces a legal adjacent rolling trace.
    2. Every state has a binary head/tail dyad.
    3. Paper 04 constraint payloads can be carried without changing the path rule.
    4. Invalid bits and discontinuous jumps are rejected.
    5. Rule 30 prediction remains out of scope until separately verified.
    """
    pass
```

## Usage
```python
from cqe_engine import verify_oloid_path
result = verify_oloid_path()
assert result["status"] == "pass"
```
