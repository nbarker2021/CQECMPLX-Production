# CMPLX-NVEST Hidden Guess Result Protocol

Every non-math NVEST diagnostic must hide the result until after the guess.

## Examples

- Predict which wave point is the true failure point before checking the held-out result.
- Predict whether an estimator will improve or degrade before running the ablation.
- Predict which product event caused a phase shift before revealing the known incident label.
- Predict whether a signal is reverting, trending, breaking, or noisy before the validation window is revealed.

## Required Record

- context id
- sealed result id
- candidate points
- guess
- confidence
- reveal
- outcome
- failure mode
- training credit flag
- map update
