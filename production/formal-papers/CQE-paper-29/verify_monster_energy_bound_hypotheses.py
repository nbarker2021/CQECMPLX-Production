"""Formal receipt generator for Paper 29.

Paper 29 is a horizon/quarantine paper. It closes exact arithmetic and finite
VOA partition rows, then proves that physical energy-bound readings are still
unwitnessed hypotheses rather than corpus theorems.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.centroid_voa import (  # noqa: E402
    STATES,
    TRUE_VACUA,
    verify_centroid_voa_chain,
    verify_voa_sector_decomposition,
    voa_weight,
)


OUT = Path(__file__).resolve().parent / "monster_energy_bound_hypotheses_receipt.json"
SUPERSINGULAR_PRODUCT = (47, 59, 71)
MONSTER_REPRESENTATION_DIMENSION = 196883
MCKAY_COEFFICIENT = 196884


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    factor = 3
    while factor * factor <= value:
        if value % factor == 0:
            return False
        factor += 2
    return True


def arithmetic_rows() -> dict[str, Any]:
    product = 1
    for factor in SUPERSINGULAR_PRODUCT:
        product *= factor
    primes = {str(factor): _is_prime(factor) for factor in SUPERSINGULAR_PRODUCT}
    return {
        "supersingular_product": {
            "factors": SUPERSINGULAR_PRODUCT,
            "product": product,
            "expected": MONSTER_REPRESENTATION_DIMENSION,
            "passes": product == MONSTER_REPRESENTATION_DIMENSION and all(primes.values()),
            "prime_checks": primes,
            "claim_scope": "integer arithmetic row only",
        },
        "mckay_decomposition": {
            "trivial_observer": 1,
            "monster_dimension": MONSTER_REPRESENTATION_DIMENSION,
            "sum": 1 + MONSTER_REPRESENTATION_DIMENSION,
            "expected": MCKAY_COEFFICIENT,
            "passes": 1 + MONSTER_REPRESENTATION_DIMENSION == MCKAY_COEFFICIENT,
            "claim_scope": "integer decomposition row only",
        },
    }


def voa_rows() -> dict[str, Any]:
    voa = verify_voa_sector_decomposition()
    chain = verify_centroid_voa_chain()
    weights = {str(state): voa_weight(state) for state in STATES}
    vacua = [str(state) for state in sorted(TRUE_VACUA)]
    excited = [str(state) for state in sorted(set(STATES) - set(TRUE_VACUA))]
    return {
        "voa_partition": {
            "verifier_status": voa["status"],
            "seed_partition_function": voa["seed_partition_function"],
            "weight_distribution": voa["weight_distribution"],
            "weights": weights,
            "vacua": vacua,
            "excited": excited,
            "passes": (
                voa["status"] == "pass"
                and voa["seed_partition_function"] == "Z(q) = 2q^0 + 6q^5"
                and voa["weight_distribution"] == {0: 2, 5: 6}
            ),
            "claim_scope": "finite eight-state chart partition only",
        },
        "centroid_chain": {
            "verifier_status": chain["status"],
            "seed_partition_function": chain["seed_partition_function"],
            "fixed_points": chain["fixed_points"],
            "period_4_states": chain["period_4_states"],
            "chain_conclusion": chain["chain_conclusion"],
            "passes": (
                chain["status"] == "pass"
                and chain["fixed_points"] == 2
                and chain["period_4_states"] == 6
            ),
            "claim_scope": "finite chart identity; no Moonshine transport theorem",
        },
    }


def hypothesis_rows() -> list[dict[str, Any]]:
    return [
        {
            "id": "H1",
            "name": "voa_weight_is_physical_energy",
            "status": "not_claimed",
            "allowed_reading": "VOA weight is an energy analog or wrap-step count.",
            "forbidden_promotion": "VOA weight 5 is a calibrated physical energy gap.",
            "witness_function_present": False,
            "physical_units_present": False,
            "falsifier": "A units-bearing map from wrap steps to joules fails calibration, or no such map is supplied.",
        },
        {
            "id": "H2",
            "name": "monster_dimension_is_energy_ceiling",
            "status": "not_claimed",
            "allowed_reading": "196883 is a representation-dimension/combinatorial ceiling analog.",
            "forbidden_promotion": "196883 is a universal physical energy or state-count ceiling.",
            "witness_function_present": False,
            "physical_units_present": False,
            "falsifier": "A same-contract state space exceeds the proposed ceiling, or no proved fingerprint-to-Monster map exists.",
        },
        {
            "id": "H3",
            "name": "pariah_happy_family_bounds_physics",
            "status": "not_claimed",
            "allowed_reading": "Pariah/Happy-Family closure is cited as a finite boundary-routing analog.",
            "forbidden_promotion": "Pariah closure inversion is a physical boundary law.",
            "witness_function_present": False,
            "physical_units_present": False,
            "falsifier": "An isomorphism-invariant encoding breaks the inversion, or no physical boundary witness is supplied.",
        },
    ]


def build_receipt() -> dict[str, Any]:
    arithmetic = arithmetic_rows()
    voa = voa_rows()
    hypotheses = hypothesis_rows()
    checks = [
        _check("47*59*71_equals_196883", arithmetic["supersingular_product"]["passes"], arithmetic["supersingular_product"]),
        _check("196884_equals_1_plus_196883", arithmetic["mckay_decomposition"]["passes"], arithmetic["mckay_decomposition"]),
        _check("voa_partition_2q0_6q5", voa["voa_partition"]["passes"], voa["voa_partition"]),
        _check("centroid_chain_finite_chart", voa["centroid_chain"]["passes"], voa["centroid_chain"]),
        _check(
            "energy_hypotheses_remain_quarantined",
            all(row["status"] == "not_claimed" and not row["witness_function_present"] for row in hypotheses),
            hypotheses,
        ),
        _check(
            "no_physical_energy_claim_promoted",
            all(not row["physical_units_present"] for row in hypotheses),
            hypotheses,
        ),
    ]
    passed = all(check["pass"] for check in checks)
    return {
        "paper": "CQE-paper-29",
        "title": "Monster/Universal Energy-Bound Hypotheses",
        "status": "pass_with_quarantined_hypotheses" if passed else "fail",
        "closed_scope": [
            "integer arithmetic: 196883 = 47*59*71",
            "integer decomposition: 196884 = 1 + 196883",
            "finite VOA partition: Z(q) = 2q^0 + 6q^5",
            "finite centroid chain: 2 fixed points and 6 period-4 states",
        ],
        "not_claimed": [
            "VOA weight as physical energy",
            "Monster dimension as a universal energy ceiling",
            "Pariah/Happy-Family closure as a physical boundary law",
            "a new Monstrous Moonshine theorem",
        ],
        "proof_rows": {
            "arithmetic": arithmetic,
            "voa": voa,
        },
        "hypothesis_rows": hypotheses,
        "open_obligations": [
            "Supply a units-bearing physical-energy transport theorem before any energy claim is promoted.",
            "Supply a proved fingerprint-to-Monster map before any universal ceiling claim is promoted.",
            "Supply an encoding-invariant Pariah/Happy-Family boundary theorem before any physical-boundary claim is promoted.",
            "Replace horizon citations with final bibliography entries and expert review.",
        ],
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    OUT.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"].startswith("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
