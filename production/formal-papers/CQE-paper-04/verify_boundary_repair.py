#!/usr/bin/env python3
"""Finite verifier for CQE Paper 04, Boundary Repair."""

from __future__ import annotations

import json
from pathlib import Path


AXIS_SHEET = {
    (0, 1, 0): (2, 0),
    (1, 1, 0): (3, 1),
}

CORRECTION_STATES = [(0, 1, 0), (1, 1, 0)]
REQUIRED_FIELDS = {
    "state",
    "axis_sheet",
    "reason",
    "status",
    "next_legal_routes",
    "source_paper",
    "target_paper",
}


def repair_boundary(state: tuple[int, int, int] | dict) -> dict:
    if isinstance(state, dict):
        if REQUIRED_FIELDS.issubset(state):
            return dict(state)
        raise ValueError("untyped failure is not repairable")
    if state not in AXIS_SHEET:
        raise ValueError(f"state {state} is not a Paper 02 correction boundary")
    return {
        "state": list(state),
        "axis_sheet": list(AXIS_SHEET[state]),
        "reason": "Paper 02 correction fired: C and not R",
        "status": "constraint",
        "next_legal_routes": [
            "CQE-paper-05 path-carrier intake",
            "CQE-paper-03 stronger theorem intake",
        ],
        "source_paper": "CQE-paper-04",
        "target_paper": "CQE-paper-05",
    }


def verify() -> dict:
    repaired = [repair_boundary(state) for state in CORRECTION_STATES]
    untyped_rejected = False
    try:
        repair_boundary({"status": "failed"})
    except ValueError:
        untyped_rejected = True

    checks = {
        "consumes_two_paper02_correction_states": len(repaired) == 2,
        "preserves_paper03_coordinates": {
            tuple(row["state"]): tuple(row["axis_sheet"]) for row in repaired
        } == AXIS_SHEET,
        "all_required_fields_present": all(REQUIRED_FIELDS.issubset(row) for row in repaired),
        "constraints_not_proofs": all(row["status"] == "constraint" for row in repaired),
        "next_legal_routes_nonempty": all(row["next_legal_routes"] for row in repaired),
        "repair_is_idempotent": all(repair_boundary(row) == row for row in repaired),
        "untyped_failure_rejected": untyped_rejected,
    }
    return {
        "paper": "CQE-paper-04",
        "theorem": "Typed boundary repair",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "repaired_constraints": repaired,
        "falsifier": {"input": {"status": "failed"}, "accepted": not untyped_rejected},
        "corrected_claim": (
            "Boundary repair converts failed joins into typed constraints; "
            "it does not promote them directly to proof."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("boundary_repair_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
