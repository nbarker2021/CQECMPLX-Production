#!/usr/bin/env python3
"""Verifier for CQE Paper 08, Lattice Closure Template."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "packages" / "cqecmplx-forge" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lattice_forge.lattice_codes import (  # noqa: E402
    verify_extended_hamming_8,
    verify_golay_24,
    verify_hamming_7_fano,
    verify_lattice_code_chain,
    verify_powered_chain,
)
from lattice_forge.nebe_gamma72 import verify_nebe_gamma72_contract  # noqa: E402


def verify() -> dict:
    chain = verify_lattice_code_chain()
    fano = verify_hamming_7_fano()
    e8 = verify_extended_hamming_8()
    golay = verify_golay_24()
    powered = verify_powered_chain()
    gamma72 = verify_nebe_gamma72_contract()

    checks = {
        "chain_passes": chain["status"] == "pass",
        "fano_hamming_identity_passes": fano["status"] == "pass"
        and fano["weight_distribution"] == {0: 1, 3: 7, 4: 7, 7: 1}
        and len(fano["weight3_supports"]) == 7,
        "extended_hamming_e8_seed_passes": e8["status"] == "pass"
        and e8["is_self_dual"] is True
        and e8["weight_distribution"] == {0: 1, 4: 14, 8: 1},
        "golay_24_ingredient_passes_without_leech_overclaim": golay["status"] == "pass"
        and golay["orthogonality_errors"] == 0
        and golay["leech_construction_proved"] is False,
        "powered_72_sheet_bound_passes": powered["status"] == "pass"
        and powered["powered_chain"]["8x9"] == 72
        and powered["sheet_K_bound"] == 9
        and powered["nebe_extremal_min_norm"] == 8,
        "gamma72_transport_passes_without_landing_overclaim": gamma72["status"] == "pass"
        and gamma72["all_three_sheet_round_trips_exact"] is True
        and gamma72["gamma72_landing_proved"] is False,
        "leech_landing_overclaim_rejected": golay["leech_construction_proved"] is False,
        "gamma72_landing_overclaim_rejected": gamma72["gamma72_landing_proved"] is False,
    }

    return {
        "paper": "CQE-paper-08",
        "theorem": "Local lattice closure template",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "local_chain": {
            "chain_summary": chain["chain_summary"],
            "tower_correspondence": chain["tower_correspondence"],
            "powered_shortcut": chain["powered_shortcut"],
            "sheet_K_bound": chain["sheet_K_bound"],
        },
        "fano_hamming": {
            "codeword_count": fano["codeword_count"],
            "min_weight": fano["min_weight"],
            "weight_distribution": fano["weight_distribution"],
            "weight3_support_count": len(fano["weight3_supports"]),
        },
        "extended_hamming_e8_seed": {
            "codeword_count": e8["codeword_count"],
            "min_weight": e8["min_weight"],
            "weight_distribution": e8["weight_distribution"],
            "is_self_dual": e8["is_self_dual"],
        },
        "golay_24": {
            "generator_count": golay["generator_count"],
            "orthogonality_errors": golay["orthogonality_errors"],
            "triplet_structure": golay["triplet_structure"],
            "leech_construction_proved": golay["leech_construction_proved"],
        },
        "powered_72": {
            "powered_chain": powered["powered_chain"],
            "sheet_K_bound": powered["sheet_K_bound"],
            "nebe_dim": powered["nebe_dim"],
            "nebe_extremal_min_norm": powered["nebe_extremal_min_norm"],
        },
        "gamma72_contract": {
            "payloads_checked": gamma72["payloads_checked"],
            "all_three_sheet_round_trips_exact": gamma72["all_three_sheet_round_trips_exact"],
            "polarization_matrices_supplied": gamma72["polarization_matrices_supplied"],
            "gamma72_landing_proved": gamma72["gamma72_landing_proved"],
            "scope": gamma72["scope"],
        },
        "falsifiers": [
            {
                "claim": "Golay ingredients alone prove the rootless Leech landing",
                "accepted": False,
            },
            {
                "claim": "three Leech-sheet round trips prove the Gamma72 polarization action",
                "accepted": False,
            },
            {
                "claim": "the chain proves that no other closure template exists",
                "accepted": False,
            },
        ],
        "scope_boundary": (
            "Local lattice closure facts are certified; Leech landing, Gamma72 "
            "polarization, and uniqueness of all possible closure chains remain "
            "outside this theorem."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("lattice_closure_template_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
