# Paper 24.50 - KnightForge Claim Contract

## Admission Rule

A Paper 24 claim is admitted only when it is framed as a finite local-rule
automaton or a frame operator unless a stronger game-theoretic proof is attached.
The receipt must preserve occupied rows, rejected rows, local states, anneal
trajectories, sector labels, and open obligations.

## Required Fields

Each admitted board row must provide:

- board size or lattice domain,
- sweep order,
- cell identifier,
- `L`, `C`, and `R` bits,
- occupancy or rejection decision,
- attack/exclusion evidence,
- side label,
- L-conjugate attractor,
- anneal step count,
- frame label or reason absent,
- closure status.

## Rejected Promotions

The following promotions are not allowed:

- finite greedy placement to solved chess,
- frame operator to playable N-dimensional game,
- board sequence to OEIS identity without search evidence,
- chart sector split to complete placement-class theorem,
- analog token-board closure to game-theoretic proof.

## Falsifiers

The claim fails if an occupied pair attacks, if a row cannot replay its local
state, if any row fails L-conjugate closure within three steps, if the `2 + 6`
sector verifier fails, or if a claimed sequence identity is not reproduced by
the finite sweep.

## Carry Rule

Later game-lattice papers may import the local-rule receipt and frame operator.
They inherit the open playability and sequence-identity obligations until their
own receipts close them.
