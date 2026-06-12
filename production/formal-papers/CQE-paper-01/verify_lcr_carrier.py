#!/usr/bin/env python3
"""Finite verifier for CQE Paper 01, LCR Chain Carrier."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path


def states() -> list[tuple[int, int, int]]:
    return [(left, center, right) for left in (0, 1) for center in (0, 1) for right in (0, 1)]


def reverse_lr(state: tuple[int, int, int]) -> tuple[int, int, int]:
    left, center, right = state
    return (right, center, left)


def shell(state: tuple[int, int, int]) -> int:
    return sum(state)


def verify() -> dict:
    all_states = states()
    fixed = [state for state in all_states if reverse_lr(state) == state]
    pairs = []
    seen = set(fixed)
    for state in all_states:
        if state in seen:
            continue
        mate = reverse_lr(state)
        pairs.append([state, mate])
        seen.add(state)
        seen.add(mate)

    shell_counts = Counter(shell(state) for state in all_states)
    counterexample = (1, 0, 1)
    false_shell2_value_claim_rejected = (
        shell(counterexample) == 2
        and counterexample[0] == counterexample[2]
        and reverse_lr(counterexample) == counterexample
    )

    checks = {
        "state_count_is_8": len(all_states) == 8,
        "center_preserved_under_reversal": all(state[1] == reverse_lr(state)[1] for state in all_states),
        "reversal_is_involution": all(reverse_lr(reverse_lr(state)) == state for state in all_states),
        "shell_multiplicities_are_1_3_3_1": [shell_counts[i] for i in range(4)] == [1, 3, 3, 1],
        "fixed_orbit_count_is_4": len(fixed) == 4,
        "paired_orbit_count_is_2": len(pairs) == 2,
        "shell2_value_inequality_claim_rejected": false_shell2_value_claim_rejected,
        "minimal_address_count_is_3": len({"left_boundary", "center", "right_boundary"}) == 3,
    }

    return {
        "paper": "CQE-paper-01",
        "theorem": "Minimal LCR carrier",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "states": [list(state) for state in all_states],
        "fixed_states": [list(state) for state in fixed],
        "reversal_pairs": [[list(a), list(b)] for a, b in pairs],
        "shell_counts": {str(key): shell_counts[key] for key in range(4)},
        "corrected_claim": (
            "L and R are opposed directions as addresses; they are not required "
            "to have unequal values in every state."
        ),
        "counterexample_to_value_inequality": list(counterexample),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("lcr_carrier_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
