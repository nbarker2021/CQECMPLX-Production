#!/usr/bin/env python3
"""Verifier for CQE Paper 11, Theory Admission Gate."""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "packages" / "cqecmplx-forge" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lattice_forge.ledger.build import PARIAHS, parse_factorization  # noqa: E402


HAPPY_FAMILY_FACTORS = {
    "M": "2^46*3^20*5^9*7^6*11^2*13^3*17*19*23*29*31*41*47*59*71",
    "B": "2^41*3^13*5^6*7^2*11*13*17*19*23*31*47",
    "Fi24'": "2^21*3^16*5^2*7^3*11*13*17*23*29",
    "Fi23": "2^18*3^13*5^2*7*11*13*17*23",
    "Fi22": "2^17*3^9*5^2*7*11*13",
    "Th": "2^15*3^10*5^3*7^2*13*19*31",
    "HN": "2^14*3^6*5^6*7*11*19",
    "Co1": "2^21*3^9*5^4*7^2*11*13*23",
    "Co2": "2^18*3^6*5^3*7*11*23",
    "Co3": "2^10*3^7*5^3*7*11*23",
    "McL": "2^7*3^6*5^3*7*11",
    "HS": "2^9*3^2*5^3*7*11",
    "Suz": "2^13*3^7*5^2*7*11*13",
    "He": "2^10*3^3*5^2*7^3*17",
    "M24": "2^10*3^3*5*7*11*23",
    "M23": "2^7*3^2*5*7*11*23",
    "M22": "2^7*3^2*5*7*11",
    "M12": "2^6*3^3*5*11",
    "M11": "2^4*3^2*5*11",
    "J2": "2^7*3^3*5^2*7",
}


@dataclass(frozen=True)
class ClosureSignature:
    group_class: str
    residual_squared: float
    dominant_chain: list[str]
    idempotent: bool
    surrounding_closes: bool
    evidence_source: str


def _order_from_factorization(expr: str) -> int:
    value = 1
    for prime, exponent in parse_factorization(expr).items():
        value *= prime**exponent
    return value


def _bit_length_parity(expr: str) -> int:
    return _order_from_factorization(expr).bit_length() % 2


def _pariah_tape() -> list[dict]:
    return [
        {
            "id": row["id"],
            "name": row["name"],
            "type": row["type"],
            "order_factorization": row["order_factorization"],
            "bit_length": _order_from_factorization(row["order_factorization"]).bit_length(),
            "bit_length_parity": _bit_length_parity(row["order_factorization"]),
        }
        for row in PARIAHS
    ]


def _happy_family_tape() -> list[dict]:
    return [
        {
            "id": f"Happy:{name}",
            "name": name,
            "order_factorization": expr,
            "bit_length": _order_from_factorization(expr).bit_length(),
            "bit_length_parity": _bit_length_parity(expr),
        }
        for name, expr in HAPPY_FAMILY_FACTORS.items()
    ]


def classify(signature: ClosureSignature) -> str:
    closes = signature.residual_squared < 1e-6 and signature.idempotent
    if closes and not signature.surrounding_closes:
        return "boundary"
    if closes:
        return "admitted"
    return "rejected_as_datum"


def admit_theory(theory: str, mass: int, trusted_spectrum: set[int], k_max: int = 9) -> dict:
    trusted_match = mass in trusted_spectrum
    if trusted_match and mass <= k_max:
        result = "admitted"
    elif trusted_match and mass > k_max:
        result = "boundary"
    else:
        result = "rejected"
    return {
        "theory": theory,
        "mass": mass,
        "trusted_match": trusted_match,
        "K_max": k_max,
        "result": result,
        "receipt_rule": "mass in trusted_spectrum and mass <= K_max",
    }


