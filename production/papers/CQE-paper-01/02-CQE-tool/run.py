#!/usr/bin/env python3

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.
"""CQE-paper-01 Smoke Test — LCR Chain Carrier Verifier.

Self-contained. Uses only white-room lib-forge engine and its verifiers.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

# Zero hardcoded paths: resolve white-room root from this file's location.
# This file lives at <root>/papers/CQE-paper-01/02-CQE-tool/run.py
# so root is 4 parents up: papers/ -> CQE-paper-01/ -> 02-CQE-tool/ -> run.py
_HERE = Path(__file__).resolve()
ROOT = Path(os.environ["CQE_ANCHOR"]).resolve() if os.environ.get("CQE_ANCHOR") \
    else _HERE.parent.parent.parent.parent

# Engine and shared-memory are siblings under lib-forge/
sys.path.insert(0, str(ROOT / "lib-forge"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_engine"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_shared_memory"))
import cqe_engine_paths              # noqa: E402,F401
import cqe_shared_memory_paths       # noqa: E402,F401

from cqe_engine import (
    Registry, SlotName, transport, hydrate,
    verify_lcr_bijective,  # to be implemented
)
from cqe_shared_memory import SharedMemory, StreamKind


def main() -> None:
    print("=" * 65)
    print("CQE-PAPER-01 SMOKE TEST — LCR Chain Carrier")
    print("=" * 65)

    # 1) Run paper-specific verifier
    print("\n[1/3] Running LCR bijective verifier...")
    result = verify_lcr_bijective()
    assert result["status"] == "pass", f"LCR verifier failed: {result}"
    print(f"    LCR bijective: {result['status']} (checks: {result.get('checked', 'N/A')})")

    # 2) Smoke test the engine ribbon transport (Paper 01 tool binding)
    print("\n[2/3] Running engine ribbon transport...")
    reg = Registry(root=ROOT)
    paper = reg.get("CQE-paper-01")
    
    new_fills = {
        SlotName.B: ("LCR chain carrier rule", "paper01 spec", "binary+vector"),
        SlotName.L: ("left boundary: L readout", str(ROOT / "papers" / "CQE-paper-01" / "01-CQE-formal" / "FORMAL.md"), "binary"),
        SlotName.R: ("right boundary: R readout", str(ROOT / "papers" / "CQE-paper-01" / "03-CQE-workbook" / "WORKBOOK.md"), "binary"),
        SlotName.W: ("supplemental workbook analogue", str(ROOT / "papers" / "CQE-paper-01" / "03-CQE-workbook" / "WORKBOOK.md"), "vector"),
    }
    out_ribbon, receipt = transport(paper.ribbon, tool="paper01-lcr-carrier", new_fills=new_fills, paper_id="CQE-paper-01")
    
    # Verify obligation delta closed B, L, R, W (C and A are default-filled)
    assert sorted(receipt.obligation_delta["closed"]) == ["B", "L", "R", "W"]
    assert receipt.obligation_delta["opened"] == []
    print(f"    Transport OK: closed {receipt.obligation_delta['closed']}")

    # 3) Verify hydration leaves only T and O obligated (6 of 8 slots filled)
    print("\n[3/3] Verifying hydration...")
    h = hydrate("CQE-paper-01", out_ribbon)
    # Default arity fills C (center/title) + A (citation-anchor/INTENT.md).
    # This transport closes B, L, R, W. That leaves exactly T and O obligated.
    assert h.obligated == ["T", "O"], f"Expected ['T', 'O'], got {h.obligated}"
    print(f"    Hydration OK: obligated = {h.obligated}")
    print(f"    Summary: {h.summary()}")

    print("\n" + "=" * 65)
    print("CQE-PAPER-01 SMOKE TEST: PASS")
    print("=" * 65)


if __name__ == "__main__":
    main()
