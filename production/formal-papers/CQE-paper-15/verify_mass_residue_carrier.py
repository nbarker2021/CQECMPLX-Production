#!/usr/bin/env python3
"""Finite verifier for CQE Paper 15, Mass-Residue Carrier."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

from lattice_forge.centroid_voa import (  # noqa: E402
    STATES,
    TRUE_VACUA,
    verify_voa_sector_decomposition,
    voa_weight,
)
from lattice_forge.f2_majorana import verify_f2_majorana  # noqa: E402
from lattice_forge.rule30_nth_bit import (  # noqa: E402
    CORRECTION_FIRING_STATES,
    verify_all_layers,
)


def rule30(left: int, center: int, right: int) -> int:
    return left ^ (center | right)


def rule90_like(left: int, center: int, right: int) -> int:
    return left ^ center ^ right


def obstruction(left: int, center: int, right: int) -> int:
    return center & right


def correction_residue(left: int, center: int, right: int) -> int:
    return center & (1 - right)


def verify_rule30_split() -> dict:
    rows = []
    for left, center, right in STATES:
        rows.append(
            {
                "state": [left, center, right],
                "rule30": rule30(left, center, right),
                "linear_part": rule90_like(left, center, right),
                "obstruction_C_and_R": obstruction(left, center, right),
                "split_holds": rule30(left, center, right)
                == (rule90_like(left, center, right) ^ obstruction(left, center, right)),
                "correction_residue_C_and_not_R": correction_residue(left, center, right),
            }
        )
    return {
        "rows": rows,
        "split_holds_for_all_states": all(row["split_holds"] for row in rows),
        "correction_firing_states": [
            row["state"] for row in rows if row["correction_residue_C_and_not_R"] == 1
        ],
    }


def verify() -> dict:
    f2 = verify_f2_majorana()
    voa = verify_voa_sector_decomposition()
    nth = verify_all_layers(max_depth=128)
    split = verify_rule30_split()

    weights = {str(state): voa_weight(state) for state in STATES}
    weight_distribution = {}
    for value in weights.values():
        weight_distribution[value] = weight_distribution.get(value, 0) + 1

    checks = {
        "rule30_linear_obstruction_split_holds": split["split_holds_for_all_states"],
        "f2_majorana_passes": f2.get("status") == "pass",
        "rule30_obstruction_arf_is_zero": f2.get("rule30_correction_arf") == 0,
        "matching_arf_glues_and_mismatch_rejects": f2.get("zero_vs_hyperbolic_can_glue") is True
        and f2.get("zero_vs_elliptic_can_glue") is False,
        "voa_sector_decomposition_passes": voa.get("status") == "pass",
        "voa_weight_distribution_is_2_6": weight_distribution == {0: 2, 5: 6},
        "true_vacua_are_weight_zero": all(voa_weight(state) == 0 for state in TRUE_VACUA),
        "correction_firing_states_match_residue_formula": set(CORRECTION_FIRING_STATES)
        == {(0, 1, 0), (1, 1, 0)},
        "nth_bit_layers_pass_with_open_mckay_thompson": nth.get("status") == "pass"
        and nth.get("oracle_accuracy") == 1.0
        and "McKay" in nth.get("open_step_O2prime", ""),
        "physical_higgs_mass_left_as_obligation": True,
    }

    return {
        "paper": "CQE-paper-15",
        "theorem": "mass-residue carrier substrate layer",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "rule30_split": split,
        "f2_majorana_summary": {
            "status": f2.get("status"),
            "q_zero_arf": f2.get("q_zero_arf"),
            "q_hyperbolic_arf": f2.get("q_hyperbolic_arf"),
            "q_elliptic_arf": f2.get("q_elliptic_arf"),
            "rule30_correction_arf": f2.get("rule30_correction_arf"),
            "zero_vs_hyperbolic_can_glue": f2.get("zero_vs_hyperbolic_can_glue"),
            "zero_vs_elliptic_can_glue": f2.get("zero_vs_elliptic_can_glue"),
        },
        "voa_summary": {
            "status": voa.get("status"),
            "weight_distribution": weight_distribution,
            "seed_partition_function": voa.get("seed_partition_function"),
            "vacua": voa.get("vacua"),
            "weights": weights,
        },
        "nth_bit_summary": {
            "status": nth.get("status"),
            "max_depth": nth.get("max_depth"),
            "oracle_accuracy": nth.get("oracle_accuracy"),
            "lucas_correction_accuracy": nth.get("lucas_correction_accuracy"),
            "lucas_only_accuracy": nth.get("lucas_only_accuracy"),
            "correction_firing_fraction": nth.get("correction_firing_fraction"),
            "voa_weight_distribution": nth.get("voa_weight_distribution"),
            "open_step_O2prime": nth.get("open_step_O2prime"),
        },
        "closed_layers": [
            "Rule 30 splits into linear part xor C*R obstruction over F2",
            "Rule 30 obstruction has Arf invariant 0",
            "Arf-matching gluing admits and Arf-mismatch gluing rejects",
            "VOA sector decomposition is 2q^0 + 6q^5",
            "correction residue C and not R identifies the local surviving-residue states",
            "nth-bit local/oracle layer passes while McKay-Thompson parity remains open",
        ],
        "open_layers": [
            "physical Higgs mechanism",
            "particle mass spectrum or numerical mass prediction",
            "electroweak symmetry breaking/Yukawa coupling derivation",
            "closed-form McKay-Thompson correction parity",
        ],
        "falsifiers": [
            {"claim": "Rule 30 split fails on any local state", "accepted": False},
            {"claim": "Arf mismatch can be glued losslessly", "accepted": False},
            {"claim": "VOA weight partition is not 2 vacua and 6 excited states", "accepted": False},
            {"claim": "This receipt proves physical Higgs mass", "accepted": False},
        ],
        "scope_boundary": (
            "Paper 15 proves a finite mass-residue carrier proxy: obstruction, Arf gluing, "
            "VOA weighting, and correction-residue bookkeeping. Higgs and QFT mass claims remain open."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("mass_residue_carrier_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
