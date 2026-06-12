"""Paper 20 verifier: Layer-2 synthesis ledger receipts."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "production" / "packages" / "cqecmplx-forge" / "src"
sys.path.insert(0, str(SRC))

from lattice_forge.contributions_registry import Registry  # noqa: E402
from lattice_forge.ledger.build import build_seed_database  # noqa: E402
from lattice_forge.transport_obligations import verify_transport_obligations  # noqa: E402


def _registry_probe(path: Path) -> dict:
    registry = Registry(path)

    def validator(kind: str, key: object, value: object) -> tuple[bool, str]:
        if kind == "route_status" and isinstance(value, dict) and "classification" in value:
            return True, "classification field present"
        return False, "missing classification field"

    registry.register_validator("classification_required", validator)
    accepted = registry.propose(
        "route_status",
        {"paper": "CQE-paper-20", "row": "demo"},
        {"classification": "demonstrated"},
        "Paper 20 verifier probe",
        "classification_required",
    )
    rejected = registry.propose(
        "route_status",
        {"paper": "CQE-paper-20", "row": "bad"},
        {"status": "bare assertion"},
        "Paper 20 verifier negative probe",
        "classification_required",
    )
    stats = registry.stats()
    lookup = registry.lookup("route_status", {"paper": "CQE-paper-20", "row": "demo"})
    registry.close()
    return {"accepted": accepted, "rejected": rejected, "stats": stats, "lookup": lookup}


def main() -> dict:
    transport = verify_transport_obligations()
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        tmp_path = Path(tmp)
        ledger = build_seed_database(tmp_path / "layer2.sqlite", overwrite=True)
        ledger_verify = ledger.verify()
        summary = ledger.summary()
        yes_with_glue = ledger.can_close("A1", "Niemeier:A1^24")
        forbidden = ledger.can_close("G2", "Niemeier:Leech")
        unknown = ledger.can_close("not_seeded_source", "Niemeier:E8^3")
        ledger.close()
        registry = _registry_probe(tmp_path / "contrib.sqlite")

    checks = {
        "seed_ledger_verifies": ledger_verify.get("status") == "pass",
        "ledger_has_required_tables": all(
            summary.get(table, 0) > 0
            for table in [
                "object_registry",
                "exact_vectors",
                "admissibility_edges",
                "terminal_24d_forms",
                "discriminant_registry",
                "closure_obstruction_registry",
            ]
        ),
        "terminal_count_is_24": summary.get("terminal_24d_forms") == 24,
        "reachability_yes_with_template_glue": yes_with_glue.get("answer")
        == "yes_with_template_glue",
        "reachability_forbidden_is_no": forbidden.get("answer") == "no",
        "reachability_unknown_is_open": unknown.get("answer") == "unknown",
        "transport_obligations_pass_with_open_lifts": transport.get("status")
        == "pass_with_open_lifts"
        and transport.get("row_count") == 4
        and transport.get("demonstrated_count") == 2
        and transport.get("open_lift_count") == 2
        and transport.get("all_lifts_demonstrated") is False,
        "registry_accepts_only_validated_rows": registry["accepted"].get("status")
        == "accepted"
        and registry["rejected"].get("status") == "rejected"
        and registry["lookup"] is not None,
    }

    receipt = {
        "paper": "CQE Paper 20",
        "title": "Layer-2 Synthesis Ledger",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "closed_layers": [
            "seed ledger verifies",
            "ledger summary tables are populated",
            "24 terminal forms are registered",
            "can_close distinguishes yes_with_template_glue, no, and unknown",
            "transport obligations pass with two demonstrated and two open-lift rows",
            "contributions registry accepts validated rows and records rejected rows",
        ],
        "open_layers": [
            "source-paper claims are not re-proved by aggregation",
            "unknown reachability rows remain obligations",
            "forbidden rows remain recorded obstructions",
            "open transport lifts remain open until their source verifiers close them",
        ],
        "falsifiers": [
            "Ledger.verify fails",
            "unknown reachability is treated as solved",
            "forbidden reachability is discarded",
            "pass_with_open_lifts is promoted to pass",
            "a contribution enters without validator acceptance",
        ],
        "source_receipts": {
            "ledger_verify": ledger_verify,
            "summary": summary,
            "reachability": {
                "yes_with_template_glue": yes_with_glue,
                "forbidden_no": forbidden,
                "unknown_open": unknown,
            },
            "transport_obligations": transport,
            "registry_probe": registry,
        },
    }

    out_path = Path(__file__).with_name("layer2_synthesis_ledger_receipt.json")
    out_path.write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "checks": checks}, indent=2))
    return receipt


if __name__ == "__main__":
    result = main()
    raise SystemExit(0 if result["status"] == "pass" else 1)
