# Paper 21.25 - MorphForge Toolkit Supplement

## Purpose

This supplement describes the tools that may be used to reproduce Paper 21. It
is not the proof itself. The proof-carrying item is the lossless ribbon codec,
the morphonics ledger receipt, and the terminal landing check in Paper 21.

## Digital Route

Run the Paper 21 verifier:

`python production/formal-papers/CQE-paper-21/verify_morphforge_ribbon.py`

The expected result is `pass_with_open_obligations`. A valid run writes
`morphforge_ribbon_receipt.json` and reports:

- zero chart-codec round-trip mismatches,
- a 1569-state shell-2 ribbon,
- a 1568-step S3 word,
- 494 identity self-loops,
- 1074 non-identity fold steps,
- a morphonics ledger with five passing morphon closure tests,
- three explicit open failure labels,
- a 24-dimensional `Niemeier:E8^3` terminal landing template.

## Analog Route

To reproduce the idea by hand, draw a row of adjacent local windows. Mark each
window as left, center, and right. For each adjacent pair, record whether the
local ordering is unchanged or whether two positions exchange. Unchanged pairs
are identity self-loops. Exchanges are folds. The analog record is accepted only
when the reader can replay the marks and recover the same ribbon.

The analog route is useful because it exposes the base move: no hidden computer
feature is needed to understand the proof. A person can draw the ribbon, mark
the folds, and audit whether a later claim is adding information that was not in
the initial enumeration.

## Hidden-Guess Diagnostic

When training mode is enabled, every non-math validation should hide the
diagnostic label until after the agent or reviewer commits to a choice. Paper 21
uses these labels:

- closed ribbon,
- fold event,
- morphon schema closure,
- terminal template placement,
- open bridge,
- invalid promotion.

The answer key is revealed only after the choice. This keeps the diagnostic from
becoming a prompt-following exercise and turns each validation into a small
ablation.

## Boundaries

The toolkit does not prove cross-medium equivalence, material behavior,
biological behavior, CAD correctness, a Mandelbrot theorem, or a Leech lattice
construction. It supplies the reader and the audit trail those later claims must
use.
