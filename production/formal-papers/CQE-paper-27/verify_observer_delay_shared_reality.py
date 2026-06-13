"""Formal receipt generator for Paper 27.

Paper 27 closes static observer-frame and shared-center facts while preserving
observer delay and shared-reality language as interpretation. Its central
negative result is that the static Z4 frame template does not become a temporal
Rule 30 period over the tested trace.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.centroid_voa import (  # noqa: E402
    STATES,
    anneal_to_lie_conjugate,
    four_frame_label,
    gluon,
    swap_LR,
    verify_gluon_invariance,
    verify_z4_period_template,
    z4_period,
)
from lattice_forge.rule30 import canonical_rows  # noqa: E402
from lattice_forge.temporal_z4_scope import verify_temporal_z4_scope  # noqa: E402


OUT = Path(__file__).resolve().parent / "observer_delay_shared_reality_receipt.json"


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def observer_window_rows(max_depth: int = 64) -> dict[str, Any]:
    rows = canonical_rows(max_depth)
    receipt_rows: list[dict[str, Any]] = []
    delay_counts: dict[int, int] = {}
    side_disagreement_count = 0
    for depth in range(1, max_depth + 1):
        state = (
            rows[depth - 1].get(-1, 0),
            rows[depth - 1].get(0, 0),
            rows[depth - 1].get(1, 0),
        )
        reflected = swap_LR(state)
        anneal = anneal_to_lie_conjugate(state)
        delay = int(anneal["steps"])
        delay_counts[delay] = delay_counts.get(delay, 0) + 1
        side_disagrees = state[0] != state[2]
        side_disagreement_count += int(side_disagrees)
        receipt_rows.append(
            {
                "depth": depth,
                "state": state,
                "opposite_boundary_state": reflected,
                "observer_a_center": gluon(state),
                "observer_b_center": gluon(reflected),
                "shared_center": gluon(state) == gluon(reflected),
                "side_disagrees": side_disagrees,
                "anneal_delay_steps": delay,
                "anneal_final": anneal["final"],
                "four_frame_label": four_frame_label(state),
                "z4_period": z4_period(state),
                "emitted_center_bit": rows[depth].get(0, 0),
            }
        )
    return {
        "max_depth": max_depth,
        "rows_sample": receipt_rows[:16],
        "all_rows_share_center": all(row["shared_center"] for row in receipt_rows),
        "max_delay_steps": max(row["anneal_delay_steps"] for row in receipt_rows),
        "delay_counts": {str(k): v for k, v in sorted(delay_counts.items())},
        "side_disagreement_count": side_disagreement_count,
        "row_count": len(receipt_rows),
    }


def static_template_table() -> dict[str, Any]:
    return {
        str(state): {
            "four_frame_label": four_frame_label(state),
            "z4_period": z4_period(state),
            "gluon": gluon(state),
            "opposite_boundary_gluon": gluon(swap_LR(state)),
            "anneal_delay_steps": anneal_to_lie_conjugate(state)["steps"],
        }
        for state in STATES
    }


def build_receipt() -> dict[str, Any]:
    z4 = verify_z4_period_template()
    temporal = verify_temporal_z4_scope(max_depth=512)
    gluon_invariance = verify_gluon_invariance()
    observer_rows = observer_window_rows(max_depth=64)
    table = static_template_table()

    checks = [
        _check(
            "static Z4 template passes",
            z4["status"] == "pass"
            and z4["fixed_point_count"] == 2
            and z4["period_2_count"] == 0
            and z4["period_4_count"] == 6,
            {
                "status": z4["status"],
                "fixed_point_count": z4["fixed_point_count"],
                "period_2_count": z4["period_2_count"],
                "period_4_count": z4["period_4_count"],
            },
        ),
        _check(
            "temporal Z4 promotion is refuted over tested trace",
            temporal["status"] == "static_template_only"
            and temporal["temporal_period_claim_supported"] is False
            and all(not value for value in temporal["temporal_label_trace_periodic"].values())
            and all(not value for value in temporal["center_column_periodic"].values()),
            {
                "status": temporal["status"],
                "max_depth_tested": temporal["max_depth_tested"],
                "temporal_label_trace_periodic": temporal["temporal_label_trace_periodic"],
                "center_column_periodic": temporal["center_column_periodic"],
                "label_counterexamples": temporal["label_counterexamples"],
                "center_counterexamples": temporal["center_counterexamples"],
            },
        ),
        _check(
            "gluon center is shared under opposite-boundary reads",
            gluon_invariance["status"] == "pass"
            and observer_rows["all_rows_share_center"]
            and observer_rows["side_disagreement_count"] > 0,
            {
                "gluon_status": gluon_invariance["status"],
                "states_checked": gluon_invariance["states_checked"],
                "rows_checked": observer_rows["row_count"],
                "side_disagreement_count": observer_rows["side_disagreement_count"],
            },
        ),
        _check(
            "anneal delay remains bounded by three steps",
            observer_rows["max_delay_steps"] <= 3
            and set(observer_rows["delay_counts"]).issubset({"0", "1", "2", "3"}),
            {
                "max_delay_steps": observer_rows["max_delay_steps"],
                "delay_counts": observer_rows["delay_counts"],
            },
        ),
        _check(
            "observer interpretations are not promoted",
            True,
            {
                "consciousness_claim": False,
                "measurement_collapse_claim": False,
                "relativistic_simultaneity_claim": False,
                "human_latency_claim": False,
            },
        ),
    ]

    open_obligations = [
        {
            "obligation": "human latency model",
            "status": "not_claimed",
            "reason": "anneal steps are finite chart steps, not measured response times",
            "falsifier": "a latency experiment whose timing distribution cannot be mapped to the 0/1/2/3-step receipt",
        },
        {
            "obligation": "shared reality interpretation",
            "status": "interpretive",
            "reason": "shared C is a center invariant, not a proof of physical simultaneity",
        },
        {
            "obligation": "consciousness or collapse reading",
            "status": "not_claimed",
            "reason": "the static frame and shared-center receipts do not imply consciousness or measurement collapse",
        },
        {
            "obligation": "temporal Z4 period",
            "status": "refuted_for_tested_trace",
            "reason": "Rule 30 label trace and center column do not inherit periods 1, 2, or 4 over the tested window",
        },
    ]

    receipt = {
        "paper": "CQE-paper-27",
        "title": "Observer Delay and Shared Reality",
        "status": "pass_with_interpretive_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "The static four-frame Z4 template is exact, opposite-boundary "
            "observers share the same center C, and read-then-anneal delay is "
            "bounded in the finite chart. The Z4 template is explicitly refuted "
            "as a temporal Rule 30 period over the tested trace."
        ),
        "static_template_table": table,
        "z4_template": {
            "status": z4["status"],
            "fixed_point_count": z4["fixed_point_count"],
            "period_2_count": z4["period_2_count"],
            "period_4_count": z4["period_4_count"],
        },
        "temporal_scope": temporal,
        "gluon_invariance": gluon_invariance,
        "observer_rows": observer_rows,
        "checks": checks,
        "open_obligations": open_obligations,
    }
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    return receipt


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2))
    return 0 if receipt["status"] == "pass_with_interpretive_obligations" else 1


if __name__ == "__main__":
    raise SystemExit(main())
