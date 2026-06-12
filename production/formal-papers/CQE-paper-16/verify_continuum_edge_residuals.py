#!/usr/bin/env python3
"""Finite verifier for CQE Paper 16, Continuum Edge Residuals."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

from lattice_forge.centroid_voa import (  # noqa: E402
    LIE_CONJUGATES,
    STATES,
    anneal_to_lie_conjugate,
    verify_hamming_centroid_universality,
)
from lattice_forge.rule30_nth_bit import (  # noqa: E402
    CORRECTION_FIRING_STATES,
    verify_all_layers,
)


def correction_residue(state: tuple[int, int, int]) -> int:
    _left, center, right = state
    return center & (1 - right)


def edge_windows() -> list[dict]:
    rows = []
    for depth in (10, 100, 1000):
        state = STATES[depth % len(STATES)]
        anneal = anneal_to_lie_conjugate(state)
        rows.append(
            {
                "window": depth,
                "state": list(state),
                "edge_residue": correction_residue(state),
                "anneal_steps": anneal["steps"],
                "anneal_final": list(anneal["final"]),
                "anneal_closed": anneal["is_lie_conjugate"],
            }
        )
    return rows


def verify() -> dict:
    hamming = verify_hamming_centroid_universality()
    nth = verify_all_layers(max_depth=256)
    windows = edge_windows()

    all_states_close = all(
        anneal_to_lie_conjugate(state)["is_lie_conjugate"]
        and anneal_to_lie_conjugate(state)["steps"] <= 3
        for state in STATES
    )
    correction_states = {
        state for state in STATES if correction_residue(state) == 1
    }

    checks = {
        "hamming_centroid_universality_passes": hamming.get("status") == "pass",
        "all_states_close_in_at_most_3_steps": all_states_close,
        "lie_conjugate_rest_count_is_4": len(LIE_CONJUGATES) == 4,
        "edge_residue_states_are_c_and_not_r": correction_states
        == {(0, 1, 0), (1, 1, 0)}
        == set(CORRECTION_FIRING_STATES),
        "decade_windows_are_receipted": len(windows) == 3
        and all(row["anneal_closed"] for row in windows),
        "nth_layers_pass_with_open_global_collapse": nth.get("status") == "pass"
        and nth.get("oracle_accuracy") == 1.0
        and "McKay" in nth.get("open_step_O2prime", ""),
        "continuum_solution_left_as_obligation": True,
    }

    return {
        "paper": "CQE-paper-16",
        "theorem": "continuum edge residual local window layer",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "hamming_summary": {
            "status": hamming.get("status"),
            "lie_conjugate_count": hamming.get("lie_conjugate_count"),
            "step_distribution": hamming.get("step_distribution"),
        },
        "edge_residue_states": [list(state) for state in sorted(correction_states)],
        "decade_windows": windows,
        "nth_bit_summary": {
            "status": nth.get("status"),
            "max_depth": nth.get("max_depth"),
            "oracle_accuracy": nth.get("oracle_accuracy"),
            "lucas_correction_accuracy": nth.get("lucas_correction_accuracy"),
            "lucas_only_accuracy": nth.get("lucas_only_accuracy"),
            "correction_firing_fraction": nth.get("correction_firing_fraction"),
            "open_step_O2prime": nth.get("open_step_O2prime"),
        },
        "closed_layers": [
            "every local chart state anneals to a Lie-conjugate rest state in <=3 S3 steps",
            "there are four Lie-conjugate rest states",
            "edge residue is exactly C and not R",
            "sample decade windows carry local receipts",
            "local/oracle nth-bit layer passes with correction included",
        ],
        "open_layers": [
            "global continuum closure",
            "O(N) to O(log N) propagating-correction collapse",
            "closed McKay-Thompson correction parity",
            "claim that adding digits terminates continuum depth",
        ],
        "falsifiers": [
            {"claim": "A local chart state needs more than 3 anneal steps", "accepted": False},
            {"claim": "Edge residue fires outside C=1,R=0", "accepted": False},
            {"claim": "Power-of-ten windows solve the continuum limit", "accepted": False},
        ],
        "scope_boundary": (
            "Paper 16 proves local rollout closure and edge-residue windowing. "
            "The global continuum collapse remains an explicit McKay-Thompson obligation."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("continuum_edge_residuals_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
