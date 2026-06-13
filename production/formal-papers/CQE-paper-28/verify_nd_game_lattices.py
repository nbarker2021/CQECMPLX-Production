"""Formal receipt generator for Paper 28.

Paper 28 closes a finite N-dimensional local-rule game-lattice receipt. It
does not claim a general solver for chess, Go, arbitrary games, or arbitrary
dimensions.
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
    anneal_to_lie_conjugate,
    verify_hamming_centroid_universality,
)
from lattice_forge.f4_action import (  # noqa: E402
    S3_PERMUTATIONS,
    S3_PERMUTATION_NAMES,
    s3_permutation_matrices,
    verify_n3_su3_closure_exact,
)
from lattice_forge.lattice_codes import (  # noqa: E402
    verify_extended_hamming_8,
    verify_lattice_code_chain,
)
from lattice_forge.rule30 import rule30_bit  # noqa: E402


OUT = Path(__file__).resolve().parent / "nd_game_lattices_receipt.json"
TRACE2_STATES = ((1, 1, 0), (1, 0, 1), (0, 1, 1))
ADMISSIBLE_DIMENSIONS = {1, 3, 7, 8, 24, 72}


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _apply_perm_to_trace2(state: tuple[int, int, int], perm: tuple[int, int, int]) -> tuple[int, int, int]:
    if state not in TRACE2_STATES:
        raise ValueError(f"state must be a trace-2 state, got {state}")
    active = [index + 1 for index, bit in enumerate(state) if bit == 1]
    moved = {perm[index - 1] for index in active}
    return tuple(1 if index + 1 in moved else 0 for index in range(3))


def move_orbit(state: tuple[int, int, int]) -> list[dict[str, Any]]:
    rows = []
    for name, perm in zip(S3_PERMUTATION_NAMES, S3_PERMUTATIONS):
        target = _apply_perm_to_trace2(state, perm)
        anneal = anneal_to_lie_conjugate(target)
        rows.append(
            {
                "permutation": name,
                "perm": perm,
                "source_state": state,
                "target_state": target,
                "emitted_bit": rule30_bit(*target),
                "anneal_steps": anneal["steps"],
                "anneal_final": anneal["final"],
                "closes_to_lie_conjugate": anneal["final"] in LIE_CONJUGATES,
                "is_identity_carrier": name == "e",
                "carrier_status": "forbidden_logged" if name == "e" else "legal_orbit_move",
            }
        )
    return rows


def robot_game_receipt(dimension: int = 8, start_state: tuple[int, int, int] = (1, 0, 1)) -> dict[str, Any]:
    orbit = move_orbit(start_state)
    unique_targets = sorted({row["target_state"] for row in orbit})
    forbidden = [row for row in orbit if row["carrier_status"] == "forbidden_logged"]
    legal = [row for row in orbit if row["carrier_status"] == "legal_orbit_move"]
    return {
        "game_id": "dimension_8_robot_forbidden_straight_carrier",
        "dimension": dimension,
        "dimension_admissible": dimension in ADMISSIBLE_DIMENSIONS,
        "start_state": start_state,
        "orbit_row_count": len(orbit),
        "unique_target_count": len(unique_targets),
        "unique_targets": unique_targets,
        "legal_move_count": len(legal),
        "forbidden_carrier_count": len(forbidden),
        "all_rows_close": all(row["closes_to_lie_conjugate"] and row["anneal_steps"] <= 3 for row in orbit),
        "max_anneal_steps": max(row["anneal_steps"] for row in orbit),
        "orbit_rows": orbit,
        "closed_game_solver_claim": False,
    }


def build_receipt() -> dict[str, Any]:
    chain = verify_lattice_code_chain()
    hamming8 = verify_extended_hamming_8()
    centroid = verify_hamming_centroid_universality()
    su3 = verify_n3_su3_closure_exact()
    matrices = s3_permutation_matrices()
    robot = robot_game_receipt()
    non_admissible_probe = {
        "dimension": 5,
        "dimension_admissible": 5 in ADMISSIBLE_DIMENSIONS,
        "status": "obligation_not_promoted",
        "reason": "dimension 5 is not in the verified code-tower set",
    }

    checks = [
        _check(
            "forced lattice code chain passes",
            chain["status"] == "pass"
            and set(int(key) for key in chain["chain_summary"].keys()) == {1, 3, 7, 8, 24, 72}
            and chain["powered_chain"] == "pass",
            {
                "status": chain["status"],
                "chain_summary": chain["chain_summary"],
                "tower_correspondence": chain["tower_correspondence"],
                "sheet_K_bound": chain.get("sheet_K_bound"),
            },
        ),
        _check(
            "dimension 8 extended Hamming board passes",
            hamming8["status"] == "pass"
            and hamming8["codeword_count"] == 16
            and hamming8["min_weight"] == 4
            and hamming8["weight_distribution"] == {0: 1, 4: 14, 8: 1},
            {
                "status": hamming8["status"],
                "codeword_count": hamming8["codeword_count"],
                "min_weight": hamming8["min_weight"],
                "weight_distribution": hamming8["weight_distribution"],
            },
        ),
        _check(
            "S3 trace-2 move surface is exact",
            len(S3_PERMUTATIONS) == 6
            and len(matrices) == 6
            and su3["status"] == "pass",
            {
                "s3_permutation_count": len(S3_PERMUTATIONS),
                "matrix_count": len(matrices),
                "su3_status": su3["status"],
                "trace2_is_exact_s3_element": su3.get("trace2_is_exact_s3_element"),
            },
        ),
        _check(
            "finite robot game receipt closes and logs forbidden carrier",
            robot["dimension_admissible"]
            and robot["orbit_row_count"] == 6
            and robot["unique_target_count"] == 3
            and robot["legal_move_count"] == 5
            and robot["forbidden_carrier_count"] == 1
            and robot["all_rows_close"]
            and not robot["closed_game_solver_claim"],
            {
                "dimension": robot["dimension"],
                "orbit_row_count": robot["orbit_row_count"],
                "unique_target_count": robot["unique_target_count"],
                "legal_move_count": robot["legal_move_count"],
                "forbidden_carrier_count": robot["forbidden_carrier_count"],
                "max_anneal_steps": robot["max_anneal_steps"],
            },
        ),
        _check(
            "centroid closure bound covers all chart states",
            centroid["status"] == "pass"
            and centroid["lie_conjugate_count"] == 4
            and all(
                row["is_lie_conjugate"] and row["steps"] <= 3
                for row in centroid["wrap_table"].values()
            ),
            {
                "status": centroid["status"],
                "lie_conjugate_count": centroid["lie_conjugate_count"],
                "step_distribution": centroid["step_distribution"],
            },
        ),
        _check(
            "non-admissible dimension is not promoted",
            non_admissible_probe["dimension_admissible"] is False,
            non_admissible_probe,
        ),
    ]

    open_obligations = [
        {
            "obligation": "general N-dimensional game solver",
            "status": "not_claimed",
            "reason": "the receipt proves finite local-rule orbit closure, not arbitrary game solvability",
        },
        {
            "obligation": "non-code-tower dimensions",
            "status": "open",
            "reason": "dimensions outside 1,3,7,8,24,72 do not inherit this proof surface",
        },
        {
            "obligation": "real-game piece geometry",
            "status": "open",
            "reason": "each real piece type needs its own map into the trace-2/S3 orbit",
        },
        {
            "obligation": "complete game-theoretic theorem",
            "status": "not_claimed",
            "reason": "legal move receipts do not prove strategy, termination, winning states, or fairness",
        },
    ]

    receipt = {
        "paper": "CQE-paper-28",
        "title": "N-Dimensional Game Lattices",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "A finite local-rule game can be represented as a chart operator on "
            "an admissible code-tower lattice dimension: S3 move orbits are "
            "enumerated, Rule 30 local emissions are replayable, forbidden "
            "carriers are logged, and all chart rows anneal to Lie conjugates "
            "within three steps."
        ),
        "lattice_code_chain": chain,
        "extended_hamming_8": hamming8,
        "s3_su3_surface": {
            "status": su3["status"],
            "permutation_count": len(S3_PERMUTATIONS),
            "trace2_is_exact_s3_element": su3.get("trace2_is_exact_s3_element"),
        },
        "robot_game": robot,
        "non_admissible_probe": non_admissible_probe,
        "centroid_closure": {
            "status": centroid["status"],
            "lie_conjugate_count": centroid["lie_conjugate_count"],
            "step_distribution": centroid["step_distribution"],
        },
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
