# Paper 2.75 - Correction Surface as Next-State Precondition

## Purpose

Paper 2.75 explains how Paper 2 becomes a controlled precondition for Papers 3
and 4.

## Exported State

Paper 2 exports:

```text
the LCR carrier from Paper 1
the Rule30 / Rule90 comparison
the correction term C and not R
the firing states (0,1,0) and (1,1,0)
the D4 coordinates (2,0) and (3,1)
the rule that residue is obligation, not proof
```

## Use in Paper 3

Paper 3 may use the two firing states as registered chart entries only if it
preserves:

```text
the original LCR state
the correction value
the D4 axis/sheet coordinate
the receipt that proves the row
```

Paper 3 may prove stronger registration results, but those results must be
proved there. Paper 2 exports coordinates; it does not prove the whole
triality surface.

## Use in Paper 4

Paper 4 may treat the nonzero correction rows as boundary repair inputs. It
may not erase the fact that the rows began as failed-route residue.

The allowed transition is:

```text
correction residue -> typed repair constraint
```

The disallowed transition is:

```text
correction residue -> closed proof without repair
```

## Use in Later Papers

Later papers may lift the correction surface into:

- triality/Jordan registration,
- boundary repair,
- rolling path payloads,
- causal graph receipts,
- sampling and interpolation surfaces,
- Hamiltonian or mass-residue carriers.

Every lift must name which additional theorem closes the new structure.

## Precondition Rule

Before a later paper uses Paper 2, it should be able to answer:

```text
Which LCR state is active?
What is the correction value?
What route failed or required correction?
Is the residue closed, open, or transported?
Which receipt proves the imported row?
```

## Conclusion

Paper 2.75 turns the correction surface into a next-state input. It keeps the
residue visible as the suite moves from correction to registration and then to
boundary repair.
