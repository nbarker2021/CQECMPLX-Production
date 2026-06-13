# Paper 29.50 - Monster Horizon Claim Contract

## Purpose

This contract defines when a Monster or energy-bound statement may be cited
after Paper 29. It is a boundary-failure detector: it catches language that
quietly turns an arithmetic row into a physical theorem.

## Required Fields

Every claim row must include:

- row id,
- expression or source function,
- computed value,
- verifier path,
- claim scope,
- physical claim flag,
- witness-function status,
- falsifier,
- receipt path.

The physical claim flag must remain false unless the row supplies a
units-bearing transport theorem or another explicit witness appropriate to the
claim.

## Accepted Rows

`47*59*71 = 196883` is accepted as integer arithmetic.

`196884 = 1 + 196883` is accepted as integer decomposition.

`Z(q) = 2q^0 + 6q^5` is accepted as the finite eight-state VOA partition.

`voa_weight` is accepted as a finite-chart energy analog or wrap-step count.

## Rejected Promotions

The contract rejects these promotions unless a new verifier closes the missing
witness:

- `voa_weight` becomes joules,
- weight 5 becomes a measured excitation gap,
- `196883` becomes a universal energy ceiling,
- `196883` becomes a universal state-count ceiling,
- `196884 = 1 + 196883` becomes a new Moonshine proof,
- Pariah/Happy-Family closure becomes a physical boundary law,
- finite Monster arithmetic becomes a complete Standard Model extension.

## Linked Review Rule

When a later paper cites Paper 29, it must cite either a closed row or an open
hypothesis row by name. A citation that uses "Monster bound" without saying
which row is closed and which row is open fails this contract.

## Hidden-Guess Ablation

Diagnostics must present candidate statements before revealing their status.
The reviewer or agent chooses closed proof row, valid analog, or open
hypothesis. Only after that choice does the receipt expose the answer key. This
keeps the honesty layer active during every non-math validation step.
