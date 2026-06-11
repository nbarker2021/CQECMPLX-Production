# MORSR Pulse Protocol

Canonical name: Middle-Out Resonance and Shape Reader.

## Core Loop

```text
input: C centroid

for recenter_index in 0..2:
    emit 240-direction E8 pulse from current centroid
    collect all instant active nodes
    run hidden guess result diagnostic if action is non-math
    confirm one reading
    set confirmed reading as pode/node
    recenter on confirmed reading

output: quadratically confirmed extension of the first centroid
```

## Terms

- `C centroid`: the middle-origin coordinate or conceptual center being diagnosed.
- `240-direction pulse`: one pulse across the 240 E8 root directions.
- `instant active node`: any node that lights up or responds within the pulse envelope.
- `confirmed reading`: a node response that survives the active-node diagnostic and reveal step.
- `pode/node`: the placed reading that becomes the next recentering anchor.
- `quadratically confirmed extension`: the three-step recentered map grown from the original centroid.

## Diagnostic Output

Every pulse cycle must emit:

- seed centroid id
- pulse id
- active node set
- hidden guess record ids
- confirmation result
- selected pode/node
- recenter vector
- shadow/unhit directions
- confidence and failure-mode labels
- receipt hash or trace id

## Acceptance

A reading is accepted only if:

- it is reachable from the pulse envelope
- it has a diagnostic trace
- the hidden guess phase happened before reveal for non-math decisions
- the reveal/scoring phase records hit, miss, or partial
- the recenter step is reproducible from the trace
