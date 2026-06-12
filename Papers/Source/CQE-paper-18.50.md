# Paper 18.50 - VOA / Moonshine Route Claim Contract

## Purpose

This contract governs all Paper 18 claims. It admits finite seed and bounded
route receipts while rejecting global Moonshine or extractor promotions.

## Admitted Claims

Admit a claim when it gives:

```text
route source
route target
finite or bounded scope
verifier status
honesty label
open route residue
```

## Rejected Promotions

Reject by default:

```text
finite VOA seed -> full Moonshine identification
bounded McKay table -> full McKay-Thompson arithmetic
registered correction class -> proved Rule 30 extractor
Monster scalar -> physical representation theorem
pass_with_open_gaps -> closed theorem
```

## Hidden-Guess Rule

All route diagnostics must hide the receipt until the reviewer has classified
the route as:

```text
closed finite
bounded table
bounded open-gap
open
invalid
```

## Linked Receipt

Current receipt:

```text
production/formal-papers/CQE-paper-18/voa_moonshine_routes_receipt.json
```

Current verdict:

```text
finite VOA seed: pass
static Z4 route template: pass
bounded McKay bootstrap: pass
correction_via_voa: open
full Moonshine route: open
```

## Boundary Failure

The contract fails if a later paper says Paper 18 completes
`correction_via_voa`, proves the global Rule 30 extractor, or identifies the
finite seed with full Moonshine without a transport theorem.

It passes if a later paper uses Paper 18 as bounded route evidence and carries
the open global residues forward.

## Conclusion

Paper 18.50 keeps bounded route evidence useful without letting it become a
hidden global proof claim.
