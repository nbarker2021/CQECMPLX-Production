# Paper 32.75 - Supervisor Cursor Next-State Preconditions

## Purpose

This supplement defines how Paper 32 exports into deployment. The kernel may
use the supervisor cursor to schedule requests, but every scheduled request
must carry its own proof/open/readout status.

## Forward Exports

Paper 32 exports:

- coverage receipts for `n=4..8`,
- minimality scope: closed only for `n=4` and `n=5`,
- n=8 bounds row: lower `46085`, upper `46205`, corridor `120`,
- supervisor cursor as request schedule,
- paper-kernel selector wrap from Paper 32 to Paper 01,
- obligation that selectors preserve status.

## Deployment Rule

A UI, API, NotebookLM pack, sidecar kernel, or paper-kernel runner may call the
cursor to choose an order. It must then show the selected item with its own
receipt status. Cursor success is not item proof.

## Kernel Sidecar Rule

Training mode keeps hidden-guess classification on for schedule rows and
selector rows. Non-training mode may make it optional, but exported receipts
must still reveal the final answer key after classification.

## Failure Condition

Deployment fails if the cursor routes a paper, package, or product while
dropping whether that item is proven, open, readout-only, or rejected.
