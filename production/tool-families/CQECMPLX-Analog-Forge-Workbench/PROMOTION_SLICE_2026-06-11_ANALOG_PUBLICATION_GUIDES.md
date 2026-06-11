# Promotion Slice: Analog Publication Guides

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-Analog-Forge-Workbench-Publication.manifest.json`

## Scope

This slice promotes the Analog Forge Workbench package surface plus publication
artifacts requested for the Basic and Pro analog toolkit descriptions.

## Included Source Roots

- `D:\CQE_CMPLX\_analog_workbench\ForgeFactory_AnalogWorkbench_Suite_v0_1`
- `C:\Users\nbark\OneDrive\Desktop\analog kit basic.txt`
- `C:\Users\nbark\OneDrive\Desktop\analog kit pro.txt`

## Included Package Content

- package README and `pyproject.toml`;
- analog workbench docs;
- workbook sheet templates;
- Python source modules;
- tests;
- manifest data.

## Included Publication Content

- `publication-source\analog-kit-basic.txt`
- `publication-source\analog-kit-pro.txt`
- `guides\AnalogForge_Hand_Work_Guide.md`
- `guides\AnalogForge_Replacements_And_Variables.md`
- `pdf\AnalogForge_Toolkit_Basic.pdf`
- `pdf\AnalogForge_Toolkit_Pro.pdf`
- `pdf\AnalogForge_Hand_Work_Guide.pdf`
- `pdf\AnalogForge_Replacements_And_Variables.pdf`

The four PDFs were also written to:

- `C:\Users\nbark\OneDrive\Desktop\AnalogForge_Toolkit_Basic.pdf`
- `C:\Users\nbark\OneDrive\Desktop\AnalogForge_Toolkit_Pro.pdf`
- `C:\Users\nbark\OneDrive\Desktop\AnalogForge_Hand_Work_Guide.pdf`
- `C:\Users\nbark\OneDrive\Desktop\AnalogForge_Replacements_And_Variables.pdf`

## New Guide Content

`AnalogForge_Hand_Work_Guide.md` adds a practical protocol for:

- start-to-finish exploration of novel or theoretical science;
- boundary collision handling;
- proof/obligation splitting;
- eight-neighbor checks around `C`;
- conservation and receipt rules.

`AnalogForge_Replacements_And_Variables.md` adds a substitution protocol for:

- replacing unavailable tools;
- preserving function before material;
- recording substitutions as receipts;
- low-cost, classroom, field, and lab kit variants.

## Exclusions

- generated demo exports;
- notebooks;
- pre-existing generated workbench PDFs outside this publication set;
- caches, bytecode, and virtual environments.

## Verification

- PDFs were generated with local `fpdf`;
- Markdown/source JSON parsed where applicable;
- package Python files were syntax-parse checked;
- PDF publication was admitted by a dedicated publication manifest.
