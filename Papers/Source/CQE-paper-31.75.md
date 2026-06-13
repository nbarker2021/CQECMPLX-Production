# Paper 31.75 - Meta LCR Next-State Preconditions

## Purpose

This supplement defines what Paper 31 exports to Paper 32. It supplies a
readout discipline for packaging: the suite may be navigated as LCR, but every
claim must retain its own receipt and obligation status.

## Forward Exports

Paper 31 exports:

- center-invariance status,
- Rule 30 boundary table status,
- Paper 30 ribbon receipt link,
- dependency direction: readout-only,
- standing open obligations,
- Paper 32 as forward target.

## Application To Paper 32

Paper 32 may turn the suite into a deployable selector, supervisor cursor, or
kernel package. It must preserve which rows are proof rows, which rows are
readout metadata, and which rows are open obligations.

## Kernel Sidecar Rule

Training mode keeps the hidden-guess layer on when classifying readout rows.
Non-training mode may expose it as optional, but the final exported metadata
must still name the row status after classification.

## Failure Condition

The next state fails if a product, UI, API, or PDF bundle uses Paper 31's
retrospective language as proof support for a claim whose own verifier is
missing or open.
