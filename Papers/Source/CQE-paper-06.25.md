# Paper 6.25 - Toolkit for Causal Code

## Purpose

Paper 6.25 describes the review tools for causal code. These tools expose the
typed dependency graph and its falsifiers; they do not declare the full
32-paper graph complete.

## Review Objects

The toolkit works with:

```text
vertex      = paper, proof, tool, receipt, obligation, package, product
edge        = source, target, edge_type, receipt, status
closed graph = closed proof-support edges only
open edge   = tracked obligation
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-06/verify_causal_code.py
production/formal-papers/CQE-paper-06/causal_code_receipt.json
```

Additional source and kernel files:

```text
production/papers/CQE-paper-06/SOURCE.md
production/papers/CQE-paper-06/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-06/02-CQE-tool/TOOL.md
production/papers/CQE-paper-06/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-06/PAPER_KERNEL.md
```

The promoted verifier is the authority for Paper 6's closed claim. The kernel
notes currently mark `production/papers/CQE-paper-06/02-CQE-tool/run.py` as
missing, so the promoted verifier path is the replayable route for now.

## Analog Toolkit

A physical reconstruction requires:

- one card per paper/tool/receipt,
- one arrow per dependency,
- allowed edge-type labels,
- status labels,
- receipt labels.

Procedure:

```text
write each dependency as an arrow
label source and target
label the edge type
attach the receipt id
mark status
trace only closed proof-support arrows
reject hidden cycles
leave open obligations open
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What fields are required on a causal edge?
Can an open obligation be counted as proof?
Can closed proof support contain a hidden cycle?
Which edge carries Paper 5 into Paper 6?
```

Expected answers:

```text
source, target, edge_type, receipt, status
no
no
CQE-paper-05 -> CQE-paper-06, transports
```

## Boundary

Paper 6.25 is a toolkit supplement. If new edge types, statuses, or receipt
rules are added, they must pass Paper 6.50's claim contract before changing
the scientific paper.
