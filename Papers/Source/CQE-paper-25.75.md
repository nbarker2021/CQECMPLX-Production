# Paper 25.75 - Energetic Traversal Next-State Precondition

## Purpose

This supplement defines what Paper 25 exports to the next state of the suite.
It is a precondition layer, not a new proof claim.

## Exported Preconditions

Any downstream paper that uses traversal cost must inherit:

- one NSL row per step,
- additive `theta_path`,
- explicit unit policy,
- obligation carry for positive or uncalibrated rows,
- default VOA analog cost when the row is still at chart-state level,
- refusal to promote analog accounting to physical energy without calibration.

## Downstream Use

Paper 26 and later horizon papers may use the energetic traversal ledger to
compare routes, detect boundary collisions, and decide where a new verifier
must attach. They must not treat the ledger as a replacement for the domain's
own metric or measurement.

## Kernel Handshake

The kernel sidecar should expose Paper 25 as a boundary adapter: receive a
transport row, compute `theta`, return closure or obligation, and preserve the
unit policy. In training mode, the guess label stays hidden until after the
agent or reviewer predicts whether the row closes.
