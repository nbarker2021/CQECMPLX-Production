# Paper 02 — Tool: Correction Surface Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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
    # 2. Verify exact firing states: (0,1,0) and (1,1,0)
    # 3. Verify D4 projection: (axis,sheet) in {(2,0), (3,1)}
    # 4. Nonlinear residue is structured obligation data, not proof by itself
    # 5. Residue feeds next transport as correction surface
    # Returns: {"status": "pass", "checked": [...]}
    pass
```

## Usage
```python
from cqe_engine import verify_correction_surface
result = verify_correction_surface()
assert result["status"] == "pass"
```
