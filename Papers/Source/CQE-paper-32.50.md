# Paper 32.50 - Supervisor Cursor Claim Contract

## Purpose

This contract defines when a supervisor-cursor statement is valid. It prevents
the schedule from becoming an untracked substitute for the proof receipts it
routes.

## Required Fields

Every cursor row must include:

- dimension `n`,
- schedule length,
- coverage status,
- minimality status,
- lower bound,
- upper row,
- corridor width,
- receipt path,
- routed paper or tool status.

Coverage and minimality are separate fields. A covered schedule is not
automatically minimal.

## Accepted Claims

The contract accepts validated coverage for `n=4..8`.

The contract accepts closed minimality for `n=4` and `n=5`.

The contract accepts `n=8` length `46205` as the Egan upper row.

The contract accepts the Paper 32 to Paper 01 suite wrap as an active-suite
retest route.

## Rejected Promotions

The contract rejects these promotions unless a future verifier supplies the
missing evidence:

- minimality for `n>=6`,
- cursor content replacing paper content,
- a selector hiding open obligations,
- a final-observation theorem without its own proof row,
- a schedule row counted as proof for a routed paper.

## Hidden-Guess Ablation

Diagnostics must classify rows before revealing the answer. Valid labels are
coverage row, minimality row, bounds row, open corridor, selector row, and
invalid proof substitution.
