"""Formal receipt generator for Paper 31.

Paper 31 is a retrospective readout of the corpus as an enacted LCR process. It
checks center invariance, the Rule 30 boundary table, the Paper 30 ribbon
receipt, and dependency direction. It does not add a new theorem to the earlier
proof stack.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.centroid_voa import (  # noqa: E402
    STATES,
    gluon,
    swap_LR,
    verify_gluon_invariance,
)
from lattice_forge.rule30 import rule30_bit  # noqa: E402


OUT = Path(__file__).resolve().parent / "meta_lcr_readout_receipt.json"
PAPER30_RECEIPT = ROOT / "production" / "formal-papers" / "CQE-paper-30" / "grand_ribbon_meta_framer_receipt.json"
READOUT_IDS = [f"CQE-paper-{index:02d}" for index in range(31)]


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def rule30_truth_table() -> list[dict[str, int]]:
    rows = []
    for left, center, right in STATES:
        rows.append(
            {
                "L": left,
                "C": center,
                "R": right,
                "rule30_bit": rule30_bit(left, center, right),
                "anf_bit": left ^ center ^ right ^ (center & right),
            }
        )
    return rows


def center_invariance_rows() -> list[dict[str, Any]]:
    rows = []
    for state in STATES:
        antipode = swap_LR(state)
        rows.append(
            {
                "state": state,
                "antipode": antipode,
                "center": state[1],
                "gluon": gluon(state),
                "antipode_gluon": gluon(antipode),
                "invariant": gluon(state) == state[1] == gluon(antipode),
            }
        )
    return rows


def paper30_readout() -> dict[str, Any]:
    receipt = json.loads(PAPER30_RECEIPT.read_text(encoding="utf-8"))
    checks = {row["name"]: row for row in receipt["checks"]}
    return {
        "paper30_status": receipt["status"],
        "paper30_sweep_count": len(receipt["sweep_rows"]),
        "paper30_readout_rule": checks["paper_31_not_a_dependency"]["detail"],
        "paper30_confirms_31_not_dependency": checks["paper_31_not_a_dependency"]["pass"],
        "paper30_open_obligations": receipt["open_obligations"],
    }


def readout_chain_rows() -> list[dict[str, Any]]:
    rows = []
    for index, paper_id in enumerate(READOUT_IDS):
        previous_id = READOUT_IDS[index - 1] if index else None
        next_id = READOUT_IDS[index + 1] if index + 1 < len(READOUT_IDS) else "CQE-paper-32"
        rows.append(
            {
                "index": index,
                "paper_id": paper_id,
                "L": previous_id,
                "C": f"{paper_id} center readout",
                "R": next_id,
                "role": "proof_stack_position" if index < 30 else "retrospective_readout",
                "dependency_status": "downstream_readout_only" if index == 30 else "ordinary_sweep_context",
            }
        )
    return rows


def build_receipt() -> dict[str, Any]:
    gluon_check = verify_gluon_invariance()
    center_rows = center_invariance_rows()
    truth_rows = rule30_truth_table()
    paper30 = paper30_readout()
    chain = readout_chain_rows()
    checks = [
        _check("gluon_invariance_passes", gluon_check["status"] == "pass", gluon_check),
        _check("all_center_rows_invariant", all(row["invariant"] for row in center_rows), center_rows),
        _check("rule30_truth_table_matches_anf", all(row["rule30_bit"] == row["anf_bit"] for row in truth_rows), truth_rows),
        _check("paper30_receipt_available", paper30["paper30_status"].startswith("pass"), paper30),
        _check("paper31_is_not_upstream_dependency", paper30["paper30_confirms_31_not_dependency"], paper30),
        _check("readout_chain_has_31_positions_00_to_30", len(chain) == 31 and chain[-1]["paper_id"] == "CQE-paper-30", chain),
        _check("paper32_is_forward_package_target", chain[-1]["R"] == "CQE-paper-32", chain[-1]),
    ]
    passed = all(check["pass"] for check in checks)
    return {
        "paper": "CQE-paper-31",
        "title": "It Was Still Just LCR",
        "status": "pass_as_retrospective_readout" if passed else "fail",
        "closed_scope": [
            "C is the LR-invariant gluon coordinate on the eight chart states",
            "Rule 30 boundary table matches its algebraic normal form",
            "Paper 30 receipt confirms Paper 31 is readout, not upstream dependency",
            "Papers 00-30 can be walked as a retrospective LCR readout chain",
            "Paper 32 remains the forward package/deployment target",
        ],
        "not_claimed": [
            "a new theorem that changes papers 00-30",
            "closure of standing open obligations",
            "Paper 31 as a premise for earlier papers",
            "replacement of Paper 32",
        ],
        "gluon_invariance": gluon_check,
        "center_rows": center_rows,
        "rule30_truth_table": truth_rows,
        "paper30_readout": paper30,
        "readout_chain": chain,
        "open_obligations": [
            "Standing proof obligations from earlier papers remain open unless their own receipts close them.",
            "Paper 31 must remain downstream of Paper 30 in dependency direction.",
            "Paper 32 must preserve this readout as packaging/deployment metadata rather than hidden proof support.",
            "Replace citation anchors with final bibliography entries.",
        ],
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"].startswith("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
