#!/usr/bin/env python3
"""CQE-paper-00 Smoke Test — runs foundation verifiers.

This is the self-contained smoke test for Paper 00 (Foundation).
It does not depend on the airlock, lineage ForgeFactory, or MCP.
It uses only the white-room lib-forge engine and its verifiers.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

# Zero hardcoded paths: resolve white-room root from this file's location.
# This file lives at <root>/papers/CQE-paper-00/02-CQE-tool/run.py
# so root is 4 parents up: papers/ -> CQE-paper-00/ -> 02-CQE-tool/ -> run.py
_HERE = Path(__file__).resolve()
ROOT = Path(os.environ["CQE_ANCHOR"]).resolve() if os.environ.get("CQE_ANCHOR") \
    else _HERE.parent.parent.parent.parent

# Engine and shared-memory are siblings under lib-forge/
# Also add lib-forge itself so foundation.py can find lattice_forge src
sys.path.insert(0, str(ROOT / "lib-forge"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_engine"))
sys.path.insert(0, str(ROOT / "lib-forge" / "cqe_shared_memory"))
import cqe_engine_paths              # noqa: E402,F401
import cqe_shared_memory_paths       # noqa: E402,F401

from cqe_engine import (
    verify_all_foundations,
    verify_T3_chart_j3o_isomorphism,
    verify_T4_n3_closure_exact,
    verify_T5_M3_idempotent,
    verify_T6_trace_blocks,
    verify_T7_8x8_transition_exact,
    _norm_status,
)
from cqe_engine import Registry, SlotName, transport, hydrate


def main() -> None:
    print("=" * 65)
    print("CQE-PAPER-00 SMOKE TEST — Foundation Verifiers")
    print("=" * 65)

    # 1) Run all foundation verifiers (T3-T7)
    print("\n[1/3] Running foundation verifiers (T3-T7)...")
    result = verify_all_foundations()
    assert result["status"] == "pass", f"Foundation verifiers failed: {result}"
    print(f"    T3 (chart↔J₃(O)): {result['T3']['status']} ({result['T3'].get('total_depths_checked', result['T3'].get('total_checks', '?'))} checks)")
    print(f"    T4 (n=3 SU(3)):   {result['T4']['status']} (residual ℚ = {result['T4'].get('residual_squared_exact', result['T4'].get('residual_Q', '0'))})")
    print(f"    T5 (M₃²=M₃):      {_norm_status(result['T5'])} (idempotent = {result['T5'].get('closed_at_a_scale', result['T5'].get('is_exact_s3_element', '?'))})")
    print(f"    T6 (trace blocks): {_norm_status(result['T6'])} (identical = {result['T6'].get('trace1_is_exact_s3_element', result['T6'].get('trace2_is_exact_s3_element', '?'))})")
    print(f"    T7 (8×8 trans):    {_norm_status(result['T7'])} (entries = {result['T7'].get('entry_set', '?')})")

    # 2) Smoke test the engine ribbon transport (Paper 00 tool binding)
    print("\n[2/3] Running engine ribbon transport...")
    reg = Registry(root=ROOT)
    paper = reg.get("CQE-paper-00")
    
    # Transport a minimal fill (simulates the paper's tool execution)
    new_fills = {
        SlotName.B: ("b rule", str(ROOT / "lib-forge" / "cqe_engine" / "cqe_engine_paths.py"), "binary+vector"),
        SlotName.L: ("left", str(ROOT / "_meta" / "HAMILTONIAN_SOURCE.md"), "binary"),
        SlotName.R: ("right", str(ROOT / "proof-receipts" / "CQE-paper-00"), "binary"),
        SlotName.W: ("workbook", str(ROOT / "papers" / "CQE-paper-00" / "03-CQE-workbook" / "WORKBOOK.md"), "vector"),
    }
    out_ribbon, receipt = transport(paper.ribbon, tool="paper00-foundation", new_fills=new_fills, paper_id="CQE-paper-00")
    
    # Verify obligation delta closed B, L, R, W (C and A are default-filled)
    assert sorted(receipt.obligation_delta["closed"]) == ["B", "L", "R", "W"]
    assert receipt.obligation_delta["opened"] == []
    print(f"    Transport OK: closed {receipt.obligation_delta['closed']}")

    # 3) Verify hydration leaves only T and O obligated (6 of 8 slots filled)
    print("\n[3/3] Verifying hydration...")
    h = hydrate("CQE-paper-00", out_ribbon)
    # Default arity fills C (center/title) + A (citation-anchor).
    # This transport closes B, L, R, W. That leaves exactly T and O obligated.
    assert h.obligated == ["T", "O"], f"Expected ['T', 'O'], got {h.obligated}"
    print(f"    Hydration OK: obligated = {h.obligated}")
    print(f"    Summary: {h.summary()}")

    print("\n" + "=" * 65)
    print("CQE-PAPER-00 SMOKE TEST: PASS")
    print("=" * 65)


if __name__ == "__main__":
    main()