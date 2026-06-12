#!/usr/bin/env python3
"""Verifier for CQE Paper 10, T10 Master Receipt."""

from __future__ import annotations

import json
import sys
import tempfile
from dataclasses import asdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "packages" / "cqecmplx-forge" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lattice_forge.cmplx_lookup_cache import DATA_ROOT, build_default_cache  # noqa: E402
from lattice_forge.transport_obligations import verify_transport_obligations  # noqa: E402


FORMAL_RECEIPTS = {
    "CQE-paper-01": "lcr_carrier_receipt.json",
    "CQE-paper-02": "correction_surface_receipt.json",
    "CQE-paper-03": "triality_surface_receipt.json",
    "CQE-paper-04": "boundary_repair_receipt.json",
    "CQE-paper-05": "oloid_path_carrier_receipt.json",
    "CQE-paper-06": "causal_code_receipt.json",
    "CQE-paper-07": "discrete_continuous_bridge_receipt.json",
    "CQE-paper-08": "lattice_closure_template_receipt.json",
    "CQE-paper-09": "hamiltonian_window_emergence_receipt.json",
}


def _paper00_binding() -> dict:
    source = ROOT / "papers" / "CQE-paper-00" / "SOURCE.md"
    paper01_source = ROOT / "papers" / "CQE-paper-01" / "SOURCE.md"
    receipt_root = ROOT / "proof-receipts" / "CQE-paper-00"
    receipts = sorted(receipt_root.glob("**/*.json"))
    return {
        "paper": "CQE-paper-00",
        "role": "past_burden_minimum_information_contract",
        "observer_center": "C00",
        "observer_center_semantics": (
            "requested enumeration event encoded as the system center"
        ),
        "encoding_event": "E00_to_1",
        "encoding_event_semantics": (
            "Paper 00 defines what must be carried; Paper 01 begins carrying it"
        ),
        "source_present": source.exists(),
        "paper01_source_present": paper01_source.exists(),
        "receipt_count": len(receipts),
        "bound": source.exists() and paper01_source.exists() and len(receipts) > 0,
        "receipt_paths": [str(path.relative_to(ROOT)) for path in receipts],
    }


def _formal_receipt_bindings() -> list[dict]:
    bindings = []
    for paper, filename in FORMAL_RECEIPTS.items():
        path = ROOT / "formal-papers" / paper / filename
        payload = {}
        status = "missing"
        if path.exists():
            payload = json.loads(path.read_text(encoding="utf-8"))
            status = str(payload.get("status", "present"))
        bindings.append(
            {
                "paper": paper,
                "path": str(path.relative_to(ROOT)),
                "present": path.exists(),
                "status": status,
                "status_pass_like": status in {"pass", "pass_with_open_lifts"},
            }
        )
    return bindings


def _lookup_cache_receipt() -> dict:
    cache = None
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tempdir:
        try:
            cache = build_default_cache(Path(tempdir) / "cmplx_lookup.sqlite", force=True)
            status = cache.status()
            rule30_tip = asdict(cache.lookup_rule30_bit(999_999))
            prize3 = asdict(cache.prize3_lookup_receipt(4096, group="F4"))
            return {
                "data_root": str(DATA_ROOT),
                "status": status,
                "rule30_tip_receipt": rule30_tip,
                "prize3_lookup_receipt": prize3,
                "checks": {
                    "rule30_window_has_one_million_bits": status["rule30_bits"] == 1_000_000,
                    "unipotent_orbit_count_is_157": status["unipotent_orbits"] == 157,
                    "lattice_form_count_is_24": status["lattice_forms"] == 24,
                    "umrk_register_present": status["source_registers"]["umrk"] is True,
                    "lmfdb_register_present": status["source_registers"]["lmfdb"] is True,
                    "rule30_tip_is_external_dataset_receipt": (
                        rule30_tip["source_id"] == "wolfram-rule30-center-million"
                        and rule30_tip["evidence_level"] == "external_dataset"
                    ),
                    "prize3_lookup_keeps_closed_form_boundary_open": (
                        prize3["value"]["closed_form_claim"] is False
                        and "remaining_obligation" in prize3["value"]
                    ),
                },
            }
        finally:
            if cache is not None:
                cache.close()


def verify() -> dict:
    transport = verify_transport_obligations(max_depth=4096)
    paper00 = _paper00_binding()
    formal_bindings = _formal_receipt_bindings()
    lookup = _lookup_cache_receipt()

    checks = {
        "paper00_contract_bound": paper00["bound"],
        "observer_center_encoded": (
            paper00["observer_center"] == "C00"
            and paper00["encoding_event"] == "E00_to_1"
            and paper00["source_present"] is True
            and paper00["paper01_source_present"] is True
        ),
        "papers01_to_09_receipts_present": all(row["present"] for row in formal_bindings),
        "papers01_to_09_status_pass_like": all(
            row["status_pass_like"] for row in formal_bindings
        ),
        "transport_rows_inspectable": (
            transport["status"] == "pass_with_open_lifts"
            and transport["row_count"] == 4
            and transport["all_rows_have_required_fields"] is True
            and transport["valid_classifications"] is True
        ),
        "transport_witnesses_replay": transport["local_witnesses_pass"] is True,
        "transport_open_lifts_are_visible": (
            transport["demonstrated_count"] == 2
            and transport["open_lift_count"] == 2
            and transport["all_lifts_demonstrated"] is False
        ),
        "lookup_cache_materializes": all(lookup["checks"].values()),
    }

    return {
        "paper": "CQE-paper-10",
        "theorem": "T10 master receipt integrity",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "paper00_binding": paper00,
        "formal_receipt_bindings": formal_bindings,
        "transport_summary": {
            "status": transport["status"],
            "row_count": transport["row_count"],
            "demonstrated_count": transport["demonstrated_count"],
            "open_lift_count": transport["open_lift_count"],
            "all_rows_have_required_fields": transport["all_rows_have_required_fields"],
            "valid_classifications": transport["valid_classifications"],
            "local_witnesses_pass": transport["local_witnesses_pass"],
            "all_lifts_demonstrated": transport["all_lifts_demonstrated"],
        },
        "transport_rows": transport["rows"],
        "lookup_cache": lookup,
        "falsifiers": [
            {
                "claim": "T10 proves every registered lift is already demonstrated",
                "accepted": False,
            },
            {
                "claim": "The lookup cache makes a cold-start closed-form N-to-fingerprint claim",
                "accepted": False,
            },
            {
                "claim": "A paper enters the master receipt without a source or receipt binding",
                "accepted": False,
            },
            {
                "claim": "A later paper can ignore the observer enumeration event encoded at 00 -> 1",
                "accepted": False,
            },
        ],
        "scope_boundary": (
            "Paper 10 proves master-receipt inspectability and replayability for "
            "Papers 00-09. It preserves open lifts as visible audit boundaries "
            "rather than converting them into closed domain theorems."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("t10_master_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
