# CADForge + WireBlock Promotion Slice

## Product Explanation

CADForge is the CAD-facing Forge product. WireBlock is the engine that manages
legality. Together they make CAD design simple by starting from initialized
wireframe families instead of an empty modeling space.

The rule:

```text
initialized CAD family
-> legal base wireframe
-> legal attachable list
-> bounded variable tweaker
-> graph receipt
-> CAD/BOM/toolpath adapter
```

The user does not draw arbitrary geometry first. CADForge supplies the legal
shape family and the user assembles from allowed wireframe attachables.

## Why This Fits The Forge Family

| Forge slot | CADForge / WireBlock expression |
|---|---|
| Identity | `CADForge` product, `WireBlock` engine |
| Engine | legality kernel for initialized wireframe CAD |
| Math | graph constraints, LCR block readout, bounded variables |
| Tool | Python package functions and builder class |
| Product | simple CAD design workflow |
| Adapter | WireForge templates, FrameForge motion, future CAD export adapters |
| Receipt | `WireBlock` receipt with nodes, edges, variables, attachables |
| Workbook | step-by-step constrained design walkthrough |
| Obligation | downstream STEP/STL/BOM/toolpath exporters still need adapters |

## Current Implemented Families

```text
panel_bracket
enclosure_shell
metamaterial_tile
```

Each family declares:

```text
base_template
description
allowed_attachables
bounded variables
```

## Example

```python
from CADForge import CADForgeBuilder

builder = CADForgeBuilder("panel_bracket", name="demo_panel_bracket")
builder.tweak("width_mm", 96)
builder.attach("rib", anchor_node="base:n0")
receipt = builder.receipt()
```

This produces a legal graph receipt. Illegal attachables, illegal anchor nodes,
out-of-range variables, and uninitialized design states are rejected.

## SolidWorks Wrapper Path

CADForge is also designed as a wrapper around existing professional CAD tools,
starting with SolidWorks. The first adapter exports a `.bas` VBA macro module
from the WireBlock receipt. A SolidWorks user can import/run that macro to
create a legal wire skeleton in a new part, then continue the normal SolidWorks
workflow.

```text
CADForge design -> WireBlock receipt -> SolidWorks VBA macro -> SolidWorks part
```

This requires no custom SolidWorks add-in for the first stage: only this library
and the generated adapter script.

## Product Ladder Context

The same library supports simple and high-end products:

| Product | Simple description |
|---|---|
| GraphStax + FridgeForge | USB calendar/recipe/inventory appliance with graph receipts |
| LinkForge | connect calendars, lists, JSON, CSV, and external files once, then reuse |
| PixelForge / PixL8Forge | visible image/frame state tools |
| WireForge / FrameForge | wireframe templates and motion over wireframes |
| CADForge / WireBlock | constrained CAD assembly from legal wireframe attachables |
| MetaForge | high-end metamaterial design and physics pipeline |

## Open Obligations

1. Add CAD export adapters for STEP/STL/SVG/DXF.
2. Add UI controls for family selection, attachable selection, anchor picking,
   and variable sliders.
3. Add GraphStax identity resolution over final CAD graph nodes.
4. Add FridgeForge-style local persistence so CAD sessions can run from a USB
   stick as a small offline product.
5. Add MetaForge bridge so `metamaterial_tile` designs can become physics
   candidates.
6. Promote the SolidWorks macro adapter from wire skeleton import to named
   dimensions, feature templates, and drawing/BOM metadata.
