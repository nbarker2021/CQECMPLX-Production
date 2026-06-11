# CQE_MORSR Handshake And Networking Rules

CQE_MORSR handshakes use:

```text
BBA boundary read
  -> Universal Adapter handle
  -> CQE validation decision
  -> NSL gate/score
  -> receipt
  -> hidden-result map update
```

## Required Fields

- validation context id
- sealed result id
- BBA boundary result if binary-compatible
- universal adapter handle
- committed guess
- reveal
- score
- training-credit flag
- receipt hash

Networking is handled as a universal adapter product surface.
