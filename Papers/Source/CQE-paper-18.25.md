# Paper 18.25 - VOA / Moonshine Route Toolkit

## Purpose

This supplement exposes the Paper 18 route checks. It is a reviewer tool, not
the proof itself.

## Digital Route

Run:

```text
python production/formal-papers/CQE-paper-18/verify_voa_moonshine_routes.py
```

The receipt must include:

```text
finite VOA seed
Z4 route template
Monster scalar
bounded McKay matrix bootstrap
lookup-harness deferred status
correction_via_voa open status
Monster-D4 lift bounded/open-gap status
```

## Analog Route

Lay eight state cards. Mark two weight-0 cards and six weight-5 cards. Then
add a four-frame route strip:

```text
C frame
R frame
C-flipped frame
L frame
```

The two fixed cards remain white. The six period-4 cards move through the
route strip. The Monster/McKay card is marked as bounded table evidence unless
the full correction route has been supplied.

## Hidden-Guess Diagnostic

Before revealing the receipt, classify each route as:

```text
closed finite seed
closed static route template
bounded table evidence
bounded open-gap route
open global route
invalid promotion
```

Reveal the receipt only after the choice is made.

## Boundary

This toolkit may show the finite VOA seed and bounded McKay bootstrap. It may
not show `correction_via_voa` as complete, and it may not turn bounded tables
into a full Moonshine proof.

## Conclusion

Paper 18.25 makes the route visible without moving the proof boundary.
