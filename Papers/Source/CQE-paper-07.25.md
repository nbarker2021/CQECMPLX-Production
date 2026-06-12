# Paper 7.25 - Toolkit for the Discrete-Continuous Bridge

## Purpose

Paper 7.25 describes the tools for reviewing the discrete-continuous bridge.
These tools expose sample-preserving interpolation and receipt retention; they
do not prove between-sample dynamics.

## Review Objects

The toolkit works with:

```text
indexed trace       = [(0,x0), ..., (n,xn)]
bridge function     = piecewise-linear F
sample error        = abs(F(k)-xk)
endpoint agreement  = adjacent segments share samples
discrete receipt    = original proof or trace record
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json
```

Additional source and kernel files:

```text
production/papers/CQE-paper-07/SOURCE.md
production/papers/CQE-paper-07/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-07/02-CQE-tool/TOOL.md
production/papers/CQE-paper-07/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-07/PAPER_KERNEL.md
```

The kernel notes currently mark `production/papers/CQE-paper-07/02-CQE-tool/run.py`
as missing, so the promoted verifier is the replayable route for this paper.

## Analog Toolkit

A physical reconstruction requires:

- graph paper or any coordinate surface,
- a finite list of indexed values,
- a straightedge or equivalent mark,
- a receipt line.

Procedure:

```text
plot each indexed sample
connect adjacent samples with straight segments
check that every original sample remains on the line
write the sample error for each index
mark between-sample interpretation as unproven unless separately verified
keep the original discrete receipt beside the drawing
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What is the interpolation error at integer samples?
Do adjacent segments agree at shared endpoints?
Does sample preservation prove between-sample physics?
What must stay attached to the drawing?
```

Expected answers:

```text
zero
yes
no
the original discrete receipt
```

## Boundary

Paper 7.25 is a toolkit supplement. If a later trace claims physical dynamics
between samples, it must pass Paper 7.50's claim contract and attach an
additional theorem.
