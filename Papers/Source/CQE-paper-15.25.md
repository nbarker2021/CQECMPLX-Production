# Paper 15.25 - Toolkit for Mass-Residue Carrier

## Purpose

This support paper exposes the tools for Paper 15. It does not prove the Higgs
mechanism. It shows how to inspect the finite substrate residue carrier.

## Digital Route

Run:

```text
python production/formal-papers/CQE-paper-15/verify_mass_residue_carrier.py
```

The verifier checks:

```text
Rule 30 split
F2 Arf invariant
Arf gluing/rejection
VOA weight distribution
correction residue states
nth-bit local/oracle layer with McKay-Thompson parity still open
```

## Analog Route

Write the local state as three marks:

```text
L C R
```

Cancel the linear part:

```text
L xor C xor R
```

The obstruction token is:

```text
C and R
```

The correction residue token is:

```text
C and not R
```

Color the state by VOA weight:

```text
0 = vacuum
5 = excited carrier
```

## Hidden-Guess Diagnostic

Before revealing the receipt, ask:

```text
Does the state carry correction residue?
Is its VOA weight 0 or 5?
Does its Arf class glue or reject?
Is the claim substrate-level or physical-Higgs-level?
```

Reveal the receipt only after the guess is recorded.

## Boundary

This toolkit can prove the local residue carrier. It cannot turn that carrier
into a measured particle mass without another proof.