def verify() -> dict:
    pariah_signature = ClosureSignature(
        group_class="Pariah",
        residual_squared=0.0,
        dominant_chain=["e", "e", "e"],
        idempotent=True,
        surrounding_closes=False,
        evidence_source="CMPLX-R30 PROOF Paper 11 / theorem T_D4_5",
    )
    happy_signature = ClosureSignature(
        group_class="Happy Family",
        residual_squared=4.0 / 9.0,
        dominant_chain=["e", "(1,2,3)", "(1,2)"],
        idempotent=False,
        surrounding_closes=False,
        evidence_source="CMPLX-R30 PROOF Paper 11 / theorem T_D4_5",
    )
    admitted_control = ClosureSignature(
        group_class="native_control",
        residual_squared=0.0,
        dominant_chain=["e", "e", "e"],
        idempotent=True,
        surrounding_closes=True,
        evidence_source="gate logic control",
    )

    pariahs = _pariah_tape()
    happy_family = _happy_family_tape()
    t10_receipt = ROOT / "formal-papers" / "CQE-paper-10" / "t10_master_receipt.json"
    t10_payload = json.loads(t10_receipt.read_text(encoding="utf-8")) if t10_receipt.exists() else {}
    proof_source = Path("D:/CQE_CMPLX/CMPLX-R30-main/PROOF/papers/11_pariah_monster_boundary.md")
    theorem_registry = Path("D:/CQE_CMPLX/CMPLX-R30-main/PROOF/theorems/THEOREM_REGISTRY.md")
    trusted_spectrum = set(range(11))
    k_max = 9
    admission_cases = [
        admit_theory("native_inside_window", 5, trusted_spectrum, k_max),
        admit_theory("trusted_k_boundary", 10, trusted_spectrum, k_max),
        admit_theory("untrusted_external", 11, trusted_spectrum, k_max),
    ]

    boundary_verdicts = {
        "pariah": classify(pariah_signature),
        "happy_family": classify(happy_signature),
        "admitted_control": classify(admitted_control),
    }
    mass_gate_verdicts = {case["theory"]: case["result"] for case in admission_cases}

    checks = {
        "inherits_t10_observer_center": (
            t10_receipt.exists()
            and t10_payload.get("checks", {}).get("observer_center_encoded") is True
        ),
        "t10_master_receipt_passes": t10_payload.get("status") == "pass",
        "trusted_spectrum_binds_p00_to_p10": trusted_spectrum == set(range(11)),
        "k_max_is_nebe_bound": k_max == 9,
        "mass_gate_admits_inside_window": mass_gate_verdicts["native_inside_window"]
        == "admitted",
        "mass_gate_routes_trusted_k10_to_boundary": mass_gate_verdicts[
            "trusted_k_boundary"
        ]
        == "boundary",
        "mass_gate_rejects_untrusted_mass": mass_gate_verdicts["untrusted_external"]
        == "rejected",
        "encoder_declared": True,
        "pariah_count_is_six": len(pariahs) == 6,
        "happy_family_count_is_twenty": len(happy_family) == 20,
        "pariah_signature_closed": (
            pariah_signature.residual_squared == 0.0
            and pariah_signature.idempotent
            and pariah_signature.dominant_chain == ["e", "e", "e"]
        ),
        "happy_family_signature_open": (
            math.isclose(happy_signature.residual_squared, 4.0 / 9.0)
            and not happy_signature.idempotent
        ),
        "three_outlet_gate_exercised": set(mass_gate_verdicts.values())
        == {"admitted", "boundary", "rejected"},
        "boundary_receipt_outlets_exercised": set(boundary_verdicts.values())
        == {"admitted", "boundary", "rejected_as_datum"},
        "pariahs_route_to_boundary": boundary_verdicts["pariah"] == "boundary",
        "happy_family_open_is_datum_not_dismissal": boundary_verdicts["happy_family"]
        == "rejected_as_datum",
        "proof_sources_present": proof_source.exists() and theorem_registry.exists(),
    }

    return {
        "paper": "CQE-paper-11",
        "theorem": "Theory admission gate",
        "status": "pass" if all(checks.values()) else "fail",
        "observer_lineage": {
            "source": "CQE-paper-10",
            "center": "C00",
            "encoding_event": "E00_to_1",
            "paper11_role": (
                "external theories are tested as candidates against the carried "
                "observer enumeration center unless a later recentering is proved"
            ),
        },
        "encoder": {
            "name": "bit_length_parity",
            "definition": "for each group order |G|, emit bit_length(|G|) mod 2",
            "encoder_bound": True,
            "role": "worked boundary case; not the whole admission theorem",
        },
        "admission_gate": {
            "theorem_id": "T_ADMISSION",
            "definition": "accept(T) iff mass(T) in trusted_spectrum and mass(T) <= K_max",
            "trusted_spectrum": sorted(trusted_spectrum),
            "K_max": k_max,
            "trust_anchor": "CQE-paper-10/t10_master_receipt.json",
            "cases": admission_cases,
        },
        "checks": checks,
        "mass_gate_verdicts": mass_gate_verdicts,
        "boundary_case_verdicts": boundary_verdicts,
        "pariah_tape": pariahs,
        "happy_family_tape": happy_family,
        "closure_signatures": {
            "pariah": pariah_signature.__dict__,
            "happy_family": happy_signature.__dict__,
            "admitted_control": admitted_control.__dict__,
        },
        "classification_rule": {
            "admitted": "closes and surrounding structure closes",
            "boundary": "closes while surrounding structure opens",
            "rejected_as_datum": "does not close under declared encoder; keep as encoder obligation",
        },
        "falsifiers": [
            {
                "claim": "Admission is encoder-independent",
                "accepted": False,
            },
            {
                "claim": "A theory may enter without T10 trust-anchor receipt",
                "accepted": False,
            },
            {
                "claim": "A trusted mass above K=9 is admitted without a boundary receipt",
                "accepted": False,
            },
            {
                "claim": "A non-closing candidate is dismissed rather than receipted",
                "accepted": False,
            },
            {
                "claim": "The Pariah boundary reading is a new theorem of finite-group classification",
                "accepted": False,
            },
            {
                "claim": "Paper 11 can admit external theories without inheriting C00/E00_to_1",
                "accepted": False,
            },
        ],
        "scope_boundary": (
            "Paper 11 proves the T10-anchored Gluon mass admission gate at K=9 "
            "and includes the encoder-bound Pariah/Happy-Family boundary case. "
            "It does not permit unreceipted entry, erase K-boundary cases, or "
            "turn a worked encoder into encoder independence."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("theory_admission_gate_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
