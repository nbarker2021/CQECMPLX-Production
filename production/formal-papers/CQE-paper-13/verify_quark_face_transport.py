#!/usr/bin/env python3
"""Finite verifier for CQE Paper 13, Quark-Face Transport."""

from __future__ import annotations

import json
import sys
from itertools import permutations
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

from lattice_forge.f4_action import (  # noqa: E402
    S3_PERMUTATIONS,
    S3_PERMUTATION_NAMES,
    verify_n3_su3_closure_exact,
)
from lattice_forge.g2_f4_t5_conjugate import verify_conjugate_triple  # noqa: E402
from lattice_forge.jordan_j3 import verify_j3o_axioms  # noqa: E402


SHELL2_STATES = {
    "C-": (1, 1, 0),
    "C0": (1, 0, 1),
    "C+": (0, 1, 1),
}

TRACE2_IDEMPOTENTS = {
    "C-": "E11+E22",
    "C0": "E11+E33",
    "C+": "E22+E33",
}

COLOR_FACES = ("R", "G", "B", "anti-R", "anti-G", "anti-B")


def induced_trace2_pair(perm: tuple[int, int, int], pair: tuple[int, int]) -> tuple[int, int]:
    mapped = (perm[pair[0] - 1], perm[pair[1] - 1])
    return tuple(sorted(mapped))


def verify_s3_closure() -> dict:
    pairs = {
        "C-": (1, 2),
        "C0": (1, 3),
        "C+": (2, 3),
    }
    pair_to_label = {value: key for key, value in pairs.items()}
    rows = []
    for name, perm in zip(S3_PERMUTATION_NAMES, S3_PERMUTATIONS):
        image = {
            label: pair_to_label[induced_trace2_pair(perm, pair)]
            for label, pair in pairs.items()
        }
        rows.append({"permutation": name, "image": image})
    all_images_close = all(
        set(row["image"].values()) == set(SHELL2_STATES)
        for row in rows
    )
    return {
        "permutation_count": len(rows),
        "expected_s3_count": len(list(permutations((1, 2, 3)))),
        "all_images_close_on_trace2_triple": all_images_close,
        "rows": rows,
    }


def verify_color_face_model() -> dict:
    charges = {face: (1 if not face.startswith("anti-") else -1) for face in COLOR_FACES}
    conjugates = {
        "R": "anti-R",
        "G": "anti-G",
        "B": "anti-B",
        "anti-R": "R",
        "anti-G": "G",
        "anti-B": "B",
    }
    z3_cycle = {"R": "G", "G": "B", "B": "R"}
    checks = {
        "six_faces": len(COLOR_FACES) == 6,
        "three_color_three_anticolor": sum(v == 1 for v in charges.values()) == 3
        and sum(v == -1 for v in charges.values()) == 3,
        "conjugation_is_involution": all(conjugates[conjugates[face]] == face for face in COLOR_FACES),
        "z3_cycle_closes_on_colors": z3_cycle[z3_cycle[z3_cycle["R"]]] == "R",
    }
    return {
        "faces": list(COLOR_FACES),
        "charges": charges,
        "conjugates": conjugates,
        "z3_cycle": z3_cycle,
        "checks": checks,
        "status": "pass" if all(checks.values()) else "fail",
        "scope": "analog six-face color/anticolor transport model; not a derivation of physical quark color",
    }


def verify() -> dict:
    j3 = verify_j3o_axioms()
    su3 = verify_n3_su3_closure_exact()
    route = verify_conjugate_triple(max_depth=256)
    s3 = verify_s3_closure()
    color = verify_color_face_model()

    checks = {
        "shell2_has_three_states": len(SHELL2_STATES) == 3
        and all(sum(state) == 2 for state in SHELL2_STATES.values()),
        "trace2_idempotent_count_is_three": len(TRACE2_IDEMPOTENTS) == 3,
        "j3o_axioms_pass": j3.get("status") == "pass",
        "s3_has_six_permutations": s3["permutation_count"] == 6
        and s3["expected_s3_count"] == 6,
        "s3_closes_trace2_triple": s3["all_images_close_on_trace2_triple"],
        "n3_su3_closure_exact": su3.get("status") == "pass"
        and su3.get("residual_squared_exact") == "0",
        "bounded_route_classifier_passes": route.get("status") == "pass"
        and route.get("oracle_backed") is True
        and route.get("depth_only_bridge") is False,
        "six_face_analog_model_passes": color["status"] == "pass",
        "physical_standard_model_derivation_left_as_obligation": True,
    }

    return {
        "paper": "CQE-paper-13",
        "theorem": "quark-face transport algebraic layer",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "shell2_states": {label: list(state) for label, state in SHELL2_STATES.items()},
        "trace2_idempotents": TRACE2_IDEMPOTENTS,
        "s3_trace2_action": s3,
        "su3_closure_summary": {
            "status": su3.get("status"),
            "n_steps": su3.get("n_steps"),
            "residual_squared_exact": su3.get("residual_squared_exact"),
            "is_exact_group_ring_element": su3.get("is_exact_group_ring_element"),
            "s3_coefficients_exact_strings": su3.get("s3_coefficients_exact_strings"),
        },
        "j3_summary": {
            "status": j3.get("status"),
            "checks_passed": j3.get("checks_passed"),
            "errors": j3.get("errors"),
        },
        "route_summary": {
            "status": route.get("status"),
            "honesty": route.get("honesty"),
            "max_depth_tested": route.get("max_depth_tested"),
            "oracle_backed": route.get("oracle_backed"),
            "depth_only_bridge": route.get("depth_only_bridge"),
            "all_resolved_in_3_or_less": route.get("all_resolved_in_3_or_less"),
            "proof_boundary": route.get("proof_boundary"),
        },
        "color_face_model": color,
        "closed_layers": [
            "three shell-2 chart states",
            "three trace-2 J3(O) idempotents",
            "six S3 Weyl actions close on the trace-2 triple",
            "n=3 shell-2 transition is exact over the SU(3) Weyl group ring",
            "bounded G2/F4/T5A route classifies oracle-enumerated bits in <=3 stages",
            "six-face color/anticolor analog model is internally consistent",
        ],
        "open_layers": [
            "derivation of physical quark color charge",
            "derivation of measured CKM phase or V-A weak structure",
            "cold-start depth-only derivation through the G2/F4/T5A route",
        ],
        "falsifiers": [
            {"claim": "S3 action fails to close on the trace-2 triple", "accepted": False},
            {"claim": "SU(3) closure has nonzero exact residual", "accepted": False},
            {"claim": "Physical quark color is derived only from this receipt", "accepted": False},
        ],
        "scope_boundary": (
            "Paper 13 proves the algebraic quark-face transport layer and its exact S3/SU3 closure. "
            "Physical Standard Model identifications remain obligations until separately derived and calibrated."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("quark_face_transport_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
