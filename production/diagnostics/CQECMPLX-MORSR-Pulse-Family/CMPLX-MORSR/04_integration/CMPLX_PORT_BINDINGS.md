# CMPLX Port Bindings

CMPLX-MORSR binds later MORSR internals into CMPLX through stable ports.

## Provided Port

- `diagnostic`: exposes pulse, scan, traversal, hidden-guess diagnostics, shadow action reports, and recenter receipts.

## Consumed Ports

- `engine`: receives problem context and returns diagnostic conclusions.
- `conservation`: scores whether a recentering reduces or conserves the active tension.
- `receipt`: records every pulse, guess, reveal, score, and map update.
- `memory`: stores training traces and repeated diagnostic maps.
- `cache`: prevents duplicate pulse work when context and centroid are identical.
- `geometry`: supplies canonical E8 directions and root/chamber metadata.

## Adapter Boundary

The later supplied MORSR tool can have any internal method names. The adapter must expose the following CMPLX-facing calls:

- `diagnostic.seed(context) -> centroid`
- `diagnostic.pulse(centroid, directions=240) -> active_nodes`
- `diagnostic.guess(context, active_nodes) -> sealed_guess`
- `diagnostic.reveal(sealed_result_id) -> result`
- `diagnostic.score(guess, result) -> honesty_score`
- `diagnostic.recenter(confirmed_node) -> centroid`
- `diagnostic.trace() -> receipt_like_record`
