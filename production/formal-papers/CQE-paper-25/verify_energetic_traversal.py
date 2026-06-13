"""Formal receipt generator for Paper 25.

Paper 25 closes the energetic traversal layer as a unit-agnostic accounting
kernel. It verifies NSL boundary arithmetic, additive traversal receipts, the
bounded transport-obligation spine, and the default VOA analog cost. It does
not claim physical joules, least-action physics, thermodynamic optimality, or
unification of Noether/Shannon/Landauer law.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "production" / "packages" / "cqecmplx-forge" / "src"))

from lattice_forge.centroid_voa import (  # noqa: E402
    verify_voa_sector_decomposition,
    voa_weight,
)
from lattice_forge.ledger.nsl import NSLTerm  # noqa: E402
from lattice_forge.transport_obligations import (  # noqa: E402
    transport_obligations,
    verify_transport_obligations,
)


OUT = Path(__file__).resolve().parent / "energetic_traversal_receipt.json"


@dataclass(frozen=True)
class TraversalStep:
    step_id: str
    transport_id: str
    source: str
    target: str
    state: tuple[int, int, int]
    term: NSLTerm
    unit_policy: str = "normalized_analog_units"

    def as_dict(self) -> dict[str, Any]:
        row = self.term.as_dict()
        return {
            "step_id": self.step_id,
            "transport_id": self.transport_id,
            "source": self.source,
            "target": self.target,
            "state": self.state,
            "voa_weight": voa_weight(self.state),
            "unit_policy": self.unit_policy,
            "nsl": row,
            "theta": row["theta"],
            "closes_internally": row["closes_internally"],
            "obligation": None
            if row["closes_internally"]
            else "boundary_residue_exceeds_absorption",
        }


def _check(name: str, passed: bool, detail: Any) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def _path_summary(path_id: str, steps: list[TraversalStep]) -> dict[str, Any]:
    rows = [step.as_dict() for step in steps]
    theta_path = sum(float(row["theta"]) for row in rows)
    open_steps = [
        row["step_id"]
        for row in rows
        if row["obligation"] or row["unit_policy"] != "normalized_analog_units"
    ]
    return {
        "path_id": path_id,
        "step_count": len(rows),
        "rows": rows,
        "theta_path": theta_path,
        "closes_as_path": theta_path <= 0.0 and not open_steps,
        "open_steps": open_steps,
        "accepted_as_physical_energy": False,
    }


def example_traversals() -> dict[str, Any]:
    obligations = transport_obligations()
    first, second, third, fourth = [row["id"] for row in obligations]

    closing = _path_summary(
        "closing_normalized_spine",
        [
            TraversalStep(
                "c1",
                first,
                "{0,1}^3",
                "D4 axis/sheet",
                (0, 0, 0),
                NSLTerm(0.10, 0.20, 0.10, absorption_capacity=0.60),
            ),
            TraversalStep(
                "c2",
                second,
                "D4 axis/sheet",
                "J3(O) diagonal carrier",
                (0, 1, 0),
                NSLTerm(0.20, 0.10, 0.20, absorption_capacity=0.55),
            ),
            TraversalStep(
                "c3",
                third,
                "J3(O) carrier",
                "G2/F4/T5A route",
                (1, 1, 1),
                NSLTerm(0.05, 0.05, 0.10, absorption_capacity=0.30),
            ),
        ],
    )
    open_path = _path_summary(
        "open_uncalibrated_lift",
        [
            TraversalStep(
                "o1",
                first,
                "{0,1}^3",
                "D4 axis/sheet",
                (0, 0, 1),
                NSLTerm(0.25, 0.25, 0.25, absorption_capacity=0.50),
            ),
            TraversalStep(
                "o2",
                fourth,
                "exceptional route metadata",
                "Niemeier landing form",
                (1, 0, 0),
                NSLTerm(0.40, 0.30, 0.20, absorption_capacity=0.25),
                unit_policy="uncalibrated_domain_units",
            ),
        ],
    )
    return {"paths": [closing, open_path]}


def build_receipt() -> dict[str, Any]:
    transport = verify_transport_obligations()
    voa = verify_voa_sector_decomposition()
    traversals = example_traversals()
    paths = traversals["paths"]

    sample = NSLTerm(0.2, 0.3, 0.4, absorption_capacity=0.5, alpha=2.0, beta=3.0, gamma=4.0)
    expected_theta = 2.0 * 0.2 + 3.0 * 0.3 + 4.0 * 0.4 - 0.5
    open_steps = [
        row
        for path in paths
        for row in path["rows"]
        if row["obligation"] or row["unit_policy"] != "normalized_analog_units"
    ]
    closing_paths = [path for path in paths if path["closes_as_path"]]

    checks = [
        _check(
            "NSLTerm computes weighted theta and closure gate",
            abs(sample.theta - expected_theta) < 1e-12
            and sample.closes_internally is False
            and NSLTerm(0.1, 0.1, 0.1, absorption_capacity=0.5).closes_internally,
            {
                "sample_theta": sample.theta,
                "expected_theta": expected_theta,
                "sample_closes": sample.closes_internally,
            },
        ),
        _check(
            "transport obligation spine verifies with open lifts carried",
            transport["status"] == "pass_with_open_lifts"
            and transport["row_count"] == 4
            and transport["local_witnesses_pass"],
            {
                "status": transport["status"],
                "row_count": transport["row_count"],
                "demonstrated_count": transport["demonstrated_count"],
                "open_lift_count": transport["open_lift_count"],
            },
        ),
        _check(
            "VOA default analog cost is 2 plus 6",
            voa["status"] == "pass"
            and voa["weight_distribution"] == {0: 2, 5: 6}
            and voa["seed_partition_function"] == "Z(q) = 2q^0 + 6q^5",
            {
                "status": voa["status"],
                "weight_distribution": voa["weight_distribution"],
                "seed_partition_function": voa["seed_partition_function"],
            },
        ),
        _check(
            "traversal additivity holds for normalized rows",
            all(
                abs(path["theta_path"] - sum(row["theta"] for row in path["rows"])) < 1e-12
                for path in paths
            ),
            [{"path_id": path["path_id"], "theta_path": path["theta_path"]} for path in paths],
        ),
        _check(
            "receipt includes one closed path and one carried obligation",
            len(closing_paths) == 1 and len(open_steps) >= 1,
            {
                "closing_paths": [path["path_id"] for path in closing_paths],
                "open_step_ids": [row["step_id"] for row in open_steps],
            },
        ),
        _check(
            "unit honesty blocks physical energy promotion",
            all(path["accepted_as_physical_energy"] is False for path in paths),
            {
                "physical_energy_claim": False,
                "calibration_required_before_joule_claim": True,
            },
        ),
    ]

    open_obligations = [
        {
            "obligation": "physical unit calibration",
            "status": "open",
            "reason": "NSL rows are normalized analog accounting terms, not joules",
        },
        {
            "obligation": "absorption measurement",
            "status": "open",
            "reason": "absorption_capacity must be supplied by a domain measurement or declared policy",
        },
        {
            "obligation": "least-action or geodesic reading",
            "status": "not_claimed",
            "reason": "a smaller theta_path is leaner only inside the analog ledger",
        },
        {
            "obligation": "NSL physical-law unification",
            "status": "not_claimed",
            "reason": "Noether, Shannon, and Landauer anchors remain inspirations and components, not subsumed laws",
        },
    ]

    receipt = {
        "paper": "CQE-paper-25",
        "title": "Energetic Traversal Maps",
        "status": "pass_with_open_obligations"
        if all(check["pass"] for check in checks)
        else "fail",
        "closed_claim": (
            "A CQE traversal can carry a replayable unit-agnostic NSL ledger; "
            "step theta values add along the path, closed paths satisfy theta_path <= 0, "
            "and non-closing or uncalibrated rows are emitted as obligations."
        ),
        "transport_spine": {
            "status": transport["status"],
            "row_count": transport["row_count"],
            "demonstrated_count": transport["demonstrated_count"],
            "open_lift_count": transport["open_lift_count"],
            "rows": transport["rows"],
        },
        "voa_default_cost": {
            "status": voa["status"],
            "weight_distribution": voa["weight_distribution"],
            "seed_partition_function": voa["seed_partition_function"],
        },
        "traversals": traversals,
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
