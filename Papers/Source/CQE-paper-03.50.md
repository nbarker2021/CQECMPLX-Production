# Paper 3.50 - Triality Surface Claim Contract

## Purpose

Paper 3.50 defines what counts as a valid claim about the Paper 3 registration
surface. It preserves the useful local theorem while preventing stronger
triality language from being silently counted as proved.

## Admitted Paper 3 Claims

The following claims are admitted from Paper 3:

```text
the eight LCR states have a bijective axis/sheet encoding
axis pairs are antipodal complement pairs
diag(L,C,R) preserves shell as trace
shell-2 states are trace-2 diagonal idempotents
Paper 2 correction coordinates are preserved as (2,0) and (3,1)
```

## Claim Requirements

Any later paper using Paper 3 must state:

```text
which LCR state or state set is being registered
which coordinate language is being used
whether the import is LCR, axis/sheet, diagonal trace, or idempotent
which receipt proves the imported row
whether any stronger D4/F4/J3(O) claim is proved separately
```

## Linked Receipt

The minimum receipt link for Paper 3 is:

```text
paper: CQE-paper-03
theorem: Local D4/J3 triality surface
receipt: production/formal-papers/CQE-paper-03/triality_surface_receipt.json
status: pass
```

The receipt is sufficient for finite registration. It is not sufficient by
itself for full D4 triality, full F4 action, or full exceptional Jordan
algebra dynamics.

## Boundary Failures

The following are boundary failures:

```text
using triality language without naming the finite registration actually proved
claiming Paper 3 proves full D4 triality
using off-diagonal octonionic claims without a separate receipt
changing the axis/sheet chart without rerunning the verifier
using Paper 2 correction rows without preserving their coordinates
```

Boundary failures become obligations for later group-action, repair, or
causal-code papers.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted coordinate or scope status
revealed receipt
match/mismatch
next obligation if mismatch
```

The "does this prove full D4 triality?" prompt is required because the correct
answer is negative. That negative result is part of the honesty layer.

## Conclusion

Paper 3.50 lets later papers import the triality surface honestly. It keeps
the finite object-registration theorem strong while making the unclosed
exceptional-algebra extensions visible as separate obligations.
