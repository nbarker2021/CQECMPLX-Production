# ForgeFactory Analog Workbench Suite v0.1

This package turns the by-hand analog workbook kit into a literal Python and PDF workbench suite.

The suite has two jobs:

1. Define the physical kit in a way that can be printed, assembled, and used by hand.
2. Provide a Python simulation layer that records the same actions digitally as receipts, workbook sheets, and reports.

Core rule:

```text
observed action -> loose grey substrate -> three-color gradient -> yes/no continuation -> proof or obligation -> receipt -> bound page or open obligation
```

Install locally:

```bash
python -m pip install -e .
analog-workbench kit --out exports/kit_manifest.json
analog-workbench demo --out exports/demo_run
analog-workbench pdf --out exports/pdfs
```

No raw user source ZIPs are included. This is a standalone package derived from the session's analog workbook definition.
