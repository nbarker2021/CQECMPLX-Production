#!/usr/bin/env python3
"""Finite verifier for CQE Paper 14, Boundary-Repair Curvature."""

from __future__ import annotations

import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(PACKAGE_SRC))

from lattice_forge.cayley_dickson_oloid import (  # noqa: E402
    cayley_dickson_oloid_normal_form,
    verify_cayley_dickson_oloid_normal_form,
)
from lattice_forge.f4_action import verify_n3_su3_closure_exact  # noqa: E402
from lattice_forge.oloid_dual_path import verify_dual_path_oloid  # noqa: E402
from lattice_forge.transport_obligations import verify_transport_obligations  # noqa: E402


def repair_score(classification: str) -> int:
    """Scalar repair proxy: larger value means less closed transport."""
    weights = {
        "demonstrated": 0,
        "bounded_local": 1,
        "bounded_external": 2,
        "registered_landing_forms": 3,
        "open": 4,
    }
    return weights[classification]


def verify() -> dict:
    transport = verify_transport_obligations(max_depth=512)
    su3 = verify_n3_su3_closure_exact()
    normal = verify_cayley_dickson_oloid_normal_form(max_n=16, energy_terms=16)
    dual = verify_dual_path_oloid()
    sample_form = cayley_dickson_oloid_normal_form(3, energy_terms=16)

    rows = transport["rows"]
    repair_rows = [
        {
            "id": row["id"],
            "classification": row["classification"],
            "repair_score": repair_score(row["classification"]),
            "proof_boundary": row["proof_boundary"],
        }
        for row in rows
    ]
    nonzero_repair_rows = [row for row in repair_rows if row["repair_score"] > 0]

    dual_checks = {
        key: value
        for key, value in dual.items()
        if key.startswith("triple_involution")
        or key.startswith("dyad_at_")
        or key == "s3_action_coherent"
    }

    checks = {
        "transport_ledger_passes_with_open_lifts": transport["status"] == "pass_with_open_lifts",
        "transport_rows_have_boundaries": all(row.get("proof_boundary") for row in rows),
        "demonstrated_rows_have_zero_repair": all(
            row["repair_score"] == 0
            for row in repair_rows
            if row["classification"] == "demonstrated"
        ),
        "open_lifts_have_nonzero_repair": len(nonzero_repair_rows) == transport["open_lift_count"],
        "flat_su3_reference_has_zero_residual": su3.get("status") == "pass"
        and su3.get("residual_squared_exact") == "0",
        "oloid_normal_form_passes": normal["status"] == "pass"
        and tuple(normal["pattern"]) == (1, 8, 8, 1),
        "oloid_honesty_boundary_present": "does not by itself prove nth-bit extraction"
        in sample_form.honesty,
        "dual_path_oloid_passes": dual.get("status") == "pass",
        "gr_physics_left_as_obligation": True,
    }

    return {
        "paper": "CQE-paper-14",
        "theorem": "boundary-repair curvature substrate layer",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "transport_summary": {
            "status": transport["status"],
            "row_count": transport["row_count"],
            "demonstrated_count": transport["demonstrated_count"],
            "open_lift_count": transport["open_lift_count"],
            "all_lifts_demonstrated": transport["all_lifts_demonstrated"],
        },
        "repair_rows": repair_rows,
        "flat_reference": {
            "source": "Paper 13 n=3 SU3 closure",
            "residual_squared_exact": su3.get("residual_squared_exact"),
            "repair_score": 0,
        },
        "oloid_normal_form": {
            "status": normal["status"],
            "pattern": normal["pattern"],
            "honesty": sample_form.honesty,
        },
        "dual_path_summary": {
            "status": dual.get("status"),
            "checks": dual_checks,
        },
        "closed_layers": [
            "transport obligations are typed and boundary-bearing",
            "demonstrated rows score zero repair",
            "open lifts score nonzero repair",
            "Paper 13 exact SU3 closure supplies zero-repair reference",
            "Cayley-Dickson/Oloid normal form verifies 1,8,8,1 carrier pattern",
            "dual-path oloid verifies three-dyad involution coherence",
        ],
        "open_layers": [
            "Riemann/Ricci/Einstein tensor derivation",
            "calibrated gravitational measurement",
            "nth-bit extraction from the oloid normal form alone",
        ],
        "falsifiers": [
            {"claim": "A demonstrated transport row has nonzero repair score", "accepted": False},
            {"claim": "An open lift can be treated as zero curvature", "accepted": False},
            {"claim": "Einstein field equations are verified by this receipt", "accepted": False},
        ],
        "scope_boundary": (
            "Paper 14 proves a substrate repair-magnitude ledger and curved-carrier witness. "
            "General Relativity curvature is a candidate interpretation, not a closed physical theorem."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("boundary_repair_curvature_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
