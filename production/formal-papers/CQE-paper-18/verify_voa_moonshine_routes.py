"""Paper 18 verifier: VOA/Moonshine representation-route receipts."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(SRC))

from lattice_forge.centroid_voa import (  # noqa: E402
    verify_centroid_voa_chain,
    verify_voa_sector_decomposition,
    verify_z4_period_template,
)
from lattice_forge.mckay_matrix_tables import verify_mckay_matrix_bootstrap  # noqa: E402
from lattice_forge.monster_d4_lift_claim import verify_monster_d4_lift_claim  # noqa: E402
from lattice_forge.voa_lookup import (  # noqa: E402
    MONSTER_SCALAR,
    architecture_summary,
    correction_class_for,
    correction_via_voa,
    mckay_thompson_coefficient_parity,
    verify_voa_lookup_harness,
)


def _jsonable_architecture() -> dict:
    arch = architecture_summary()
    arch["correction_firing_classes"] = {
        str(k): v for k, v in arch.get("correction_firing_classes", {}).items()
    }
    return arch


def main() -> dict:
    sector = verify_voa_sector_decomposition()
    z4 = verify_z4_period_template()
    chain = verify_centroid_voa_chain()
    matrix = verify_mckay_matrix_bootstrap()
    lookup = verify_voa_lookup_harness(max_depth=128)
    monster_d4 = verify_monster_d4_lift_claim(max_depth=128)
    arch = _jsonable_architecture()

    correction_exception = None
    try:
        correction_via_voa(10, 0)
    except NotImplementedError as exc:
        correction_exception = type(exc).__name__

    parity_rows = {
        g: [mckay_thompson_coefficient_parity(g, k) for k in range(1, 10)]
        for g in ["1A", "2A", "3A", "5A", "7A"]
    }

    checks = {
        "centroid_voa_chain_passes": chain.get("status") == "pass",
        "seed_partition_is_2q0_plus_6q5": sector.get("status") == "pass"
        and sector.get("weight_distribution") == {0: 2, 5: 6}
        and sector.get("seed_partition_function") == "Z(q) = 2q^0 + 6q^5",
        "z4_template_is_2_fixed_6_period4": z4.get("status") == "pass"
        and z4.get("fixed_point_count") == 2
        and z4.get("period_2_count") == 0
        and z4.get("period_4_count") == 6,
        "monster_scalar_is_196883": MONSTER_SCALAR == 196883
        and arch.get("monster_scalar_factorization") == "47 * 59 * 71",
        "bounded_mckay_matrix_bootstrap_passes": matrix.get("status") == "pass"
        and matrix.get("honesty_label") == "BOUNDED_EXEC"
        and matrix.get("3A_9x9_a1_is_783") is True
        and matrix.get("2A_9x9_a1_is_4372") is True,
        "lookup_harness_is_bounded_and_deferred": lookup.get("status") == "pass"
        and lookup.get("mckay_thompson_implemented") is True
        and lookup.get("correction_via_voa_implemented") is False
        and lookup.get("trigger_status") == "WP-MOONSHINE-DEFERRED",
        "correction_class_hypothesis_registered": correction_class_for(2, 0) == "2A"
        and correction_class_for(3, 1) == "3A"
        and correction_class_for(1, 0) is None,
        "correction_via_voa_remains_open": correction_exception == "NotImplementedError",
        "monster_d4_lift_bounded_open_gap_passes": monster_d4.get("status")
        == "pass_with_open_gaps"
        and monster_d4.get("honesty_label") == "BOUNDED_EXEC"
        and monster_d4.get("checks", {}).get("all_eight_chart_states_enumerated") is True
        and monster_d4.get("checks", {}).get("d4_lift_all_n_after_activation") is True
        and monster_d4.get("checks", {}).get("g2_f4_route_within_3_moves") is True,
    }

    receipt = {
        "paper": "CQE Paper 18",
        "title": "VOA / Moonshine Representation Routes",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "closed_layers": [
            "finite centroid VOA sector decomposition 2q^0 + 6q^5",
            "static Z4 route template with 2 fixed points and 6 period-4 states",
            "Monster scalar 196883 factorization 47 * 59 * 71",
            "bounded McKay matrix bootstrap for 1A,2A,3A,5A,7A",
            "registered correction-class hypothesis for (2,0)->2A and (3,1)->3A",
            "bounded Monster-D4 lift after all eight chart states activate",
        ],
        "open_layers": [
            "correction_via_voa implementation",
            "full McKay-Thompson arithmetic beyond bounded tables",
            "Rule 30 O(log N) extractor through the route",
            "full Moonshine identification of the finite chart seed",
            "physical representation theorem beyond the route receipts",
        ],
        "falsifiers": [
            "seed partition differs from 2q^0 + 6q^5",
            "Z4 template has period-2 states or does not split 2+6",
            "bounded McKay matrix bootstrap fails",
            "lookup harness is promoted despite WP-MOONSHINE-DEFERRED",
            "correction_via_voa is claimed complete",
        ],
        "source_receipts": {
            "sector": sector,
            "z4": z4,
            "chain": chain,
            "mckay_matrix_bootstrap": matrix,
            "voa_lookup_harness": lookup,
            "monster_d4_lift": monster_d4,
            "architecture": arch,
            "parity_rows_k1_to_k9": parity_rows,
            "correction_via_voa_exception": correction_exception,
        },
    }

    out_path = Path(__file__).with_name("voa_moonshine_routes_receipt.json")
    out_path.write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "checks": checks}, indent=2))
    return receipt


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result["status"] == "pass" else 1)
