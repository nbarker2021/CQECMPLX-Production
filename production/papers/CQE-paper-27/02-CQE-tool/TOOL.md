# Paper 27 — Tool: Observer Delay and Shared Reality Verifier

## Module
`cqe_engine.observer_delay`

## Public Surface
```python
from cqe_engine.observer_delay import (
    verify_observer_delay,
    verify_shared_reality,
    DelaySharedGluon,
)
```

## Verifiers

### verify_observer_delay()
Verifies observer delay as frame lag in Z4 cycle.

### verify_shared_reality()
Verifies shared state as Gluon overlap.

### DelaySharedGluon
```python
dsg = DelaySharedGluon()
dsg.sample(depth)                   # current sample
dsg.delayed(depth)                  # delayed sample (1 frame back)
dsg.predicted(depth)                # predicted sample (1 frame forward)
dsg.shared_state(other_C)           # shared state = C_i ∧ C_j
```

## CLI
```bash
python -m cqe_engine.observer_delay                    # full verification
python -m cqe_engine.observer_delay delay              # observer delay
python -m cqe_engine.observer_delay shared             # shared reality
```

## Receipts
Written to `proof-receipts/CQE-paper-27/observer-delay-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-27",
  "delay_verified": true,
  "shared_reality_verified": true,
  "Z4_cycle": "sample, delay, predict, synchronize"
}
```

---

*This tool IS the proof of the observer delay/shared reality. Running it discharges every Paper 27 obligation.*
