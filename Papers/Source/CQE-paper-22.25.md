# Paper 22.25 - MetaForge Toolkit Supplement

## Purpose

This supplement describes how to run and inspect the MetaForge materials
pipeline. It supports Paper 22 but does not replace its proof.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-22/verify_metaforge_materials.py`

The expected status is `pass_with_open_obligations`. The run writes
`metaforge_materials_receipt.json` and checks material inventory, Pareto partner
selection, ten-fold evaluation, seam proposal, production accounting, and
additional material-pair replay.

## Package Route

The promoted package lives at:

`production/lib-forge/CQECMPLX-MetaMaterial-Designer/meta_material_system`

The key source surfaces are:

- `material_db.py` for material records,
- `pareto_partnering.py` for partner scoring,
- `fold_evaluation.py` for ten-fold candidate transport,
- `seam_detection.py` for mitigation rows,
- `production_energy.py` for production estimates,
- `meta_material_designer.py` for the combined pipeline.

## Analog Route

A reviewer can reproduce the candidate logic with cards. Each material is a
card with lattice, property, gluon, and oloid fields. Pair cards by score,
advance the chosen pair through ten fold cards, place an error-wall token when a
fold creates a boundary issue, and then attach seam cards as mitigation rows.
The analog version is accepted only if it preserves the same candidate status:
not fabricated, not measured, and not promoted beyond its receipt.

## Hidden-Guess Diagnostic

Training mode should hide the diagnostic label until after the reviewer chooses
one:

- valid candidate,
- invalid material row,
- partner-score row,
- fold-accounting row,
- seam obligation,
- production estimate,
- invalid promotion.

The revealed answer teaches the boundary between a generated candidate and a
tested material.
