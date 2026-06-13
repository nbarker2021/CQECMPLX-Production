"""Formal receipt generator for Paper 23.

Paper 23 closes FoldForge only as a replayable protein-fold descriptor:
residue-chain local windows, a contact-map receipt, bounded winding evidence,
bifurcation accounting, and explicit validation obligations. It does not claim
native-structure prediction, AlphaFold parity, measured free energy, fold-rate
prediction, or PDB validation.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.rule30 import (  # noqa: E402
    rule30_oloid_bifurcation_detector,
    rule30_winding_number_proof,
    verify_rule30_oloid_bifurcation_detector,
    verify_rule30_oloid_winding_from_n,
    verify_rule30_winding_number_proof,
)


OUT = Path(__file__).resolve().parent / "foldforge_descriptor_receipt.json"
HYDROPHOBIC = set("AILMFWVY")


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def residue_chart(sequence: str) -> list[dict[str, Any]]:
    encoded = [1 if aa in HYDROPHOBIC else 0 for aa in sequence]
    chart: list[dict[str, Any]] = []
    for i, center in enumerate(encoded):
        left = encoded[i - 1] if i > 0 else None
        right = encoded[i + 1] if i + 1 < len(encoded) else None
        chart.append(
            {
                "index": i,
                "residue": sequence[i],
                "L": left,
                "C": center,
                "R": right,
                "window_complete": left is not None and right is not None,
            }
        )
    return chart


def contact_map(sequence: str) -> dict[str, Any]:
    encoded = [1 if aa in HYDROPHOBIC else 0 for aa in sequence]
    contacts: list[dict[str, int]] = []
    n = len(sequence)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 3, n):
            if encoded[i] and encoded[j]:
                matrix[i][j] = 1
                matrix[j][i] = 1
                contacts.append({"i": i, "j": j})
    total_pairs = n * (n - 1) // 2
    contact_order = (
        sum(abs(c["j"] - c["i"]) for c in contacts) / (len(contacts) * n)
        if contacts
        else 0.0
    )
    return {
        "sequence_length": n,
        "contact_count": len(contacts),
        "total_pairs": total_pairs,
        "contact_density": len(contacts) / total_pairs,
        "contact_order": contact_order,
        "contacts": contacts,
        "symmetric": all(matrix[i][j] == matrix[j][i] for i in range(n) for j in range(n)),
        "diagonal_zero": all(matrix[i][i] == 0 for i in range(n)),
    }


def lcr_bifurcations(chart: list[dict[str, Any]]) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    previous_side: int | None = None
    for row in chart:
        if not row["window_complete"]:
            continue
        side = row["R"] - row["L"]
        if previous_side is not None and side != previous_side:
            events.append(
                {
                    "index": row["index"],
                    "residue": row["residue"],
                    "previous_side": previous_side,
                    "side": side,
                    "event": "side_change",
                }
            )
        previous_side = side
    return events


def build_receipt() -> dict[str, Any]:
    sequence = "MKTFFVLLLCTFTVLA"
    chart = residue_chart(sequence)
    contacts = contact_map(sequence)
    local_events = lcr_bifurcations(chart)

    winding_model = rule30_winding_number_proof(max_depth=512, max_order=4)
    winding_verify = verify_rule30_winding_number_proof(winding_model)
    oloid_verify = verify_rule30_oloid_winding_from_n(max_depth=128)
    bif_model = rule30_oloid_bifurcation_detector(
        max_depth=512,
        sheet_size=16,
        page_size=512,
        block_size=8,
    )
    bif_verify = verify_rule30_oloid_bifurcation_detector(bif_model)

    checks = [
        _check(
            "residue chain maps to complete local windows",
            len(chart) == len(sequence)
            and sum(1 for row in chart if row["window_complete"]) == len(sequence) - 2,
            {
                "sequence": sequence,
                "length": len(sequence),
                "complete_windows": sum(1 for row in chart if row["window_complete"]),
                "hydrophobic_count": sum(row["C"] for row in chart),
            },
        ),
        _check(
            "contact map is replayable and symmetric",
            contacts["contact_count"] > 0
            and contacts["symmetric"]
            and contacts["diagonal_zero"]
            and 0 < contacts["contact_density"] < 1,
            contacts,
        ),
        _check(
            "local LCR side changes emit candidate bifurcation marks",
            len(local_events) > 0,
            local_events,
        ),
        _check(
            "winding number proof verifies as bounded trace witness",
            winding_model["status"] == "pass_with_open_gaps"
            and winding_verify["schema_status"] == "pass"
            and winding_model["complexity_proof"]["claim_status"] == "BOUNDED_TRACE_WITNESS"
            and winding_model["operator_stability"]["stable_across_pages"],
            {
                "model_status": winding_model["status"],
                "verify": winding_verify,
                "operator_stability": winding_model["operator_stability"],
                "complexity_proof": winding_model["complexity_proof"],
                "open_gaps": winding_model["open_gaps"],
            },
        ),
        _check(
            "direct oloid predictor defects remain explicit",
            oloid_verify["status"] == "pass_with_open_gaps"
            and oloid_verify["defect_count"] > 0
            and not oloid_verify["claim"]["bounded_exec_at_window"],
            {
                "status": oloid_verify["status"],
                "accuracy": oloid_verify["accuracy"],
                "defect_count": oloid_verify["defect_count"],
                "first_defects": oloid_verify["first_defects"][:4],
                "interpretation": oloid_verify["claim"]["interpretation"],
            },
        ),
        _check(
            "substrate bifurcation detector schema passes with gap carried",
            bif_model["status"] == "pass_with_open_gaps"
            and bif_verify["schema_status"] == "pass"
            and bif_model["complete_sheet_count"] >= 1,
            {
                "model_status": bif_model["status"],
                "verify": bif_verify,
                "defect_count": bif_model["defect_count"],
                "complete_sheet_count": bif_model["complete_sheet_count"],
                "tail_defect_count": bif_model["tail_defect_count"],
                "detected_clean_climb_count": bif_model["detected_clean_climb_count"],
                "open_gaps": bif_model["open_gaps"],
            },
        ),
    ]

    open_obligations = [
        {
            "obligation": "PDB validation",
            "status": "open",
            "reason": "the descriptor has not been tested against deposited structures",
        },
        {
            "obligation": "native structure prediction",
            "status": "not_claimed",
            "reason": "the receipt emits descriptors, not coordinates or free-energy minima",
        },
        {
            "obligation": "depth-only winding extractor",
            "status": "open",
            "reason": "the winding state is still read from a bounded trace witness",
        },
        {
            "obligation": "biological encoding",
            "status": "open",
            "reason": "the demonstration uses a simple hydrophobic/polar encoding",
        },
        {
            "obligation": "fold-rate or thermodynamic validation",
            "status": "open",
            "reason": "no kinetic or experimental energy receipt is included",
        },
    ]

    receipt = {
        "paper": "CQE-paper-23",
        "title": "FoldForge Protein Folding",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "FoldForge supplies a replayable residue-window, contact-map, "
            "winding-trace, and bifurcation-descriptor receipt for protein fold "
            "candidates without claiming native-structure prediction."
        ),
        "candidate_descriptor": {
            "sequence": sequence,
            "chart_sample": chart[:6],
            "contact_map": contacts,
            "local_bifurcations": local_events,
        },
        "substrate": {
            "winding_proof": {
                "status": winding_model["status"],
                "verification": winding_verify,
                "operator_stability": winding_model["operator_stability"],
                "winding_trace_sample": winding_model["winding_trace_sample"],
                "open_gaps": winding_model["open_gaps"],
            },
            "oloid_predictor_check": oloid_verify,
            "bifurcation_detector": {
                "status": bif_model["status"],
                "verification": bif_verify,
                "defect_count": bif_model["defect_count"],
                "complete_sheet_count": bif_model["complete_sheet_count"],
                "tail_defect_count": bif_model["tail_defect_count"],
                "detected_clean_climb_count": bif_model["detected_clean_climb_count"],
                "open_gaps": bif_model["open_gaps"],
            },
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
