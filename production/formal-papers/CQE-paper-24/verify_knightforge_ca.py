"""Formal receipt generator for Paper 24.

Paper 24 closes KnightForge as a finite local-rule cellular-automaton and
frame-operator receipt. It does not claim a solved N-dimensional chess game, an
OEIS identity, or a complete game-theoretic theorem.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.centroid_voa import (  # noqa: E402
    LIE_CONJUGATES,
    STATES,
    anneal_to_lie_conjugate,
    three_conjugate_label,
    verify_centroid_voa_chain,
    verify_hamming_centroid_universality,
    verify_voa_sector_decomposition,
    voa_weight,
)


OUT = Path(__file__).resolve().parent / "knightforge_ca_receipt.json"
BOARD_SIZE = 8
KNIGHT_MOVES = {
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1),
}
LEFT_APPROACHES = {(-2, -1), (-1, -2)}
RIGHT_APPROACHES = {(-2, 1), (-1, 2)}


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _attacks(a: tuple[int, int], b: tuple[int, int]) -> bool:
    return (b[0] - a[0], b[1] - a[1]) in KNIGHT_MOVES


def greedy_knight_receipt(size: int = BOARD_SIZE) -> dict[str, Any]:
    occupied: list[tuple[int, int]] = []
    rows: list[dict[str, Any]] = []
    for y in range(size):
        x_range = range(size) if y % 2 == 0 else range(size - 1, -1, -1)
        for x in x_range:
            cell = (x, y)
            left = int(any((x + dx, y + dy) in occupied for dx, dy in LEFT_APPROACHES))
            right = int(any((x + dx, y + dy) in occupied for dx, dy in RIGHT_APPROACHES))
            blocked = any(_attacks(piece, cell) for piece in occupied)
            center = 0 if blocked else 1
            state = (left, center, right)
            anneal = anneal_to_lie_conjugate(state)
            label = three_conjugate_label(state)
            row = {
                "cell": [x, y],
                "number": len(rows) + 1,
                "L": left,
                "C": center,
                "R": right,
                "blocked": blocked,
                "decision": "occupy" if center else "reject",
                "side": right - left,
                "state": state,
                "anneal_steps": anneal["steps"],
                "attractor": anneal["final"],
                "is_lie_conjugate": anneal["is_lie_conjugate"],
                "frame_label": label,
                "voa_weight": voa_weight(state),
            }
            rows.append(row)
            if center:
                occupied.append(cell)

    attacked_pairs = [
        [list(a), list(b)]
        for i, a in enumerate(occupied)
        for b in occupied[i + 1 :]
        if _attacks(a, b)
    ]
    weight_counts: dict[int, int] = {}
    state_counts: dict[str, int] = {}
    side_counts: dict[int, int] = {}
    for row in rows:
        weight_counts[row["voa_weight"]] = weight_counts.get(row["voa_weight"], 0) + 1
        state_counts[str(row["state"])] = state_counts.get(str(row["state"]), 0) + 1
        side_counts[row["side"]] = side_counts.get(row["side"], 0) + 1

    return {
        "board_size": size,
        "cell_count": size * size,
        "occupied_count": len(occupied),
        "rejected_count": size * size - len(occupied),
        "occupied_cells": [list(cell) for cell in occupied],
        "non_attacking": not attacked_pairs,
        "attacked_pairs": attacked_pairs,
        "receipt_rows_sample": rows[:16],
        "all_rows_close_to_lie_conjugate": all(row["is_lie_conjugate"] for row in rows),
        "max_anneal_steps": max(row["anneal_steps"] for row in rows),
        "weight_counts": {str(k): v for k, v in sorted(weight_counts.items())},
        "state_counts": state_counts,
        "side_counts": {str(k): v for k, v in sorted(side_counts.items())},
        "frame_labels_sample": {
            str(tuple(row["cell"])): row["frame_label"] for row in rows[:16]
        },
    }


def n_dimensional_frame_operator(dimensions: int = 4) -> dict[str, Any]:
    axis_states = list(STATES[:dimensions])
    axis_labels = [three_conjugate_label(state) for state in axis_states]
    return {
        "dimensions": dimensions,
        "status": "frame_operator_defined",
        "axis_states": axis_states,
        "axis_labels": axis_labels,
        "composite_weight": sum(voa_weight(state) for state in axis_states),
        "closed_game_claim": False,
    }


def build_receipt() -> dict[str, Any]:
    hamming = verify_hamming_centroid_universality()
    voa = verify_voa_sector_decomposition()
    chain = verify_centroid_voa_chain()
    board = greedy_knight_receipt()
    frame_operator = n_dimensional_frame_operator(4)

    checks = [
        _check(
            "centroid annealing universality closes",
            hamming["status"] == "pass"
            and hamming["lie_conjugate_count"] == 4
            and all(
                row["is_lie_conjugate"] and row["steps"] <= 3
                for row in hamming["wrap_table"].values()
            ),
            {
                "status": hamming["status"],
                "lie_conjugate_count": hamming["lie_conjugate_count"],
                "step_distribution": hamming["step_distribution"],
                "lie_conjugates": sorted(list(LIE_CONJUGATES)),
            },
        ),
        _check(
            "VOA sector decomposition is 2 plus 6",
            voa["status"] == "pass"
            and voa["weight_distribution"] == {0: 2, 5: 6}
            and voa["seed_partition_function"] == "Z(q) = 2q^0 + 6q^5",
            {
                "status": voa["status"],
                "weight_distribution": voa["weight_distribution"],
                "seed_partition_function": voa["seed_partition_function"],
                "non_vacua_count": voa["non_vacua_count"],
            },
        ),
        _check(
            "centroid VOA chain passes",
            chain["status"] == "pass"
            and chain["fixed_points"] == 2
            and chain["period_4_states"] == 6,
            chain,
        ),
        _check(
            "finite greedy knight placement is deterministic and non-attacking",
            board["cell_count"] == BOARD_SIZE * BOARD_SIZE
            and board["occupied_count"] > 0
            and board["rejected_count"] > 0
            and board["non_attacking"],
            {
                "board_size": board["board_size"],
                "cell_count": board["cell_count"],
                "occupied_count": board["occupied_count"],
                "rejected_count": board["rejected_count"],
                "attacked_pairs": board["attacked_pairs"],
            },
        ),
        _check(
            "greedy placement rows close under L-conjugate annealing",
            board["all_rows_close_to_lie_conjugate"]
            and board["max_anneal_steps"] <= 3,
            {
                "max_anneal_steps": board["max_anneal_steps"],
                "weight_counts": board["weight_counts"],
                "state_counts": board["state_counts"],
                "side_counts": board["side_counts"],
            },
        ),
        _check(
            "N-dimensional lift is only a frame operator",
            frame_operator["status"] == "frame_operator_defined"
            and not frame_operator["closed_game_claim"]
            and len(frame_operator["axis_labels"]) == frame_operator["dimensions"],
            frame_operator,
        ),
    ]

    open_obligations = [
        {
            "obligation": "OEIS identity",
            "status": "open",
            "reason": "the finite sequence is not claimed identical to any OEIS entry",
        },
        {
            "obligation": "N-dimensional playability",
            "status": "open",
            "reason": "the frame operator is defined, but a complete game is not proven well-posed",
        },
        {
            "obligation": "placement-class to 2+6 orbit validation",
            "status": "open",
            "reason": "the 2+6 sector split is proven for chart states, not every board-pattern class",
        },
        {
            "obligation": "combinatorial game theory review",
            "status": "open",
            "reason": "no domain expert critique is included in the receipt",
        },
    ]

    receipt = {
        "paper": "CQE-paper-24",
        "title": "KnightForge / N-Dimensional Chess Automata",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "Greedy knight placement can be represented as a finite local-rule "
            "CA receipt whose chart states close under L-conjugate centroid "
            "annealing; the N-dimensional extension is a frame operator, not a "
            "solved game."
        ),
        "centroid_substrate": {
            "hamming": {
                "status": hamming["status"],
                "lie_conjugate_count": hamming["lie_conjugate_count"],
                "step_distribution": hamming["step_distribution"],
            },
            "voa": {
                "status": voa["status"],
                "weight_distribution": voa["weight_distribution"],
                "seed_partition_function": voa["seed_partition_function"],
            },
            "chain": chain,
        },
        "greedy_knight": board,
        "n_dimensional_frame_operator": frame_operator,
        "checks": checks,
        "open_obligations": open_obligations,
    }
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["status"] == "pass_with_open_obligations" else 1


if __name__ == "__main__":
    raise SystemExit(main())
