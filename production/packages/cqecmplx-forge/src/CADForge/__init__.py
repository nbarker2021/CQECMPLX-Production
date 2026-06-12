"""CADForge - simple constrained CAD builder over WireBlock and WireForge."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Mapping
import json

from WireBlockEngine import (
    attach,
    design_receipt,
    design_walkthrough,
    families,
    initialize_design,
    tweak,
)
from CADForge.solidworks_adapter import emit_solidworks_vba, export_solidworks_adapter


class CADForgeBuilder:
    """Stateful helper for walking a user through a legal CAD design."""

    def __init__(self, family: str = "panel_bracket", *, name: str = "untitled", variables: Mapping[str, Any] | None = None):
        self.design = initialize_design(family, name=name, variables=variables)

    def attach(self, attachable: str, **kwargs: Any) -> "CADForgeBuilder":
        self.design = attach(self.design, attachable, **kwargs)
        return self

    def tweak(self, variable: str, value: Any) -> "CADForgeBuilder":
        self.design = tweak(self.design, variable, value)
        return self

    def receipt(self) -> Dict[str, Any]:
        return design_receipt(self.design)

    def export(self, outdir: str | Path) -> Dict[str, str]:
        out = Path(outdir)
        out.mkdir(parents=True, exist_ok=True)
        design_path = out / "cadforge_design.json"
        receipt_path = out / "wireblock_receipt.json"
        solidworks_path = out / "solidworks_wireblock_import.bas"
        walkthrough_path = out / "walkthrough.md"
        receipt = self.receipt()
        design_path.write_text(json.dumps(self.design, indent=2, sort_keys=True), encoding="utf-8")
        receipt_path.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
        export_solidworks_adapter(receipt, solidworks_path)
        walkthrough_path.write_text(render_walkthrough(self.design), encoding="utf-8")
        return {
            "design": str(design_path),
            "receipt": str(receipt_path),
            "solidworks_macro": str(solidworks_path),
            "walkthrough": str(walkthrough_path),
        }


def render_walkthrough(design: Mapping[str, Any]) -> str:
    """Render a concise human walkthrough for a design state."""
    family = str(design.get("family", "panel_bracket"))
    walk = design_walkthrough(family)
    lines = [
        f"# CADForge Walkthrough - {design.get('name', 'untitled')}",
        "",
        f"Family: `{family}`",
        "",
        walk["description"],
        "",
        "## Legal Variables",
        "",
    ]
    for key, spec in walk["variable_schema"].items():
        current = design.get("variables", {}).get(key, spec["default"])
        lines.append(
            f"- `{key}` = {current} {spec['unit']} "
            f"(range {spec['minimum']}..{spec['maximum']}, step {spec['step']})"
        )
    lines += ["", "## Legal Attachables", ""]
    for key, spec in walk["allowed_attachables"].items():
        count = sum(1 for item in design.get("attachables", []) if item.get("name") == key)
        lines.append(
            f"- `{key}` uses `{spec['template']}` as `{spec['edge_type']}` "
            f"({count}/{spec['max_count']} attached)"
        )
    lines += ["", "## Current Build", ""]
    lines.append(f"- Nodes: {len(design.get('nodes', []))}")
    lines.append(f"- Edges: {len(design.get('edges', []))}")
    lines.append(f"- Attachables: {len(design.get('attachables', []))}")
    lines += ["", "## Walkthrough", ""]
    for idx, step in enumerate(walk["steps"], start=1):
        lines.append(f"{idx}. {step}")
    lines.append("")
    return "\n".join(lines)


def create_design(
    family: str = "panel_bracket",
    *,
    name: str = "untitled",
    variables: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    return initialize_design(family, name=name, variables=variables)


def demo_design() -> Dict[str, Any]:
    builder = CADForgeBuilder("panel_bracket", name="demo_panel_bracket")
    builder.tweak("width_mm", 96).tweak("height_mm", 64)
    builder.attach("rib", anchor_node="base:n0", attachment_id="rib_left", scale=0.5)
    builder.attach("mount_ring", anchor_node="base:n3", attachment_id="mount_ring_right", scale=0.45)
    return builder.receipt()


__all__ = [
    "CADForgeBuilder",
    "create_design",
    "demo_design",
    "emit_solidworks_vba",
    "export_solidworks_adapter",
    "families",
    "render_walkthrough",
]
