# Paper 27.25 - Observer Delay Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 27's observer-frame receipt. The
proof is in Paper 27 and its formal verifier; human observer interpretations
remain obligations.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-27/verify_observer_delay_shared_reality.py`

The expected status is `pass_with_interpretive_obligations`. The verifier
checks the static Z4 template, the temporal-period refutation, the shared `C`
invariant, bounded anneal delay, and the non-promotion of consciousness,
collapse, simultaneity, and human-latency claims.

## Analog Route

Draw a three-cell strip `L | C | R`. Put one observer token at the left
boundary and one at the right boundary. Both read toward the center. Swap
`L` and `R` to simulate the opposite-boundary observer, then verify that the
center bead remains unchanged.

Use four cards for the static Z4 frames. Rotate the cards to compute the
four-frame label. Do not use the wheel to predict time. Mark any failed
temporal prediction as a black follow-up row.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- static Z4 frame fact,
- temporal Z4 overclaim,
- shared center fact,
- boundary-side residue,
- bounded anneal delay,
- invalid consciousness promotion,
- invalid measurement-collapse promotion.

The answer key distinguishes finite chart receipt from observer
interpretation.
