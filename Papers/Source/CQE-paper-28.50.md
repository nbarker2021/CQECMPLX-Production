# Paper 28.50 - N-Dimensional Game Lattice Claim Contract

## Purpose

This contract defines the minimum fields required before a game-lattice claim
can be promoted.

## Required Fields

Each game row must provide game id, dimension, dimension-admissible Boolean,
source state, S3 permutation, target state, emitted bit, anneal steps, anneal
final state, carrier status, and closure status.

Each board claim must provide the dimension verifier used. For dimension 8,
the receipt must include extended Hamming codeword count, minimum weight, and
weight distribution.

## Promotion Rules

The following may be promoted:

- forced code-tower dimension membership,
- dimension-8 extended Hamming board,
- finite S3 trace-2 move orbit,
- Rule 30 local emission,
- forbidden carrier logging,
- <=3-step centroid closure.

The following promotions are rejected:

- finite move orbit to complete game solver,
- admissible dimension to arbitrary dimension,
- legal move receipt to strategy proof,
- robot example to all board games,
- trace-2 orbit to every real piece type without a piece map.

## Linked Review

Paper 28 inherits Paper 24's board-automata discipline and Paper 27's
observer/turn-delay guard. It may export local-rule game receipts only when
open game-theory obligations remain visible.
