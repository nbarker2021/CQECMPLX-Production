# Paper 30.50 - Grand Ribbon Claim Contract

## Purpose

This contract defines when a corpus-level ribbon statement is valid. It keeps
the meta-framer from turning into an untracked proof shortcut.

## Required Fields

Every ribbon row must include:

- paper id,
- slot name,
- slot value,
- provenance,
- source kind,
- proof status,
- obligation status when applicable.

A row is closed only when slot value and provenance are both present. A missing
provenance field is not a small formatting issue; it is an unfilled slot.

## Accepted Claims

The contract accepts that papers 00-29 can be represented as a 30-position
eight-slot sweep.

The contract accepts that `build_terminal_composition_tree` supplies a
canonical terminal route for the tested seed/terminal pair.

The contract accepts `pass_with_open_lifts` as a valid transport-ledger state
because open lifts are preserved as boundary data.

The contract accepts Paper 31 as a later readout of the sweep.

## Rejected Promotions

The contract rejects these promotions unless a new verifier changes the
evidence:

- the ribbon framing is a new mathematical theorem,
- Paper 31 is required as a premise for papers 00-29,
- all transport lifts are treated as closed,
- a slot without provenance is counted as filled,
- legacy 31-bead workbook language is used without marking Paper 31 as readout,
- a product selector hides open obligations.

## Hidden-Guess Ablation

Diagnostics must ask the reviewer to classify a row before revealing the
answer. The valid labels are closed slot, open slot, open lift, valid readout,
and invalid dependency. The answer key appears only after the choice.
