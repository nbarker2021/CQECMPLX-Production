# CADForge + SolidWorks Wrapper Adapter

## Position

CADForge does not replace SolidWorks. CADForge wraps the design-start problem
around SolidWorks.

SolidWorks remains the professional CAD environment where engineers finish
parts, assemblies, drawings, tolerances, mates, manufacturing features, and
exports. CADForge/WireBlock improves the front of that workflow by making the
starting geometry legal before it enters SolidWorks.

The wrapper rule:

```text
CADForge legal family
-> WireBlock legal attachables and bounded variables
-> WireForge wireframe skeleton
-> SolidWorks adapter macro
-> normal SolidWorks modeling workflow
```

## Why This Helps SolidWorks Users

The reported industry pain is not that SolidWorks is bad. It is that daily CAD
work can still suffer from:

```text
bad starting templates
over-flexible design space
manual rebuild loops
wrong anchor assumptions
late discovery of illegal geometry
unclear design intent after handoff
```

CADForge addresses those issues before the model becomes a SolidWorks part.

It supplies:

| CADForge/WireBlock layer | Material improvement |
|---|---|
| initialized design family | no blank-page start |
| legal attachable palette | no arbitrary unsupported feature families |
| bounded variable tweaker | fewer invalid dimensions |
| anchor validation | no attachable placed on a missing node |
| graph receipt | design intent survives handoff |
| SolidWorks macro adapter | no custom SolidWorks add-in required |

## Zero New SolidWorks Code Principle

The first integration requires no SolidWorks add-in.

It needs only:

```text
1. this Python library
2. a generated SolidWorks VBA macro module
3. a CADForge design or WireBlock receipt JSON
```

SolidWorks already supports VBA macros and API automation. The official
SOLIDWORKS API documentation describes macros and API automation, and
`ISketchManager.CreateLine` creates sketch lines in an active 2D or 3D sketch.

## Adapter Output

CADForge exports:

```text
cadforge_design.json
wireblock_receipt.json
solidworks_wireblock_import.bas
walkthrough.md
```

The `.bas` macro:

```text
opens a new SolidWorks part
starts a 3D sketch
creates line segments for legal WireBlock graph edges
prints the CADForge family/design id
rebuilds the part
leaves the engineer in SolidWorks for normal CAD completion
```

## Example

Python:

```python
from CADForge import CADForgeBuilder

builder = CADForgeBuilder("panel_bracket", name="solidworks_panel")
builder.tweak("width_mm", 96)
builder.attach("rib", anchor_node="base:n0")
paths = builder.export("exports/solidworks_panel")
print(paths["solidworks_macro"])
```

SolidWorks:

```text
1. Open SolidWorks.
2. Open the VBA macro editor.
3. Import or paste `solidworks_wireblock_import.bas`.
4. Run `CADForgeWireBlockImport`.
5. Use SolidWorks dimensions/features to finish the part.
```

## What The Adapter Does Not Claim

The adapter does not claim to finish production CAD automatically.

It does not replace:

```text
feature engineering
mates
tolerances
drawings
FEA
PDM rules
manufacturing review
professional judgment
```

It creates a legal, receipted starting skeleton and preserves design intent.

## Next Adapter Levels

Level 1, current:

```text
CADForge receipt -> SolidWorks VBA 3D sketch skeleton
```

Level 2:

```text
bounded variables -> SolidWorks dimensions and named parameters
```

Level 3:

```text
attachable types -> SolidWorks feature templates and library features
```

Level 4:

```text
WireBlock receipt -> drawing/BOM/checklist/PDM metadata
```

Level 5:

```text
MetaForge material tile -> SolidWorks part + simulation setup handoff
```

## Product Statement

CADForge improves SolidWorks materially by moving uncertainty out of the CAD
session and into a legal pre-CAD design kit. The engineer still uses SolidWorks,
but the first model state is already constrained, attachable-aware, variable
bounded, and receipted.
