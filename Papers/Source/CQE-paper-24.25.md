# Paper 24.25 - KnightForge Toolkit Supplement

## Purpose

This supplement shows how to reproduce the KnightForge receipt. The proof is in
Paper 24 and its formal verifier; this file holds the tool and analog handling.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-24/verify_knightforge_ca.py`

The expected status is `pass_with_open_obligations`. The verifier checks
centroid annealing, the `2 + 6` sector split, finite greedy knight placement,
per-row L-conjugate closure, and the N-dimensional frame-operator boundary.

## Analog Route

Draw a numbered board. Sweep cells in order. At each cell, mark the two opposed
knight-approach families as `L` and `R`; mark `C = 1` if the cell is occupied
and `C = 0` if the cell is rejected. Draw the anneal route by swapping the three
positions until `L = R`. The analog row passes if the same attractor and step
count are recovered.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- occupied row,
- rejected row,
- attacking invalid row,
- L-conjugate closure,
- sector split,
- frame operator,
- invalid solved-game promotion.

The answer key distinguishes local CA closure from game-theoretic closure.
