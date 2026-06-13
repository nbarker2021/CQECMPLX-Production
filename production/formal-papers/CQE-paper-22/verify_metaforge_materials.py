"""Formal receipt generator for Paper 22.

Paper 22 closes MetaForge only as a reproducible materials-candidate pipeline.
It verifies material loading, Pareto partner selection, deterministic fold
evaluation, seam proposal, and production-estimate accounting. It does not
claim finite-element validation, fabrication, measured auxetic behavior, or
superior mechanical performance.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
PACKAGE_ROOT = (
    ROOT
    / "production"
    / "lib-forge"
    / "CQECMPLX-MetaMaterial-Designer"
    / "meta_material_system"
)
sys.path.insert(0, str(PACKAGE_ROOT))

from fold_evaluation import run_10_fold_evaluation  # noqa: E402
from material_db import get_material, list_materials  # noqa: E402
from pareto_partnering import find_pareto_partners  # noqa: E402
from production_energy import generate_production_plan  # noqa: E402
from seam_detection import detect_seam_candidates  # noqa: E402


OUT = Path(__file__).resolve().parent / "metaforge_materials_receipt.json"


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _summarize_pair(base_name: str, partner_name: str | None = None) -> dict[str, Any]:
    base = get_material(base_name)
    if base is None:
        raise ValueError(f"unknown base material: {base_name}")

    materials = [get_material(name) for name in list_materials()]
    partners = find_pareto_partners(base, materials)
    partner = get_material(partner_name) if partner_name else partners[0].material_b
    if partner is None:
        raise ValueError(f"unknown partner material: {partner_name}")

    folds = run_10_fold_evaluation(base, partner)
    seams = detect_seam_candidates(base, partner, folds)
    plan = generate_production_plan(base, partner, folds, seams, 1.0)

    pair_row = next(
        (candidate for candidate in partners if candidate.material_b.name == partner.name),
        None,
    )

    return {
        "base": base.name,
        "partner": partner.name,
        "partner_rank": partners.index(pair_row) + 1 if pair_row else None,
        "pareto_score": pair_row.pareto_score if pair_row else None,
        "pareto_components": {
            "lattice_match": pair_row.lattice_match if pair_row else None,
            "property_synergy": pair_row.property_synergy if pair_row else None,
            "gluon_coherence": pair_row.gluon_coherence if pair_row else None,
            "oloid_compatibility": pair_row.oloid_compatibility if pair_row else None,
            "interface_energy": pair_row.interface_energy if pair_row else None,
            "strain_tolerance": pair_row.strain_tolerance if pair_row else None,
        },
        "fold": {
            "fold_count": len(folds.folds),
            "final_tensile": folds.final_tensile,
            "final_composite": folds.final_composite,
            "final_gluon_mass": folds.final_gluon_mass,
            "total_formation_energy": folds.total_formation_energy,
            "error_wall_summary": {
                wall_type.value: count
                for wall_type, count in folds.error_wall_summary.items()
            },
        },
        "seams": [
            {
                "material": seam.material.name,
                "role": seam.role,
                "placement": seam.placement,
                "effectiveness": seam.effectiveness,
                "required_thickness_nm": seam.required_thickness,
            }
            for seam in seams
        ],
        "production_plan": {
            "total_energy_joules_per_cm2": plan.total_energy_joules_per_cm2,
            "total_time_hours": plan.total_time_hours,
            "max_temperature_K": plan.max_temperature_K,
            "max_pressure_atm": plan.max_pressure_atm,
            "estimated_cost_usd_per_cm2": plan.estimated_cost_usd_per_cm2,
            "scalability_score": plan.scalability_score,
            "step_count": len(plan.steps),
            "notes": plan.notes,
        },
    }


def build_receipt() -> dict[str, Any]:
    material_names = list_materials()
    graphene_hbn = _summarize_pair("graphene")
    test_pairs = [
        _summarize_pair("graphene", "tbg"),
        _summarize_pair("mos2", "hbn"),
        _summarize_pair("bp", "mxene"),
        _summarize_pair("sto", "mowse2"),
    ]

    checks = [
        _check(
            "material database has a finite replayable inventory",
            len(material_names) >= 20
            and get_material("graphene") is not None
            and get_material("hbn") is not None,
            {"material_count": len(material_names), "sample": material_names[:5]},
        ),
        _check(
            "graphene selects hBN as top Pareto partner",
            graphene_hbn["partner"] == "Hexagonal Boron Nitride"
            and graphene_hbn["partner_rank"] == 1
            and graphene_hbn["pareto_score"] >= 0.88,
            {
                "partner": graphene_hbn["partner"],
                "rank": graphene_hbn["partner_rank"],
                "pareto_score": graphene_hbn["pareto_score"],
                "components": graphene_hbn["pareto_components"],
            },
        ),
        _check(
            "fold engine emits a deterministic ten-fold candidate receipt",
            graphene_hbn["fold"]["fold_count"] == 10
            and graphene_hbn["fold"]["final_tensile"] > 0
            and graphene_hbn["fold"]["final_composite"] > 0
            and 0 < graphene_hbn["fold"]["final_gluon_mass"] <= 3.0,
            graphene_hbn["fold"],
        ),
        _check(
            "seam detector emits explicit mitigation candidates",
            len(graphene_hbn["seams"]) >= 1
            and {seam["role"] for seam in graphene_hbn["seams"]}
            >= {"healing", "electrical", "gradient"},
            graphene_hbn["seams"],
        ),
        _check(
            "production estimator emits positive bounded accounting",
            graphene_hbn["production_plan"]["total_energy_joules_per_cm2"] > 0
            and graphene_hbn["production_plan"]["estimated_cost_usd_per_cm2"] > 0
            and graphene_hbn["production_plan"]["step_count"] >= 5
            and 0 < graphene_hbn["production_plan"]["scalability_score"] <= 1,
            graphene_hbn["production_plan"],
        ),
        _check(
            "additional material pairs run through the same pipeline",
            all(row["fold"]["fold_count"] == 10 for row in test_pairs)
            and all(row["production_plan"]["total_energy_joules_per_cm2"] > 0 for row in test_pairs)
            and all(row["production_plan"]["estimated_cost_usd_per_cm2"] > 0 for row in test_pairs),
            [
                {
                    "base": row["base"],
                    "partner": row["partner"],
                    "fold_count": row["fold"]["fold_count"],
                    "seam_count": len(row["seams"]),
                    "energy": row["production_plan"]["total_energy_joules_per_cm2"],
                    "cost": row["production_plan"]["estimated_cost_usd_per_cm2"],
                }
                for row in test_pairs
            ],
        ),
    ]

    open_obligations = [
        {
            "obligation": "finite-element validation",
            "status": "open",
            "reason": "the receipt estimates properties but does not solve continuum mechanics",
        },
        {
            "obligation": "fabrication and load testing",
            "status": "open",
            "reason": "no printed or deposited candidate has a measured stress-strain receipt here",
        },
        {
            "obligation": "manufacturability constraints",
            "status": "open",
            "reason": "minimum feature size, overhang, tooling, and defect tolerances are not closed by the candidate ledger",
        },
        {
            "obligation": "relative-density and Poisson-ratio measurement",
            "status": "open",
            "reason": "the package emits a candidate stack and estimates, not a measured auxetic unit cell",
        },
    ]

    receipt = {
        "paper": "CQE-paper-22",
        "title": "MetaForge Applied Materials",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "MetaForge supplies a replayable candidate-generation ledger for "
            "material pair selection, ten-fold evaluation, seam proposal, and "
            "production-estimate accounting."
        ),
        "package_root": str(PACKAGE_ROOT),
        "graphene_hbn_candidate": graphene_hbn,
        "additional_pairs": test_pairs,
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
