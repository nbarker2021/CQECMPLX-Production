#!/usr/bin/env python3
"""CQE-paper-03 Smoke Test — D4/J3 Triality Verifier."""
from __future__ import annotations
import os, sys
from pathlib import Path

_HERE = Path(__file__).resolve()
ROOT = Path(os.environ["CQE_ANCHOR"]).resolve() if os.environ.get("CQE_ANCHOR") \
    else _HERE.parent.parent.parent.parent

sys.path.insert(0, str(ROOT / "lib-forge"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_engine"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_shared_memory"))
import cqe_engine_paths, cqe_shared_memory_paths  # noqa: E402,F401

from cqe_engine import Registry, SlotName, transport, hydrate, verify_triality
from cqe_shared_memory import SharedMemory, StreamKind

def main():
    print("=" * 65)
    print("CQE-PAPER-03 SMOKE TEST — D4/J3 Triality")
    print("=" * 65)

    print("\n[1/3] Running triality verifier...")
    result = verify_triality()
    assert result["status"] == "pass", f"Triality failed: {result}"
    print(f"    T_TRIALITY: {result['status']} (checks: {result.get('checked', 'N/A')})")

    print("\n[2/3] Running engine ribbon transport...")
    reg = Registry(root=ROOT)
    paper = reg.get("CQE-paper-03")
    new_fills = {
        SlotName.B: ("triality rule", "paper03 spec", "binary+vector"),
        SlotName.L: ("left boundary", str(ROOT / "papers" / "CQE-paper-03" / "01-CQE-formal" / "FORMAL.md"), "binary"),
        SlotName.R: ("right boundary", str(ROOT / "papers" / "CQE-paper-03" / "03-CQE-workbook" / "WORKBOOK.md"), "binary"),
        SlotName.W: ("workbook analogue", str(ROOT / "papers" / "CQE-paper-03" / "03-CQE-workbook" / "WORKBOOK.md"), "vector"),
    }
    out_ribbon, receipt = transport(paper.ribbon, tool="paper03-triality", new_fills=new_fills, paper_id="CQE-paper-03")
    assert sorted(receipt.obligation_delta["closed"]) == ["B", "L", "R", "W"]
    assert receipt.obligation_delta["opened"] == []
    print(f"    Transport OK: closed {receipt.obligation_delta['closed']}")

    print("\n[3/3] Verifying hydration...")
    h = hydrate("CQE-paper-03", out_ribbon)
    assert h.obligated == ["T", "O"], f"Expected ['T', 'O'], got {h.obligated}"
    print(f"    Hydration OK: obligated = {h.obligated}")
    print(f"    Summary: {h.summary()}")

    print("\n" + "=" * 65)
    print("CQE-PAPER-03 SMOKE TEST: PASS")
    print("=" * 65)

if __name__ == "__main__":
    main()
