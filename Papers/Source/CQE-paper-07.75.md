# Paper 7.75 - Discrete-Continuous Bridge as Next-State Precondition

## Purpose

Paper 7.75 explains how sample-preserving bridges become preconditions for
Paper 8 and later continuum papers.

## Exported State

Paper 7 exports:

```text
indexed trace
piecewise-linear bridge
zero sample error at integer points
endpoint agreement
original discrete receipt
scope boundary for between-sample dynamics
```

## Use in Paper 8

Paper 8 may use bridge outputs as sampled receipts entering a lattice closure
template. It must preserve the indexed samples and avoid treating the
interpolant as a proof of lattice closure.

The allowed transition is:

```text
sample-preserved trace -> lattice closure input
```

The disallowed transition is:

```text
continuous drawing -> closed lattice theorem without receipt
```

## Use in Paper 9

Paper 9 may use indexed traces as Hamiltonian window inputs. If it claims time
or dynamics beyond sample preservation, Paper 9 must supply its own verifier.

## Use in Paper 16

Paper 16 may read residuals at continuum edges only if it keeps the Paper 7
scope boundary visible. Continuum collapse is not proved by interpolation.

## Precondition Rule

Before a later paper uses Paper 7, it should be able to answer:

```text
What discrete trace is being bridged?
Are all indexed samples preserved?
What is the sample error?
Is any between-sample claim being made?
Which receipt proves the bridge?
```

## Conclusion

Paper 7.75 turns sample-preserving interpolation into portable state. It lets
later papers draw and transport traces while keeping the discrete proof and
scope boundary intact.
