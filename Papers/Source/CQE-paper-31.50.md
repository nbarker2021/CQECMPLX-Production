# Paper 31.50 - Meta LCR Claim Contract

## Purpose

This contract defines valid uses of Paper 31. It lets the corpus describe
itself as LCR while preventing the meta-description from becoming a proof
shortcut.

## Required Fields

Every Paper 31 claim row must include:

- readout object,
- left boundary,
- center,
- right boundary,
- boundary rule,
- receipt path,
- dependency direction,
- open-obligation status.

Dependency direction is mandatory. A row that uses Paper 31 as a premise for
papers 00-30 fails this contract.

## Accepted Claims

The contract accepts that `C` is the LR-invariant gluon coordinate.

The contract accepts the Rule 30 truth table as the local boundary readout.

The contract accepts Paper 31 as a retrospective readout of Paper 30's ribbon.

The contract accepts Paper 32 as the next packaging/deployment target.

## Rejected Promotions

The contract rejects these promotions unless a future verifier changes the
evidence:

- Paper 31 proves earlier papers,
- a meta-reading closes standing obligations,
- Paper 31 replaces Paper 32,
- the readout is treated as a new physical theorem,
- open obligations are hidden in the walkthrough.

## Hidden-Guess Ablation

Diagnostics must ask the reviewer to classify a row before revealing the
answer. Valid labels are invariant center, boundary table, readout-only row,
open obligation, invalid dependency, and forward package target.
