# Hidden Guess Result Protocol

This protocol is required for every CMPLX-MORSR non-math diagnostic, validation, review, recommendation, and action choice.

## Rule

The AI or engine must commit to a guess before seeing the held-out result.

## Phases

1. `context_open`: show only the allowed context.
2. `result_sealed`: store the expected result, label, answer, or oracle behind a sealed reference.
3. `guess_commit`: require a choice, classification, diagnosis, confidence, and reason.
4. `result_reveal`: reveal the held-out result after commit.
5. `score`: mark hit, miss, partial, overfit, underfit, or invalid.
6. `delta_map`: record what changed between the guess and the result.
7. `training_trace`: write the example into the diagnostic map.

## Required Record

```json
{
  "protocol": "hidden_guess_result_v1",
  "context_id": "string",
  "sealed_result_id": "string",
  "guess": {
    "choice": "string",
    "confidence": 0.0,
    "reason": "string"
  },
  "revealed_result": {
    "label": "string",
    "source": "string"
  },
  "score": {
    "outcome": "hit|miss|partial|invalid",
    "delta": "string",
    "failure_mode": "string"
  },
  "map_update": {
    "pattern": "string",
    "next_check": "string"
  }
}
```

## Forbidden Shortcut

No diagnostic may use an answer, label, future observation, test result, review verdict, or expected outcome before the guess phase. If a tool already knows the answer, the run must be marked `contaminated` and excluded from training credit.
