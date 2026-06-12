# Workspace Aggregation and Cleanup Plan

## Purpose

The D: drive contains scattered work that may hold paper, proof, tool, kernel,
receipt, archive, or obligation value. Cleanup must not discard work before
that value is extracted.

This plan governs the review.

## Rule

No item is deleted, minimized, or treated as duplicate until it has passed
through:

```text
inventory -> classify -> extract -> promote/archive -> receipt
```

## Classification

Each discovered item is classified as one or more of:

- review paper content,
- quarter-paper supplement content,
- proof or theorem evidence,
- executable verifier,
- receipt or ledger,
- lib/forge/kernel binding,
- analog or workbook guide,
- source citation or prior-art anchor,
- duplicate/composite candidate,
- archive-only historical record,
- open obligation.

Duplicates are not removed at first pass. If two items say the same thing,
they are combined into a composite form and the originals remain traceable
until the composite is receipted.

## Promotion Targets

Review-facing paper material goes to:

```text
Papers/Source/
Papers/PDF/
```

Evidence and machinery go to:

```text
production/
tracking/
proofing/
reviews/
```

Historical or superseded material goes to an archive record, not an
untracked deletion.

## Paper Rewrite Rule

Each integer paper must be rewritten as a proper scientific paper:

```text
abstract
claims
predictions
test protocol
generated proof or receipt
formalization
falsifiers
results
references
evidence bindings
```

Toolkits, analog methods, kernels, lib-forge data, and narrative reader aids
belong in the `.25`, `.50`, and `.75` companion papers unless the integer
paper's claim is itself about a tool.

## Current Initial State

The visible review package must cover:

```text
Paper 0
Paper 0.25
Paper 0.50
Paper 0.75
Papers 1-32
```

Current production bodies may be used as fallback PDFs only so the whole suite
is visible. They are not final. Next work is to rewrite Paper 1 into the new
strict scientific form, then add Paper 1.25, Paper 1.50, and Paper 1.75 as
companion supports before moving to Paper 2, repeating this for every paper.
