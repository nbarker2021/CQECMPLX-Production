#!/usr/bin/env python3

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.
"""CQE-paper-04 Smoke Test — Boundary Repair Verifier."""
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

from cqe_engine import Registry, SlotName, transport, hydrate, verify_boundary_repair
from cqe_shared_memory import SharedMemory, StreamKind

def main():
    print("=" * 65)
    print("CQE-PAPER-04 SMOKE TEST — Boundary Repair")
    print("=" * 65)

    print("\n[1/3] Running verify_boundary_repair...")
    result = verify_boundary_repair()
    assert result["status"] == "pass", f"{verifier_name} failed: {result}"
    print(f"    T_BOUNDARY_REPAIR: Failed joins become typed constraints for the next legal route.: {result['status']} (checks: {result.get('checked', 'N/A')})")

    print("\n[2/3] Running engine ribbon transport...")
    reg = Registry(root=ROOT)
    paper = reg.get("CQE-paper-04")
    new_fills = {
        SlotName.B: ("boundary repair rule", "paper04 spec", "binary+vector"),
        SlotName.L: ("left boundary", str(ROOT / "papers" / "CQE-paper-04" / "01-CQE-formal" / "FORMAL.md"), "binary"),
        SlotName.R: ("right boundary", str(ROOT / "papers" / "CQE-paper-04" / "03-CQE-workbook" / "WORKBOOK.md"), "binary"),
        SlotName.W: ("supplemental workbook analogue", str(ROOT / "papers" / "CQE-paper-04" / "03-CQE-workbook" / "WORKBOOK.md"), "vector"),
    }
    out_ribbon, receipt = transport(paper.ribbon, tool="paper04-boundary-repair", new_fills=new_fills, paper_id="CQE-paper-04")
    assert sorted(receipt.obligation_delta["closed"]) == ["B", "L", "R", "W"]
    assert receipt.obligation_delta["opened"] == []
    print(f"    Transport OK: closed {receipt.obligation_delta['closed']}")

    print("\n[3/3] Verifying hydration...")
    h = hydrate("CQE-paper-04", out_ribbon)
    assert h.obligated == ["T", "O"], f"Expected ['T', 'O'], got {h.obligated}"
    print(f"    Hydration OK: obligated = {h.obligated}")
    print(f"    Summary: {h.summary()}")

    print("\n" + "=" * 65)
    print("CQE-PAPER-04 SMOKE TEST: PASS")
    print("=" * 65)

if __name__ == "__main__":
    main()
