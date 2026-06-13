# Paper 28.75 - N-Dimensional Game Lattice Next-State Precondition

## Purpose

This supplement defines what Paper 28 exports to later applied tools.

## Exported Preconditions

Downstream tools may use:

- admissible-dimension check,
- local `(L, C, R)` move row,
- S3 move-orbit enumeration,
- Rule 30 emitted bit,
- forbidden carrier ledger,
- centroid closure status,
- explicit refusal of general game-solver promotion.

## Downstream Use

CADForge, robot planners, board-game prototypes, and constraint-search tools
may use this receipt shape as a local legal-move kernel. They must add their
own domain geometry and strategy verifiers before claiming solved behavior.

## Kernel Handshake

The kernel sidecar should expose Paper 28 as a game-lattice adapter: receive a
dimension and chart state, reject non-admissible dimensions unless separately
proved, emit S3 orbit rows, log forbidden carriers, and return closure status.
In training mode, the guess label stays hidden until the reviewer predicts
whether the row is a legal move, forbidden carrier, dimension error, or
overclaim.
