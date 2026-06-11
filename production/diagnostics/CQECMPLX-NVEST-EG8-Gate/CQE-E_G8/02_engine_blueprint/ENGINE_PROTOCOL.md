# CQE-E/G8 Engine Protocol

```text
receive candidate point/context from NVEST
  -> read binary boundary if compatible
  -> universal adapter handle
  -> seal expected result
  -> compute Fourier/E8/G8 gate features
  -> commit gate decision
  -> reveal result
  -> score
  -> accept/reject/amortize/signal via NSL
  -> bind to library or mark candidate new datum
  -> emit receipt
```

## Gate Decisions

- accept
- reject
- amortize
- signal-only
- contaminated
- defer
