# Paper 01 — Tool: LCR Chain Carrier Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Tool Binding
- Module: `forgefactory.paper01_lcr_chain_carrier` (lineage)
- CQE Engine: `cqe_engine.formal.verify_lcr_bijective` (white-room)

## Required Outputs
- `receipt.json` — replayable transport record
- `workbook_sheet.json` — analog sheet encoding
- `example_result.json` — domain example output
- `obligation_ledger.csv` — unresolved residues

## Minimum Test
Smoke test producing at least one proof-like row and one obligation-like row.

## Verifier Specification
```python
def verify_lcr_bijective() -> dict:
    """Verify LCR is the minimal chain carrier preserving center with two opposed boundaries."""
    # 1. Local window: all 8 chart states
    # 2. Center preservation: C = C(swap_LR(s)) for all states
    # 3. Boundary opposition: L and R are distinct addresses, not necessarily unequal values
    # 4. Correction check: shell=2 includes (1,0,1), so a blanket L != R value claim is false
    # 5. Minimality: no smaller carrier exists
    # Returns: {"status": "pass", "checked": [...]}
    pass
```

## Usage
```python
from cqe_engine import verify_lcr_bijective
result = verify_lcr_bijective()
assert result["status"] == "pass"
```
