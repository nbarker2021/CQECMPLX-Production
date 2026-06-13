# Paper 24 - KnightForge / N-Dimensional Chess Automata

## Abstract

Paper 24 registers greedy non-attacking knight placement as a local-rule
cellular-automaton receipt whose states close under the L-conjugate centroid
structure. The chessboard is the concrete shadow of the proof. The proof itself
is the finite chart result: all `(L, C, R)` states anneal to one of four `L = R`
attractors in at most three S3 transposition steps, and the same chart states
split into the `2 + 6` VOA sector pattern.

The paper does not solve chess, N-dimensional chess, or any named OEIS sequence.
It proves the CA receipt and the frame-operator lift. Playability, sequence
identity, and full combinatorial-game meaning remain obligations.

## Closed Evidence

The verifier calls the promoted `centroid_voa.py` substrate. The Hamming
centroid verifier passes, giving four L-conjugate attractors:
`(0,0,0)`, `(0,1,0)`, `(1,0,1)`, and `(1,1,1)`. Every chart state closes to
that plane in at most three steps. The sector verifier passes with partition
`Z(q) = 2q^0 + 6q^5`, two weight-zero vacua and six weight-five excited states.
The centroid chain verifier also passes with two fixed points and six period-4
states.

The local greedy-knight verifier sweeps an 8 by 8 board in numbered
boustrophedon order. At each cell it records the opposed knight-approach bits
`L` and `R`, the occupancy decision `C`, the side label `R - L`, the
L-conjugate attractor, the anneal step count, the three-conjugate frame label,
and the VOA weight. The finite board receipt is deterministic, has occupied and
rejected rows, has no attacking occupied pairs, and every row closes to an
L-conjugate in at most three steps.

## Definitions

A placement state is a local triple `(L, C, R)`. `C` is the current cell's
occupancy decision. `L` and `R` are opposed approach bits determined by whether
earlier placed knights attack the current cell from the left-approach or
right-approach L-move families. A rejection is a data row, not a deletion.

An L-conjugate state is a state with `L = R`. A frame operator is a tuple of
three-conjugate labels assigned to board axes or move axes. It is an operator
definition, not a proof of a complete game.

## Claims

1. The L-conjugate attractor structure closes.

The centroid substrate proves that all eight chart states reach the four
`L = R` attractors in at most three S3 transposition steps.

2. The chart sectors split as `2 + 6`.

The VOA sector verifier returns `Z(q) = 2q^0 + 6q^5`: two true vacua and six
excited states.

3. A finite greedy knight board can be represented as a local-rule CA receipt.

The verifier sweeps a finite numbered board, emits one row per cell, records
occupied and rejected decisions, and verifies that the occupied set is
non-attacking.

4. The board receipt inherits L-conjugate closure.

Every emitted row carries an `(L, C, R)` state and an annealing receipt. The
maximum step count is at most three.

5. The N-dimensional lift is a frame operator.

The verifier constructs a finite frame-operator row for four axes. It does not
claim that this row is a playable, terminating, or strategically meaningful
N-dimensional chess game.

## Theorem 24

KnightForge is a valid CQE board-automata kernel when it returns a replayable
finite placement receipt whose local states close under L-conjugate centroid
annealing and whose N-dimensional extension is explicitly labeled as a frame
operator rather than a solved game.

## Proof

Run `verify_knightforge_ca.py`. The first three checks verify the substrate:
the L-conjugate closure, the `2 + 6` sector split, and the centroid chain. These
checks prove the chart structure used by the board receipt.

The fourth check constructs the finite greedy knight board. The receipt is
accepted only if the sweep covers all board cells, produces both occupied and
rejected rows, and leaves no occupied pair connected by a knight attack. This
establishes the local-rule CA shadow of the chess example.

The fifth check applies the centroid closure to every board row. A failed
anneal, or a row requiring more than three steps, would falsify the claim that
the board receipt is carried by the L-conjugate chart structure.

The final check builds the N-dimensional frame operator and verifies that it is
not represented as a closed game claim. Thus the paper proves the finite CA and
frame-lift receipt while carrying the game-theoretic obligations.

## Receipt

The formal receipt is generated at:

`production/formal-papers/CQE-paper-24/knightforge_ca_receipt.json`

## Open Obligations

OEIS identity remains open. N-dimensional playability remains open. The
placement-class relation to the `2 + 6` sector split remains open beyond the
local chart receipt. Combinatorial-game expert review remains open.

## Suite Role

Paper 23 supplies the chain/path descriptor discipline. Paper 24 applies that
discipline to board automata. Paper 25 may reuse the board receipt as a
move-cost or traversal ledger, while Paper 28 may develop broader game lattices.
