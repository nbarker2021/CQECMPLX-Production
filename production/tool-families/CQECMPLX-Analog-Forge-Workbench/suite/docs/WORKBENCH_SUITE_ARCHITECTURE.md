# Workbench Suite Architecture

## Layers

1. Physical kit definition - colors, tools, copies, roles.
2. Operator modules - dice, cards, strings, binding.
3. Receipt modules - proof/obligation records.
4. Simulation module - one action loop.
5. PDF reports - manual, printable sheets, demo report.
6. Notebook scaffold - human-readable demo notebook.

## Result policy

Every operation that yields a result should emit either:

- a JSON receipt,
- a printable workbook sheet,
- a PDF report,
- or a small Python object/module that can be imported and tested.
