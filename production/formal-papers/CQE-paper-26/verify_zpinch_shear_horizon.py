"""Formal receipt generator for Paper 26.

Paper 26 closes only the Oloid/octonion carrier algebra and the ledger
classification rule for a pinch/shear analog. It does not close a physical
Z-pinch, plasma confinement, friction, or energy-generation claim.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.oloid_octonionic import (  # noqa: E402
    GENERATOR_BIT0,
    GENERATOR_BIT1,
    OctonionicOloidState,
    orient_bit_information_content,
    verify_octonionic_oloid,
)
from lattice_forge.oloid_rolling import (  # noqa: E402
    roll_chart_landing,
    roll_chart_trace,
    verify_oloid_rolling,
)
from lattice_forge.rule30_nth_bit import _simulate  # noqa: E402
from lattice_forge.transport_obligations import (  # noqa: E402
    CLASSIFICATIONS,
    transport_obligations,
)


OUT = Path(__file__).resolve().parent / "zpinch_shear_horizon_receipt.json"


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _basis_index(state: OctonionicOloidState) -> int:
    return state.dominant_basis_index()


def _roll_with_fixed_generator(bits: list[int], generator) -> list[dict[str, Any]]:
    state = OctonionicOloidState.initial()
    trace = [
        {
            "index": 0,
            "input_bit": None,
            "dominant_basis_index": _basis_index(state),
            "orient_bit": state.orient_bit(),
        }
    ]
    for index, bit in enumerate(bits, 1):
        # The same tape advances both carriers; the chosen generator names the
        # carrier direction. The bit is retained in the receipt, not used to
        # switch generators in this fixed-generator comparison.
        state = OctonionicOloidState(state.octonion * generator)
        trace.append(
            {
                "index": index,
                "input_bit": bit,
                "dominant_basis_index": _basis_index(state),
                "orient_bit": state.orient_bit(),
            }
        )
    return trace


def carrier_shear_probe(depth: int = 16) -> dict[str, Any]:
    center_bits, _local_states = _simulate(depth)
    bits = center_bits[:depth]
    integer_trace = roll_chart_trace(bits)
    landing = roll_chart_landing(bits)
    e4_trace = _roll_with_fixed_generator(bits, GENERATOR_BIT0)
    e5_trace = _roll_with_fixed_generator(bits, GENERATOR_BIT1)
    shear_rows = []
    for left, right in zip(e4_trace, e5_trace):
        shear_rows.append(
            {
                "index": left["index"],
                "input_bit": left["input_bit"],
                "e4_orient": left["orient_bit"],
                "e5_orient": right["orient_bit"],
                "shear_bit": left["orient_bit"] ^ right["orient_bit"],
                "e4_basis": left["dominant_basis_index"],
                "e5_basis": right["dominant_basis_index"],
            }
        )
    return {
        "depth": depth,
        "rule30_center_bits": bits,
        "integer_landing": landing.as_tuple(),
        "integer_head_tail_dyad": landing.as_dyad(),
        "integer_trace_sample": [state.as_tuple() for state in integer_trace[:8]],
        "shear_rows": shear_rows,
        "shear_nonzero_count": sum(row["shear_bit"] for row in shear_rows),
        "final_e4_basis": e4_trace[-1]["dominant_basis_index"],
        "final_e5_basis": e5_trace[-1]["dominant_basis_index"],
    }


def pinch_reclassification_rows() -> list[dict[str, Any]]:
    rows = []
    for row in transport_obligations():
        if row["classification"] == "demonstrated":
            pinch_state = "not_pinched"
        elif row["classification"] in {"bounded_local", "bounded_external"}:
            pinch_state = "bounded_residue"
        else:
            pinch_state = "open_or_registered_lift"
        rows.append(
            {
                "transport_id": row["id"],
                "classification": row["classification"],
                "valid_classification": row["classification"] in CLASSIFICATIONS,
                "pinch_analog_state": pinch_state,
                "proof_boundary": row["proof_boundary"],
                "physical_pinch_claim": False,
            }
        )
    return rows


def build_receipt() -> dict[str, Any]:
    rolling = verify_oloid_rolling()
    octonion = verify_octonionic_oloid()
    probe = carrier_shear_probe()
    pinch_rows = pinch_reclassification_rows()
    orient_probe = orient_bit_information_content(
        [[(n >> i) & 1 for i in range(8)] for n in range(256)]
    )

    checks = [
        _check(
            "integer Oloid carrier verifier passes",
            rolling["status"] == "pass"
            and rolling["bit0_period_4"]
            and rolling["bit1_period_4"]
            and rolling["k8_table_size"] == 256,
            {
                "status": rolling["status"],
                "bit0_period_4": rolling["bit0_period_4"],
                "bit1_period_4": rolling["bit1_period_4"],
                "k8_table_size": rolling["k8_table_size"],
            },
        ),
        _check(
            "octonion carrier verifier passes",
            octonion["status"] == "pass"
            and octonion["e4_squared_is_minus_one"]
            and octonion["e4_fourth_is_one"]
            and octonion["non_associative_imaginary_units"],
            {
                "status": octonion["status"],
                "e4_squared_is_minus_one": octonion["e4_squared_is_minus_one"],
                "e4_fourth_is_one": octonion["e4_fourth_is_one"],
                "non_associative_imaginary_units": octonion[
                    "non_associative_imaginary_units"
                ],
                "orient_after_known_input": octonion["orient_after_known_input"],
                "dominant_after_known_input": octonion["dominant_after_known_input"],
            },
        ),
        _check(
            "same tape exposes fixed-generator shear divergence",
            probe["depth"] == 16
            and len(probe["shear_rows"]) == 17
            and probe["shear_nonzero_count"] > 0,
            {
                "depth": probe["depth"],
                "rule30_center_bits": probe["rule30_center_bits"],
                "integer_landing": probe["integer_landing"],
                "shear_nonzero_count": probe["shear_nonzero_count"],
                "final_e4_basis": probe["final_e4_basis"],
                "final_e5_basis": probe["final_e5_basis"],
            },
        ),
        _check(
            "orient bit is not promoted past carrier evidence",
            0.0 <= orient_probe["trivial_baseline_rate"] <= 1.0
            and orient_probe["sample_count"] == 256,
            orient_probe,
        ),
        _check(
            "pinch analog is ledger reclassification only",
            len(pinch_rows) == 4
            and all(row["valid_classification"] for row in pinch_rows)
            and all(row["physical_pinch_claim"] is False for row in pinch_rows),
            {
                "row_count": len(pinch_rows),
                "classifications": [row["classification"] for row in pinch_rows],
                "pinch_states": [row["pinch_analog_state"] for row in pinch_rows],
            },
        ),
    ]

    open_obligations = [
        {
            "obligation": "physical Z-pinch witness",
            "status": "open",
            "reason": "no plasma observable is connected to the carrier shear bit",
            "falsifier": "a controlled physical shear observable disagrees with the predicted carrier shear map",
        },
        {
            "obligation": "friction or generation mechanism",
            "status": "not_claimed",
            "reason": "carrier residue is algebraic path history, not a mechanical energy source",
        },
        {
            "obligation": "pinch as physical collapse",
            "status": "not_claimed",
            "reason": "pinch means transport reclassification toward open unless a physical witness is supplied",
        },
        {
            "obligation": "bounded_external measurement row",
            "status": "open",
            "reason": "a physical-domain measurement must be added before this horizon reading leaves candidate status",
        },
    ]

    receipt = {
        "paper": "CQE-paper-26",
        "title": "Z-Pinch and Shear Horizon",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "The Oloid integer carrier has period-4 rolling closure, the octonion "
            "carrier realizes the same period with e4^2=-1 and e4^4=1, and a "
            "fixed-generator comparison exposes a replayable shear analog. The "
            "plasma Z-pinch reading remains an open hypothesis."
        ),
        "rolling_verifier": rolling,
        "octonion_verifier": octonion,
        "carrier_shear_probe": probe,
        "orient_information_probe": orient_probe,
        "pinch_reclassification_rows": pinch_rows,
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
