# Paper 28.25 - N-Dimensional Game Lattice Toolkit Supplement

## Purpose

This supplement shows how to reproduce Paper 28's local-rule game-lattice
receipt. The proof is in Paper 28 and its formal verifier; full game solving
is not claimed.

## Digital Route

Run:

`python production/formal-papers/CQE-paper-28/verify_nd_game_lattices.py`

The expected status is `pass_with_open_obligations`. The verifier checks the
forced code-tower dimensions, dimension-8 extended Hamming board, S3 move
orbit, Rule 30 local emissions, forbidden carrier logging, and centroid
annealing closure.

## Analog Route

Draw an 8-cell board. Place a robot token at the active chart state `(1,0,1)`.
Write the six S3 move cards beside the board. For each card, permute the active
trace-2 state, write the target, compute the emitted bit, and draw the anneal
route to a Lie-conjugate attractor.

Mark the identity carrier as forbidden with a black bar. Do not erase it; it is
part of the receipt.

## Hidden-Guess Diagnostic

Training mode should hide the label until after the reviewer chooses one:

- admissible code-tower dimension,
- non-admissible dimension,
- legal S3 orbit move,
- forbidden carrier,
- closed anneal row,
- invalid general game-solver promotion,
- invalid real-game strategy promotion.

The answer key distinguishes finite move receipts from solved games.
