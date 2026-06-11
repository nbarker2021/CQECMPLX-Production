# CMPLX-NVEST Engine Protocol

## Core Loop

```text
input target identity/context/signal
  -> universal translate into diagnostic form
  -> binary boundary read if input is binary-compatible
  -> Fourier engine vehicle wave/centroid decomposition
  -> estimator/ablation pass
  -> identify candidate error/failure/success/value/risk points
  -> send candidates to CQE-E/G8 gate
  -> receive hidden-result score and gate decision
  -> bind result to target identity
  -> emit receipt and map update
```

## Decomposition Families

- `cmplx.engine.fourier.FourierVehicle`
- direct wave vs spectral wave
- multi-window centroid bands
- residual tension
- regime classification
- estimator ablation
- active node/signal point discovery
- shadow/gap direction discovery

## Outputs

- diagnostic target identity
- decomposition report
- candidate point list
- gate request to CQE-E/G8
- selected point/action
- hidden-result trace
- receipt
- map update
