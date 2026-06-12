#!/usr/bin/env python3
"""Finite verifier for CQE Paper 12, CA Prediction Surface."""

from __future__ import annotations

import json
from pathlib import Path


def eca_emit(rule: int, left: int, center: int, right: int) -> int:
    index = (left << 2) | (center << 1) | right
    return (rule >> index) & 1


def rule30(left: int, center: int, right: int) -> int:
    return left ^ (center | right)


def rule90(left: int, right: int) -> int:
    return left ^ right


def correction(left: int, center: int, right: int) -> int:
    return center & (1 - right)


def t_emission(left: int, center: int, right: int) -> int:
    return (1 - left) if center else (left ^ right)


def states() -> list[tuple[int, int, int]]:
    return [(left, center, right) for left in (0, 1) for center in (0, 1) for right in (0, 1)]


def is_silent_boundary(rule: int) -> bool:
    return eca_emit(rule, 0, 0, 0) == 0 and eca_emit(rule, 1, 1, 1) == 0


def verify() -> dict:
    all_states = states()
    rows = []
    for state in all_states:
        left, center, right = state
        local = rule30(left, center, right)
        rows.append(
            {
                "state": list(state),
                "eca_rule30": eca_emit(30, left, center, right),
                "rule30_formula": local,
                "t_emission": t_emission(left, center, right),
                "rule90": rule90(left, right),
                "correction": correction(left, center, right),
                "correction_identity_holds": local
                == (rule90(left, right) ^ correction(left, center, right)),
            }
        )

    silent_rules = [rule for rule in range(256) if is_silent_boundary(rule)]
    checks = {
        "rule30_truth_table_matches_formula": all(
            row["eca_rule30"] == row["rule30_formula"] for row in rows
        ),
        "t_emission_matches_rule30": all(row["t_emission"] == row["rule30_formula"] for row in rows),
        "rule30_rule90_correction_identity_holds": all(
            row["correction_identity_holds"] for row in rows
        ),
        "local_state_count_is_8": len(rows) == 8,
        "silent_boundary_rule_count_is_64": len(silent_rules) == 64,
        "cold_start_rule30_extractor_left_as_obligation": True,
        "spectral_prediction_left_as_empirical": True,
    }
    return {
        "paper": "CQE-paper-12",
        "theorem": "CA prediction surface finite local layers",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "rule30_rows": rows,
        "silent_boundary_rule_count": len(silent_rules),
        "silent_boundary_rules": silent_rules,
        "closed_layers": [
            "Rule 30 local truth table",
            "T_EMISSION local readout",
            "Rule30 = Rule90 xor (C and not R) correction identity",
            "64/256 silent-boundary count",
        ],
        "open_layers": [
            "cold-start full O(log N) Rule 30 extractor",
            "spectral next-state prediction accuracy theorem",
            "case-by-case closure proof for every silent-boundary rule",
        ],
        "falsifiers": [
            {
                "claim": "The spectral layer is a proved cold-start Rule 30 predictor",
                "accepted": False,
            },
            {
                "claim": "A local T_EMISSION receipt proves between-depth dynamics without the local state",
                "accepted": False,
            },
            {
                "claim": "A layer may omit its cost and defect receipt",
                "accepted": False,
            },
        ],
        "scope_boundary": (
            "Paper 12 proves the finite local prediction-surface layers and silent-boundary count; "
            "cold-start extraction and spectral prediction remain explicit obligations."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("ca_prediction_surface_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
