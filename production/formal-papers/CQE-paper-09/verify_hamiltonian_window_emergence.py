#!/usr/bin/env python3
"""Verifier for CQE Paper 09, Hamiltonian Window Emergence."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "packages" / "cqecmplx-forge" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from lattice_forge.temporal_z4_scope import verify_temporal_z4_scope  # noqa: E402


@dataclass(frozen=True)
class CenterState:
    paper: str
    center: str


BASE_CENTERS = [
    CenterState("CQE-paper-00", "Gluon_Gamma"),
    CenterState("CQE-paper-01", "SideFlip_C1"),
    CenterState("CQE-paper-02", "Correction_C2"),
    CenterState("CQE-paper-03", "Triality_C3"),
    CenterState("CQE-paper-04", "Repair_C4"),
    CenterState("CQE-paper-05", "Carrier_C5"),
]


def hamiltonian_read(order: int, states: list[CenterState]) -> list[dict]:
    widths = {2: 3, 3: 5, 4: 7}
    width = widths[order]
    if len(states) < width:
        return []
    reads = []
    for start in range(len(states) - width + 1):
        window = states[start : start + width]
        centers = [state.center for state in window]
        papers = [state.paper for state in window]
        forward = " -> ".join(centers)
        backward = " <- ".join(reversed(centers))
        composite = "C[" + "|".join(centers) + "]"
        reads.append(
            {
                "order": order,
                "width": width,
                "start": start,
                "source_indices": list(range(start, start + width)),
                "source_papers": papers,
                "source_centers": centers,
                "forward": forward,
                "backward": backward,
                "surviving_center": composite,
                "reverse_receipt_well_formed": list(reversed(backward.split(" <- "))) == centers,
            }
        )
    return reads


def emit_state(paper: str, reads: list[dict]) -> CenterState:
    return CenterState(paper, "||".join(read["surviving_center"] for read in reads))


def iterative_hamiltonian() -> dict:
    states = list(BASE_CENTERS)

    order2 = hamiltonian_read(2, states)
    states.append(emit_state("CQE-paper-06", order2))

    order3 = hamiltonian_read(3, states)
    states.append(emit_state("CQE-paper-07", order3))

    order4 = hamiltonian_read(4, states)
    states.append(emit_state("CQE-paper-08", order4))

    return {
        "orders": {2: order2, 3: order3, 4: order4},
        "final_states": [{"paper": state.paper, "center": state.center} for state in states],
    }


def verify() -> dict:
    result = iterative_hamiltonian()
    orders = result["orders"]
    temporal_scope = verify_temporal_z4_scope(max_depth=64)

    all_reads = [read for reads in orders.values() for read in reads]
    checks = {
        "order2_width3_count_is_four": len(orders[2]) == 4,
        "order3_width5_count_is_three": len(orders[3]) == 3,
        "order4_width7_count_is_two": len(orders[4]) == 2,
        "all_reads_preserve_source_indices": all(
            len(read["source_indices"]) == read["width"] for read in all_reads
        ),
        "all_reads_preserve_source_centers": all(
            read["surviving_center"] == "C[" + "|".join(read["source_centers"]) + "]"
            for read in all_reads
        ),
        "all_backward_receipts_reverse_to_forward": all(
            read["reverse_receipt_well_formed"] for read in all_reads
        ),
        "static_z4_does_not_prove_temporal_periodicity": (
            temporal_scope["status"] == "static_template_only"
            and temporal_scope["temporal_period_claim_supported"] is False
        ),
    }

    return {
        "paper": "CQE-paper-09",
        "theorem": "Hamiltonian window emergence",
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "order_counts": {
            "order_2_width_3": len(orders[2]),
            "order_3_width_5": len(orders[3]),
            "order_4_width_7": len(orders[4]),
        },
        "orders": orders,
        "final_state_count": len(result["final_states"]),
        "temporal_z4_scope": {
            "status": temporal_scope["status"],
            "max_depth_tested": temporal_scope["max_depth_tested"],
            "temporal_period_claim_supported": temporal_scope["temporal_period_claim_supported"],
            "proof_boundary": temporal_scope["proof_boundary"],
        },
        "falsifiers": [
            {
                "claim": "the static Z4 chart template proves the temporal trace is period 4",
                "accepted": False,
            },
            {
                "claim": "a reverse receipt proves physical time reversal",
                "accepted": False,
            },
            {
                "claim": "a composite center is valid without source-window provenance",
                "accepted": False,
            },
        ],
        "scope_boundary": (
            "The paper proves finite local-window emergence and receipt-level "
            "reverse readability; it does not prove physical time reversal, "
            "static-Z4 temporal periodicity, or higher-order convergence."
        ),
    }


def main() -> None:
    result = verify()
    out = Path(__file__).with_name("hamiltonian_window_emergence_receipt.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
