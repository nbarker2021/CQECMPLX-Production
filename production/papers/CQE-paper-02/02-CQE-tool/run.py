#!/usr/bin/env python3
"""CQE-paper-02 Smoke Test — Correction Surface Verifier.

Self-contained. Uses only white-room lib-forge engine and its verifiers.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
ROOT = Path(os.environ["CQE_ANCHOR"]).resolve() if os.environ.get("CQE_ANCHOR") \
    else _HERE.parent.parent.parent.parent

sys.path.insert(0, str(ROOT / "lib-forge"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_engine"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_shared_memory"))
import cqe_engine_paths              # noqa: E402,F401
import cqe_shared_memory_paths       # noqa: E402,F401

from cqe_engine import (
    Registry, SlotName, transport, hydrate,
    verify_correction_surface,  # to be implemented
)
from cqe_shared_memory import SharedMemory, StreamKind


def main() -> None:
    print("=" * 65)
    print("CQE-PAPER-02 SMOKE TEST — Correction Surface")
    print("=" * 65)

    print("\n[1/3] Running correction surface verifier...")
    result = verify_correction_surface()
    assert result["status"] == "pass", f"Correction surface failed: {result}"
    print(f"    T_CORRECTION: {result['status']} (checks: {result.get('checked', 'N/A')})")

    print("\n[2/3] Running engine ribbon transport...")
    reg = Registry(root=ROOT)
    paper = reg.get("CQE-paper-02")
    
    new_fills = {
        SlotName.B: ("correction surface rule", "paper02 spec", "binary+vector"),
        SlotName.L: ("left boundary: L readout", str(ROOT / "papers" / "CQE-paper-02" / "01-CQE-formal" / "FORMAL.md"), "binary"),
        SlotName.R: ("right boundary: R readout", str(ROOT / "papers" / "CQE-paper-02" / "03-CQE-workbook" / "WORKBOOK.md"), "binary"),
        SlotName.W: ("workbook analogue", str(ROOT / "papers" / "CQE-paper-02" / "03-CQE-workbook" / "WORKBOOK.md"), "vector"),
    }
    out_ribbon, receipt = transport(paper.ribbon, tool="paper02-correction", new_fills=new_fills, paper_id="CQE-paper-02")
    
    assert sorted(receipt.obligation_delta["closed"]) == ["B", "L", "R", "W"]
    assert receipt.obligation_delta["opened"] == []
    print(f"    Transport OK: closed {receipt.obligation_delta['closed']}")

    print("\n[3/3] Verifying hydration...")
    h = hydrate("CQE-paper-02", out_ribbon)
    assert h.obligated == ["T", "O"], f"Expected ['T', 'O'], got {h.obligated}"
    print(f"    Hydration OK: obligated = {h.obligated}")
    print(f"    Summary: {h.summary()}")

    print("\n" + "=" * 65)
    print("CQE-PAPER-02 SMOKE TEST: PASS")
    print("=" * 65)


if __name__ == "__main__":
    main()
