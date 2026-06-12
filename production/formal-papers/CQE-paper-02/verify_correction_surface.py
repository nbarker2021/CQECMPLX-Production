#!/usr/bin/env python3
"""Finite verifier for CQE Paper 02, Correction Surface."""

from __future__ import annotations

import json
from pathlib import Path


AXIS_SHEET = {
    (0, 0, 0): (0, 0),
    (0, 0, 1): (1, 1),
    (0, 1, 0): (2, 0),
    (0, 1, 1): (3, 1),
    (1, 0, 0): (1, 0),
    (1, 0, 1): (2, 1),
    (1, 1, 0): (3, 1),
    (1, 1, 1): (0, 1),
}


def states() -> list[tuple[int, int, int]]:
    return [(left, center, right) for left in (0, 1) for center in (0, 1) for right in (0, 1)]


def rule30(left: int, center: int, right: int) -> int:
    return left ^ (center | right)


def rule90(left: int, right: int) -> int:
    return left ^ right


def correction(left: int, center: int, right: int) -> int:
    return center & (1 - right)


def verify() -> dict:
    all_states = states()
    rows = []
    for state in all_states:
        left, center, right = state
        corr = correction(left, center, right)
        rows.append(
            {
                "state": list(state),
                "rule30": rule30(left, center, right),
                "rule90": rule90(left, right),
                "correction": corr,
                "identity_holds": rule30(left, center, right) == (rule90(left, right) ^ corr),
                "axis_sheet": list(AXIS_SHEET[state]),
            }
        )

    firing_states = [tuple(row["state"]) for row in rows if row["correction"] == 1]
    firing_axis_sheets = {tuple(row["axis_sheet"]) for row in rows if row["correction"] == 1}
    ledger_rows = [
        {
            "state": row["state"],
            "residue": row["correction"],
            "status": "obligation" if row["correction"] else "closed",
            "next_route": "Paper 03 triality intake" if row["correction"] else None,
        }
        for row in rows
    ]

    checks = {
        "state_count_is_8": len(all_states) == 8,
        "identity_holds_for_all_states": all(row["identity_holds"] for row in rows),
        "firing_states_exact": set(firing_states) == {(0, 1, 0), (1, 1, 0)},
        "d4_projection_exact": firing_axis_sheets == {(2, 0), (3, 1)},
        "nonzero_residue_is_obligation_not_proof": all(
            row["status"] == "obligation" for row in ledger_rows if row["residue"] == 1
        ),
    }

    return {
        "paper": "CQE-paper-02",
        "theorem": "Correction surface decomposition",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "rows": rows,
        "firing_states": [list(state) for state in firing_states],
        "firing_axis_sheets": [list(item) for item in sorted(firing_axis_sheets)],
        "ledger_rows": ledger_rows,
        "corrected_claim": "A correction is positive data only when recorded as typed, replayable residue.",
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("correction_surface_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
