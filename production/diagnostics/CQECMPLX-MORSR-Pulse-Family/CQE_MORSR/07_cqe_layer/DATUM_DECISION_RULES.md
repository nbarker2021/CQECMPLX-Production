# CQE_MORSR Datum Decision Rules

CQE_MORSR treats most diagnostic material as library-bound.

## Library-Bound

- hidden guess records
- sealed result references
- reveal records
- scoring outcomes
- failure-mode labels
- map updates
- recenter confirmations
- wave-sniffer signals

## New Datum

Create a new datum only when the revealed event changes the system's reusable map in a way that cannot be represented as:

- receipt payload
- morphon state
- diagnostic trace
- CQE validation result
- library adapter output

If it only teaches the existing map, it is a training trace, not a new datum.
