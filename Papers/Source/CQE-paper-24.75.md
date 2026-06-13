# Paper 24.75 - KnightForge Next-State Bridge

## Bridge Role

Paper 24 exports a local-rule board automaton. The next state receives a way to
turn board moves into replayable `(L, C, R)` rows with closure receipts. It does
not receive solved games.

## Exported Artifacts

The next state receives:

- finite board sweep order,
- local exclusion rows,
- occupied/rejected row accounting,
- L-conjugate anneal receipts,
- `2 + 6` sector labels,
- N-dimensional frame-operator boundary,
- invalid-promotion labels.

## Use in Paper 25

Paper 25 may treat occupied moves, rejected moves, and frame labels as traversal
cost rows. It must still prove its own energy or action ledger.

## Use in Paper 28

Paper 28 may extend the board-local rule to broader game lattices. It must
separate finite reachability proof from general game solvability.

## Boundary

Paper 24 exports board-automata closure. It does not export chess closure,
strategic optimality, OEIS identity, or N-dimensional playability.
