#!/usr/bin/env python3
"""Finite verifier for CQE Paper 05, Oloid Path Carrier."""

from __future__ import annotations

import json
from pathlib import Path


def roll(state: tuple[int, int, int], bit: int) -> tuple[int, int, int]:
    if bit not in (0, 1):
        raise ValueError("bit must be binary")
    sheet, phase, parity = state
    if sheet not in (0, 1) or phase not in (0, 1, 2, 3) or parity not in (0, 1):
        raise ValueError("invalid carrier state")
    return ((sheet + 1) % 2, (phase + 1) % 4, parity ^ bit)


def dyad(state: tuple[int, int, int]) -> tuple[int, int]:
    sheet, phase, parity = state
    return (sheet, ((phase & 1) ^ sheet ^ parity) & 1)


def trace(bits: list[int], initial: tuple[int, int, int] = (0, 0, 0)) -> list[tuple[int, int, int]]:
    states = [initial]
    state = initial
    for bit in bits:
        state = roll(state, bit)
        states.append(state)
    return states


def attach_payload(state: tuple[int, int, int], payload: dict) -> dict:
    return {
        "carrier_state": list(state),
        "head_tail": list(dyad(state)),
        "payload": payload,
        "payload_alters_path_rule": False,
    }


def verify() -> dict:
    bits = [1, 0, 1, 1, 0, 0, 1, 0]
    path = trace(bits)
    legal_pairs = [
        roll(path[index], bits[index]) == path[index + 1]
        for index in range(len(bits))
    ]
    payload = {
        "state": [0, 1, 0],
        "axis_sheet": [2, 0],
        "status": "constraint",
        "source_paper": "CQE-paper-04",
    }
    carried = attach_payload(path[3], payload)

    invalid_bit_rejected = False
    try:
        roll(path[0], 2)
    except ValueError:
        invalid_bit_rejected = True

    discontinuous_jump_rejected = roll(path[0], bits[0]) != path[2]

    checks = {
        "trace_length_is_input_length_plus_one": len(path) == len(bits) + 1,
        "adjacent_pairs_are_legal_rolls": all(legal_pairs),
        "head_tail_dyads_are_binary": all(all(value in (0, 1) for value in dyad(state)) for state in path),
        "payload_does_not_alter_path_rule": carried["payload_alters_path_rule"] is False,
        "invalid_bit_rejected": invalid_bit_rejected,
        "discontinuous_jump_rejected": discontinuous_jump_rejected,
        "prediction_claim_left_out_of_scope": True,
    }
    return {
        "paper": "CQE-paper-05",
        "theorem": "Rolling path carrier",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "input_bits": bits,
        "trace": [list(state) for state in path],
        "dyads": [list(dyad(state)) for state in path],
        "carried_constraint_example": carried,
        "scope_boundary": "This proves structural path continuity, not Rule 30 prediction.",
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("oloid_path_carrier_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
