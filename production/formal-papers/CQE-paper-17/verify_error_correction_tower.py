"""Paper 17 verifier: E6-E8 error-correction tower receipts.

This verifier intentionally separates proved code/lattice receipts from open
promotion claims. It admits the forced code tower and related root-shell
landing checks; it does not admit the Leech glue action or a W(E8) extractor.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(SRC))

from lattice_forge.lattice_codes import (  # noqa: E402
    verify_extended_hamming_8,
    verify_golay_24,
    verify_hamming_7_fano,
    verify_lattice_code_chain,
    verify_parameter_chain,
    verify_powered_chain,
)
from lattice_forge.transport_obligations import (  # noqa: E402
    verify_niemeier_direct_sum_index_one_landings,
    verify_niemeier_root_shell_profiles,
)


def _dist_as_ints(dist: dict) -> dict[int, int]:
    return {int(k): int(v) for k, v in dist.items()}


def main() -> dict:
    chain = verify_lattice_code_chain()
    parameters = verify_parameter_chain()
    hamming = verify_hamming_7_fano()
    extended = verify_extended_hamming_8()
    golay = verify_golay_24()
    powered = verify_powered_chain()
    direct_sum = verify_niemeier_direct_sum_index_one_landings()
    root_shells = verify_niemeier_root_shell_profiles()

    checks = {
        "full_lattice_code_chain_passes": chain.get("status") == "pass",
        "parameter_chain_passes": parameters.get("status") == "pass"
        and parameters.get("chain") == [1, 3, 7, 8, 24],
        "hamming_7_fano_passes": hamming.get("status") == "pass"
        and hamming.get("codeword_count") == 16
        and hamming.get("min_weight") == 3
        and _dist_as_ints(hamming.get("weight_distribution", {}))
        == {0: 1, 3: 7, 4: 7, 7: 1},
        "extended_hamming_8_passes": extended.get("status") == "pass"
        and extended.get("codeword_count") == 16
        and extended.get("min_weight") == 4
        and extended.get("is_self_dual") is True
        and _dist_as_ints(extended.get("weight_distribution", {})) == {0: 1, 4: 14, 8: 1},
        "golay_24_ingredients_pass": golay.get("status") == "pass"
        and golay.get("generator_count") == 12
        and golay.get("orthogonality_errors") == 0
        and golay.get("leech_construction_proved") is False,
        "powered_nebe_bound_passes": powered.get("status") == "pass"
        and powered.get("powered_chain") == {"1^2": 1, "3^2": 9, "7^2": 49, "8x9": 72}
        and powered.get("sheet_K_bound") == 9
        and powered.get("nebe_extremal_min_norm") == 8,
        "niemeier_e8_cubed_root_shell_landing_passes": direct_sum.get("status") == "pass"
        and direct_sum.get("terminal_ids") == ["Niemeier:E8^3"]
        and direct_sum.get("exact_at_root_shell_level") is True
        and direct_sum.get("semantic_landing_from_n_proved") is False,
        "niemeier_root_shell_profiles_pass": root_shells.get("status") == "pass"
        and root_shells.get("rootful_terminal_count") == 23
        and root_shells.get("rootless_terminal_count") == 1
        and root_shells.get("exact_glue_cosets_proved") is False,
        "leech_glue_action_remains_open": golay.get("leech_construction_proved") is False,
        "w_e8_lookup_extractor_remains_open": True,
    }

    receipt = {
        "paper": "CQE Paper 17",
        "title": "E6-E8 Error-Correction Tower",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "closed_layers": [
            "parameter chain 1,3,7,8,24 passes",
            "Hamming (7,4,3) Fano-plane rung passes",
            "extended Hamming (8,4,4) self-dual doubly-even E8 seed passes",
            "Golay (24,12,8) ingredient layer and 3x8 carrier geometry pass",
            "powered chain 1,9,49,72 and Nebe 72 K-bound pass",
            "Niemeier E8^3 determinant-one direct-sum root-shell landing passes",
            "rank-24 root-shell profile registry passes at bounded profile level",
        ],
        "open_layers": [
            "rootless Leech overlattice glue action",
            "semantic map from an arbitrary N to a Niemeier terminal",
            "W(E8) lookup table or sub-O(N) extractor",
            "physical error-correction theorem beyond the verified code tower",
        ],
        "falsifiers": [
            "any rung reports status other than pass",
            "Hamming weight distribution differs from 0:1,3:7,4:7,7:1",
            "extended Hamming is not self-dual or has minimum weight other than 4",
            "Golay ingredient verification silently promotes Leech construction",
            "Niemeier direct-sum landing claims semantic N-to-terminal proof",
        ],
        "source_receipts": {
            "chain": chain,
            "parameters": parameters,
            "hamming_7_fano": hamming,
            "extended_hamming_8": extended,
            "golay_24": golay,
            "powered_chain": powered,
            "niemeier_direct_sum_index_one": direct_sum,
            "niemeier_root_shell_profiles": {
                "status": root_shells.get("status"),
                "rootful_terminal_count": root_shells.get("rootful_terminal_count"),
                "rootless_terminal_count": root_shells.get("rootless_terminal_count"),
                "all_rootful_ranks_are_24": root_shells.get("all_rootful_ranks_are_24"),
                "all_declared_coxeter_numbers_match": root_shells.get(
                    "all_declared_coxeter_numbers_match"
                ),
                "all_required_indices_are_integral": root_shells.get(
                    "all_required_indices_are_integral"
                ),
                "exact_glue_cosets_proved": root_shells.get("exact_glue_cosets_proved"),
                "scope": root_shells.get("scope"),
            },
        },
    }

    out_path = Path(__file__).with_name("error_correction_tower_receipt.json")
    out_path.write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "checks": checks}, indent=2))
    return receipt


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result["status"] == "pass" else 1)
