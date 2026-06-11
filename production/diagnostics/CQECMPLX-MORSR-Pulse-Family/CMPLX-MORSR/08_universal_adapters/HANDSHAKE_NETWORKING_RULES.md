# CMPLX-MORSR Handshake And Networking Rules

CMPLX-MORSR handshakes use:

```text
BBA boundary read
  -> Universal Adapter handle
  -> CQE library binding
  -> NSL gate
  -> receipt
  -> MORSR pulse/recenter trace
```

## Required Fields

- centroid id
- pulse id
- BBA boundary result if binary-compatible
- universal adapter handle
- active nodes
- hidden guess trace if non-math
- NSL delta
- receipt hash
- network endpoint or product surface if applicable

Networking is a product surface, not a separate architecture.
