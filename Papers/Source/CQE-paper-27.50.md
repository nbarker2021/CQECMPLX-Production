# Paper 27.50 - Observer Delay Claim Contract

## Purpose

This contract defines the minimum fields required before an observer-delay
claim can be promoted.

## Required Fields

Each observer row must provide depth, state `(L, C, R)`, reflected state
`(R, C, L)`, observer A center, observer B center, shared-center Boolean,
side-disagreement Boolean, anneal-delay steps, anneal final state,
four-frame label, static Z4 period, and emitted center bit.

Each temporal-period claim must provide the tested depth, candidate period,
label-trace result, center-column result, and first counterexample if the
claim fails.

## Promotion Rules

The following may be promoted:

- static Z4 template over eight chart states,
- shared `C` under LR reflection,
- bounded anneal delay in finite chart steps,
- temporal-period refutation over the tested trace,
- preservation of side disagreement as residue.

The following promotions are rejected:

- static Z4 label period to temporal Rule 30 period,
- anneal delay to human response time,
- shared `C` to physical simultaneity,
- frame selection to consciousness,
- frame selection to measurement collapse.

## Linked Review

Paper 27 inherits Paper 19's observer-face discipline and Paper 26's horizon
quarantine. It may export observer vocabulary only when the finite receipt and
interpretive boundary are kept together.
