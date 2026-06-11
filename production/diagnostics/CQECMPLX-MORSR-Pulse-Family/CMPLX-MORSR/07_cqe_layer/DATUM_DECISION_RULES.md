# CMPLX-MORSR Datum Decision Rules

Most CMPLX-MORSR outputs are not new data. They are library-bound events.

## Library-Bound

- pulse event
- active-node set
- hidden guess
- reveal
- score
- recenter
- shadow direction
- failure/success point
- wave-sniffer signal

## Candidate New Datum

A confirmed reading may become a new datum only if it is not already representable as:

- an existing morphon
- a receipt payload
- a diagnostic trace
- a CQE validation result
- a library adapter output

If it is only a new view or a new score, it is library-bound.
