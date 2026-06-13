# Paper 26.50 - Z-Pinch and Shear Claim Contract

## Purpose

This contract defines the minimum fields required before a Paper 26 claim can
be promoted.

## Required Fields

Each carrier row must provide tape id, index, input bit, integer carrier state
when applicable, octonion generator, orient bit, dominant basis index, and
shear bit when compared against a second carrier.

Each pinch row must provide transport id, classification, proof boundary,
pinch analog state, and a Boolean physical-pinch claim. For Paper 26 the
physical-pinch Boolean must remain false.

## Promotion Rules

The following may be promoted:

- period-4 integer carrier closure,
- `e4^2 = -1` and `e4^4 = 1`,
- non-associative octonion path residue,
- fixed-generator shear divergence as a carrier diagnostic,
- pinch as transport-ledger reclassification.

The following promotions are rejected:

- carrier shear to physical plasma shear without a measurement map,
- pinch reclassification to physical collapse,
- orient bit to friction mechanism,
- carrier residue to energy generation,
- horizon analogy to solved physics.

## Linked Review

This paper may speak backward to Paper 25 by inheriting unit and obligation
honesty. It may speak forward to Papers 27-29 by exporting a horizon-claim
quarantine pattern. It may not feed an unvalidated physical claim backward into
the proof stack.
