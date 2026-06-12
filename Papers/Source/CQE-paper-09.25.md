# Paper 9.25 - Toolkit for Hamiltonian Window Emergence

## Purpose

Paper 9.25 describes the tools for reviewing Hamiltonian window emergence.
These tools expose window counts, provenance preservation, and reverse receipt
checks. They do not prove physical time reversal.

## Review Objects

The toolkit works with:

```text
center state       = (paper_id, center)
window width       = 3, 5, or 7
window slice       = contiguous center-state segment
forward receipt    = centers in source order
backward receipt   = centers in reverse order
composite center   = ordered join of source centers
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-09/verify_hamiltonian_window_emergence.py
production/formal-papers/CQE-paper-09/hamiltonian_window_emergence_receipt.json
```

Additional source and kernel files:

```text
production/papers/CQE-paper-09/SOURCE.md
production/papers/CQE-paper-09/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-09/02-CQE-tool/TOOL.md
production/papers/CQE-paper-09/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-09/PAPER_KERNEL.md
```

The kernel notes currently mark `production/papers/CQE-paper-09/02-CQE-tool/run.py`
as missing, so the promoted verifier is the replayable route for this paper.

## Analog Toolkit

A physical reconstruction requires:

- center cards,
- ordered slots,
- a window frame of width 3, 5, or 7,
- receipt rows.

Procedure:

```text
place center cards in order
choose an odd window width
slide the window across all valid starts
record the forward center sequence
record the backward center sequence
reverse the backward receipt and compare it to the forward receipt
write the composite center from the source centers
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
How many width-3 windows exist over six centers?
How many width-5 windows exist over seven centers?
Does a reverse receipt prove physical time reversal?
Can a composite center be valid without source provenance?
```

Expected answers:

```text
4
3
no
no
```

## Boundary

Paper 9.25 is a toolkit supplement. Any physical time, periodicity, or
Hamiltonian dynamics claim must pass Paper 9.50's claim contract before it can
change the scientific paper.
