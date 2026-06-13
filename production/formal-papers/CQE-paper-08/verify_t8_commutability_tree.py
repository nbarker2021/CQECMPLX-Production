#!/usr/bin/env python3
"""Paper 08 verifier for T8, the F4-to-Niemeier commutability tree.

This verifier rebuilds a temporary lattice-forge seed ledger and queries
Forge.can_close("F4", target) for the eight canonical Niemeier terminals
recorded by the historical CMPLX-R30 proof report.

Scope boundary: this closes the seed-ledger path and template-glue receipt for
the eight canonical paths. It does not prove exact integer-vector glue-coset
representatives, rootless Leech landing, or Gamma72 polarization.
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_FORGE_SRC = _HERE.parents[1] / "packages" / "cqecmplx-forge" / "src"
if str(_FORGE_SRC) not in sys.path:
    sys.path.insert(0, str(_FORGE_SRC))

from lattice_forge.forge import Forge  # noqa: E402
from lattice_forge.ledger import build_seed_database  # noqa: E402
from lattice_forge.overlay import OverlayStore  # noqa: E402
from lattice_forge.seed import SeedStore  # noqa: E402


EXPECTED_PATHS = [
    ("Niemeier:E8^3", ["F4", "G2xF4", "E8", "Niemeier:E8^3"]),
    ("Niemeier:D16_E8", ["F4", "G2xF4", "E8", "Niemeier:D16_E8"]),
    ("Niemeier:A17_E7", ["F4", "E6", "E7", "Niemeier:A17_E7"]),
    ("Niemeier:D10_E7^2", ["F4", "E6", "E7", "Niemeier:D10_E7^2"]),
    ("Niemeier:A11_D7_E6", ["F4", "E6", "Niemeier:A11_D7_E6"]),
    ("Niemeier:E6^4", ["F4", "E6", "Niemeier:E6^4"]),
    ("Niemeier:A5^4_D4", ["F4", "D4", "Niemeier:A5^4_D4"]),
    ("Niemeier:D4^6", ["F4", "D4", "Niemeier:D4^6"]),
]


def _query_paths() -> tuple[list[dict], dict]:
    work = Path(tempfile.mkdtemp(prefix="paper08-t8-"))
    try:
        db = work / "seed.db"
        ledger = build_seed_database(db)
        ledger.close()
        forge = Forge(
            seed=SeedStore(db),
            overlay=OverlayStore.open(work),
            witness_db=work / "witness.sqlite",
        )
        paths: list[dict] = []
        for target, expected_path in EXPECTED_PATHS:
            result = forge.can_close("F4", target).get("result", {}).get("can_close", {})
            paths.append(
                {
                    "target": target,
                    "answer": result.get("answer"),
                    "path": result.get("path"),
                    "expected_path": expected_path,
                    "path_matches_expected": result.get("path") == expected_path,
                    "edge_count": len(result.get("path_edges", [])),
                    "edge_ids": [edge.get("edge_id") for edge in result.get("path_edges", [])],
                    "glue_statuses": [
                        glue.get("status") for glue in result.get("glue_templates", [])
                    ],
                    "discriminant_glue_status": (
                        result.get("discriminant_profile") or {}
                    ).get("glue_status"),
                }
            )
        build_info = {
            "temporary_seed_db_built": db.exists(),
            "temporary_seed_db_bytes": db.stat().st_size if db.exists() else 0,
        }
        return paths, build_info
    finally:
        shutil.rmtree(work, ignore_errors=True)


def main() -> int:
    paths, build_info = _query_paths()
    expected_targets = [target for target, _ in EXPECTED_PATHS]
    found_targets = [row["target"] for row in paths if str(row.get("answer", "")).startswith("yes")]
    unique_terminals = sorted({row["target"] for row in paths})
    trunk_nodes = sorted({node for row in paths for node in row["path"][1:-1]})
    template_glue_only = all(
        row["answer"] == "yes_with_template_glue" for row in paths
    )
    all_paths_match = all(row["path_matches_expected"] for row in paths)
    all_targets_found = found_targets == expected_targets
    all_distinct_terminals = len(unique_terminals) == len(EXPECTED_PATHS)
    every_path_starts_at_f4 = all(row["path"][0] == "F4" for row in paths)
    every_path_ends_at_target = all(row["path"][-1] == row["target"] for row in paths)

    checks = {
        "temporary_seed_db_built": bool(build_info["temporary_seed_db_built"]),
        "paths_count_is_8": len(paths) == 8,
        "all_targets_found_in_order": all_targets_found,
        "all_paths_match_historical_report": all_paths_match,
        "all_answers_are_yes_with_template_glue": template_glue_only,
        "all_terminals_are_distinct": all_distinct_terminals,
        "every_path_starts_at_F4": every_path_starts_at_f4,
        "every_path_ends_at_requested_target": every_path_ends_at_target,
        "trunk_nodes_are_expected": trunk_nodes == ["D4", "E6", "E7", "E8", "G2xF4"],
    }
    status = "pass" if all(checks.values()) else "fail"
    receipt = {
        "paper": "CQE-paper-08",
        "theorem": "T8 F4 to Niemeier commutability tree",
        "status": status,
        "source": "rebuilt temporary lattice_forge seed ledger",
        "build_info": build_info,
        "checks": checks,
        "paths": paths,
        "closed_scope": [
            "the eight canonical F4-to-Niemeier terminal paths are present",
            "each queried path returns yes_with_template_glue",
            "each path matches the historical CMPLX-R30 T8 path table",
        ],
        "not_claimed": [
            "exact integer-vector glue-coset representatives",
            "rootless Leech landing",
            "Gamma72 polarization or landing",
            "uniqueness of all possible closure templates",
        ],
    }
    out = _HERE / "t8_commutability_tree_receipt.json"
    out.write_text(json.dumps(receipt, indent=2, default=str) + "\n", encoding="utf-8")
    print(json.dumps({"status": status, "passed": sum(checks.values()), "total": len(checks), "receipt": str(out)}, indent=2))
    return 0 if status == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
