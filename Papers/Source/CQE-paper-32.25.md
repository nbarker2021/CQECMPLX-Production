# Paper 32.25 - Supervisor Cursor Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 32's supervisor-cursor receipt.
The proof is in Paper 32 and its formal verifier. The cursor schedules
requests; it does not replace the proof receipts attached to the requested
items.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-32/verify_supervisor_cursor_schedule.py`

The expected status is `pass_with_open_minimality_obligations`. The verifier
checks coverage for `n=4..8`, the recursive `n=8` chart walk, the Egan upper
row, the n=8 open corridor, the n=5 octad orbit, and the paper-kernel selector
wrap.

## Analog Route

Write the schedule string on a strip. Slide a length-`n` window across it. Each
window is one requested ordering. Mark a permutation as covered only when the
window contains every symbol exactly once.

Use white marks for covered orderings. Use black marks for unclosed
minimality corridors. For `n=8`, write the corridor as:

```text
46205 - 46085 = 120
```

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- covered permutation row,
- missing permutation row,
- closed minimality row,
- validated schedule without minimality,
- open corridor,
- invalid hidden proof support,
- valid suite selector.

The answer key distinguishes schedule coverage from minimality.
