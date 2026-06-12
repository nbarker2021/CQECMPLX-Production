# Paper 14.25 - Toolkit for Boundary-Repair Curvature

## Purpose

This support paper exposes the tools for Paper 14. The proof is the repair
ledger in Paper 14. The toolkit shows how to reproduce and inspect it.

## Digital Route

Run:

```text
python production/formal-papers/CQE-paper-14/verify_boundary_repair_curvature.py
```

The verifier checks:

```text
typed transport obligations
proof-boundary presence
zero repair for demonstrated rows
positive repair for open lifts
exact Paper 13 zero-repair reference
Cayley-Dickson/Oloid 1,8,8,1 normal form
dual-path oloid three-dyad coherence
```

## Analog Route

Draw a route as a line. If it closes with no adjustment, mark repair score `0`.
If it requires a named adjustment, write the adjustment as an obligation card.

Use the scoring ladder:

```text
demonstrated = 0
bounded_local = 1
bounded_external = 2
registered_landing_forms = 3
open = 4
```

The analog curved carrier is a folded or rolling strip with three possible
dyads: podal, antipodal, and shared.

## Hidden-Guess Diagnostic

Before revealing the receipt, ask:

```text
Is this row demonstrated, bounded, registered, or open?
Does it score zero repair or positive repair?
Is the claim substrate-level or physical-GR-level?
```

Then reveal the ledger row. The important training signal is whether the
evaluator distinguishes closed repair accounting from physical curvature.

## Boundary

This toolkit proves no Riemann, Ricci, Einstein, or measured gravitational
claim. It exposes the repair ledger that a later physics interpretation must
calibrate.
