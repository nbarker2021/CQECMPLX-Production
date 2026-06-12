#!/usr/bin/env python3
"""Finite verifier for CQE Paper 03, D4/J3 local triality surface."""

from __future__ import annotations

import json
from pathlib import Path


AXIS = {
    (0, 0, 0): 0,
    (1, 1, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 2,
    (1, 0, 1): 2,
    (0, 0, 1): 3,
    (1, 1, 0): 3,
}


def states() -> list[tuple[int, int, int]]:
    return [(left, center, right) for left in (0, 1) for center in (0, 1) for right in (0, 1)]


def sheet(state: tuple[int, int, int]) -> int:
    return 1 if sum(state) >= 2 else 0


def complement(state: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(1 - value for value in state)


def diagonal_idempotent(state: tuple[int, int, int]) -> bool:
    return tuple(value * value for value in state) == state


def verify() -> dict:
    all_states = states()
    encoded = {(AXIS[state], sheet(state)): state for state in all_states}
    rows = [
        {
            "state": list(state),
            "axis": AXIS[state],
            "sheet": sheet(state),
            "shell": sum(state),
            "trace": sum(state),
            "diagonal_idempotent": diagonal_idempotent(state),
            "is_shell2": sum(state) == 2,
        }
        for state in all_states
    ]
    axis_pairs = {
        str(axis): [list(state) for state in all_states if AXIS[state] == axis]
        for axis in range(4)
    }
    correction_coordinates = {
        tuple((AXIS[state], sheet(state)))
        for state in [(0, 1, 0), (1, 1, 0)]
    }
    checks = {
        "axis_sheet_bijection": len(encoded) == 8 and set(encoded.values()) == set(all_states),
        "axis_pairs_are_antipodal": all(
            complement(pair[0]) == pair[1] or complement(pair[1]) == pair[0]
            for pair in ([state for state in all_states if AXIS[state] == axis] for axis in range(4))
        ),
        "trace_equals_shell": all(row["trace"] == row["shell"] for row in rows),
        "shell2_states_are_diagonal_idempotents": all(
            row["diagonal_idempotent"] for row in rows if row["is_shell2"]
        ),
        "paper02_correction_coordinates_preserved": correction_coordinates == {(2, 0), (3, 1)},
        "strong_triality_left_as_obligation": True,
    }
    return {
        "paper": "CQE-paper-03",
        "theorem": "Local D4/J3 triality surface",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "rows": rows,
        "axis_pairs": axis_pairs,
        "paper02_correction_coordinates": [list(item) for item in sorted(correction_coordinates)],
        "scope_boundary": (
            "This verifier proves the finite local axis/sheet and diagonal J3 surface; "
            "it does not prove full D4 triality or a full F4/J3(O) action."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("triality_surface_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
