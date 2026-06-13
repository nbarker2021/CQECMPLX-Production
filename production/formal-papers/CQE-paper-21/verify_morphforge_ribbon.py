"""Formal receipt generator for Paper 21.

Paper 21 closes the MorphForge / PolyForge / MorphoniX core only as a
lossless ribbon-reading and morphon-accounting substrate. Cross-medium,
Mandelbrot, Leech, TF1, and applied-domain claims remain carried as explicit
open obligations unless a later paper supplies a domain verifier.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from lattice_forge.chart_codec import verify_chart_codec
from lattice_forge.ledger.build import build_seed_database
from lattice_forge.morphonics import morphonics_model_v0_2, verify_morphonics_model
from lattice_forge.terminal_tree import terminal_tree_summary


ROOT = Path(__file__).resolve().parent
RECEIPT = ROOT / "morphforge_ribbon_receipt.json"


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def build_receipt() -> dict[str, Any]:
    chart = verify_chart_codec(max_depth=4096)
    model = morphonics_model_v0_2()
    morphonics = verify_morphonics_model(model)

    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        ledger = build_seed_database(Path(tmp) / "morphforge.sqlite", overwrite=True)
        try:
            tree = terminal_tree_summary(ledger.terminal_tree("Niemeier:E8^3"))
        finally:
            ledger.close()

    element_counts = chart["element_counts"]
    required_failure_labels = {
        "PENDING_IMPORT",
        "MISSING_MORPHISM",
        "PENDING_MEASUREMENT",
    }
    failure_labels = {failure["label"] for failure in model["failures"]}

    checks = [
        _check(
            "chart codec round trip is lossless",
            chart["status"] == "pass" and chart["round_trip_mismatches"] == 0,
            {
                "status": chart["status"],
                "round_trip_mismatches": chart["round_trip_mismatches"],
                "first_mismatch": chart["first_mismatch"],
            },
        ),
        _check(
            "shell-2 ribbon produces an S3 word",
            chart["shell2_length"] > 0
            and chart["word_length"] == chart["shell2_length"] - 1
            and chart["non_identity_steps"] > 0
            and chart["identity_self_loops"] > 0,
            {
                "trajectory_length": chart["trajectory_length"],
                "shell2_length": chart["shell2_length"],
                "word_length": chart["word_length"],
                "identity_self_loops": chart["identity_self_loops"],
                "non_identity_steps": chart["non_identity_steps"],
            },
        ),
        _check(
            "observed folds are transposition-class steps",
            element_counts["(1 2)"] > 0
            and element_counts["(1 3)"] > 0
            and element_counts["(2 3)"] > 0
            and element_counts["(1 2 3)"] == 0
            and element_counts["(1 3 2)"] == 0,
            element_counts,
        ),
        _check(
            "morphonics ledger schema closes with carried gaps",
            morphonics["status"] == "pass_with_open_gaps"
            and morphonics["schema_status"] == "pass"
            and morphonics["open_gap_count"] == 3,
            {
                "status": morphonics["status"],
                "schema_status": morphonics["schema_status"],
                "open_gap_count": morphonics["open_gap_count"],
                "errors": morphonics["errors"],
                "warnings": morphonics["warnings"],
            },
        ),
        _check(
            "morphon closure tests all pass",
            all(test["status"] == "pass" for test in morphonics["closure_tests"]),
            morphonics["closure_tests"],
        ),
        _check(
            "morphonics table counts match the declared model",
            morphonics["counts"]
            == {
                "morphons": 5,
                "transforms": 5,
                "projections": 5,
                "accounting": 3,
                "bridges": 3,
                "claims": 11,
                "failures": 3,
                "closure_tests": 5,
            },
            morphonics["counts"],
        ),
        _check(
            "open failure labels are explicit and non-silent",
            required_failure_labels <= failure_labels,
            sorted(failure_labels),
        ),
        _check(
            "terminal landing template is 24-dimensional E8^3",
            tree["terminal_id"] == "Niemeier:E8^3"
            and tree["ambient_dimension"] == 24
            and tree["root_rank"] == 24
            and tree["residue_status"] == "residue_closes_by_required_index",
            tree,
        ),
    ]

    open_obligations = [
        {
            "obligation": "cross-medium equivalence / unibeam",
            "status": "open_until_measurement",
            "reason": "the morphonics model accounts the bridge but does not close a medium-invariant proof",
        },
        {
            "obligation": "Mandelbrot or fractal-boundary chart",
            "status": "open_until_semiconjugacy",
            "reason": "no formal semiconjugacy witness is included in the closed receipt",
        },
        {
            "obligation": "Leech construction import",
            "status": "open_until_Golay_or_Construction_A_import",
            "reason": "terminal E8^3 template is not a Leech lattice construction",
        },
        {
            "obligation": "expanded involution witnesses",
            "status": "open_until_action_orbit_quotient_witnesses",
            "reason": "the morphonics bridge carries the missing-morphism label",
        },
        {
            "obligation": "TF1, biological, material, CAD, or product claims",
            "status": "open_until_domain_verifier",
            "reason": "Paper 21 supplies the reading/accounting substrate, not a domain closure",
        },
    ]

    receipt = {
        "paper": "CQE-paper-21",
        "title": "MorphForge / PolyForge / MorphoniX",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "A grid-swept ribbon can be encoded as a lossless S3 word, accounted "
            "as morphon records, and landed in the 24-dimensional E8^3 terminal "
            "template without silently closing cross-domain bridges."
        ),
        "chart_codec": chart,
        "morphonics": morphonics,
        "terminal_tree": tree,
        "checks": checks,
        "open_obligations": open_obligations,
    }
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["status"] == "pass_with_open_obligations" else 1


if __name__ == "__main__":
    raise SystemExit(main())
