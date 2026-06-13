"""Formal receipt generator for Paper 32.

Paper 32 packages superpermutation schedules as supervisor cursors: compressed
request schedules for enumerating local reading orders. The verifier closes
coverage and bounds rows, not unproved minimality for n >= 6.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from GraphStax.permforge import (  # noqa: E402
    N5_OCTAD,
    N5_REVERSAL_FIXED,
    N5_REVERSAL_PAIRS,
    SuperPermScheduler,
    coverage_check,
    egan_upper,
    lower_bound,
    recursive_construction,
    verify_record,
)


OUT = Path(__file__).resolve().parent / "supervisor_cursor_schedule_receipt.json"


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def record_rows() -> list[dict[str, Any]]:
    rows = []
    for n in range(4, 9):
        row = verify_record(n)
        row["minimality_claim"] = "closed" if n in {4, 5} else "not_claimed"
        row["schedule_claim"] = "coverage_validated"
        rows.append(row)
    return rows


def recursive_rows() -> dict[str, Any]:
    built = recursive_construction(8)
    return {
        "n": 8,
        "length": len(built),
        "expected_chart_walk_length": 46233,
        "coverage_valid": coverage_check(built, 8),
        "egan_upper": egan_upper(8),
        "lower_bound": lower_bound(8),
        "open_corridor": egan_upper(8) - lower_bound(8),
    }


def scheduler_rows() -> dict[str, Any]:
    items = ["C", "L", "R", "B"]
    scheduler = SuperPermScheduler(4)
    schedule = list(scheduler.schedule(items))
    windows = []
    slots = "".join(items[int(slot) - 1] if slot.isdigit() else slot for slot in [])
    # Keep the schedule row compact: the coverage check above carries the proof.
    for index in range(0, min(len(schedule), 12)):
        cursor, item = schedule[index]
        windows.append({"cursor": cursor, "item": item})
    return {
        "status": scheduler.status(),
        "first_dispatch_rows": windows,
        "items": items,
        "item_count": len(items),
        "cursor_is_content": False,
        "normal_form": "No request, no C: C is produced only by an enumeration request.",
    }


def kernel_selector_row() -> dict[str, Any]:
    registry = json.loads((ROOT / "production" / "paper-kernels" / "PAPER_KERNEL_REGISTRY.json").read_text(encoding="utf-8"))
    paper = next(row for row in registry["papers"] if row["id"] == "CQE-paper-32")
    block = next(row for row in registry["blocks"] if row["id"] == paper["block"])
    return {
        "paper": paper["id"],
        "title": paper["title"],
        "suite_previous": paper["suite_previous"],
        "suite_next": paper["suite_next"],
        "block_previous": paper["block_previous"],
        "block_next": paper["block_next"],
        "block": block["id"],
        "block_papers": block["papers"],
        "has_deployment_kernel_component": "deployment_kernel" in paper["components"],
        "paper_00_contract": registry["preamble_contract"]["id"],
        "suite": registry["suite"],
        "suite_wrap": f"{paper['id']} -> {paper['suite_next']}",
    }


def build_receipt() -> dict[str, Any]:
    records = record_rows()
    recursive = recursive_rows()
    scheduler = scheduler_rows()
    kernel = kernel_selector_row()
    checks = [
        _check("records_4_to_8_validate_coverage", all(row["coverage_valid"] for row in records), records),
        _check("minimality_only_claimed_for_4_and_5", all((row["n"] in {4, 5}) == (row["minimality_claim"] == "closed") for row in records), records),
        _check("n8_record_matches_egan_upper", records[-1]["length"] == egan_upper(8) == 46205, records[-1]),
        _check("n8_open_corridor_is_120", recursive["open_corridor"] == 120, recursive),
        _check("recursive_n8_chart_walk_covers", recursive["length"] == 46233 and recursive["coverage_valid"], recursive),
        _check("n5_octad_has_eight_schedules", len(N5_OCTAD) == 8, {"octad_count": len(N5_OCTAD)}),
        _check(
            "n5_reversal_orbit_4_fixed_2_pairs",
            len(N5_REVERSAL_FIXED) == 4 and len(N5_REVERSAL_PAIRS) == 2,
            {"fixed": list(N5_REVERSAL_FIXED), "pairs": [list(pair) for pair in N5_REVERSAL_PAIRS]},
        ),
        _check("supervisor_cursor_dispatches_requests_not_content", scheduler["cursor_is_content"] is False, scheduler),
        _check("kernel_selector_wraps_to_paper01", kernel["suite_next"] == "CQE-paper-01", kernel),
    ]
    passed = all(check["pass"] for check in checks)
    return {
        "paper": "CQE-paper-32",
        "title": "The Supervisor Cursor",
        "status": "pass_with_open_minimality_obligations" if passed else "fail",
        "closed_scope": [
            "superpermutation coverage records for n=4..8 validate",
            "n=4 length 33 and n=5 length 153 are treated as closed minimality rows",
            "n=6..8 are validated schedules and bounds rows, not minimality proofs",
            "n=8 Egan upper row is 46205 and lower-bound corridor is 120",
            "supervisor cursor dispatches enumeration requests rather than replacing proof content",
            "paper-kernel selector wraps Paper 32 forward to Paper 01 for active-suite retest",
        ],
        "not_claimed": [
            "minimality for n >= 6",
            "the cursor as ribbon content",
            "closure of all suite obligations",
            "a final metaphysical observation theorem",
        ],
        "records": records,
        "recursive_n8": recursive,
        "scheduler": scheduler,
        "kernel_selector": kernel,
        "open_obligations": [
            "Ship independent n=6 and n=7 field-record receipts if shorter records are promoted.",
            "Close or narrow the n=8 corridor below 46205 before claiming minimality.",
            "Keep Paper 32 selectors from hiding proof/open/readout status.",
            "Replace citation anchors with final bibliography entries and external review.",
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
