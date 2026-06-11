from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class HiddenGuess:
    diagnostic_id: str
    action: str
    hidden_target_hash: str
    guess: dict[str, Any]
    revealed: dict[str, Any]
    score: float
    status: str


class HiddenGuessResultLayer:
    """Ablation layer for every non-math diagnostic.

    The target is represented by a hash before the guess is made. The local
    check is then revealed and scored. This creates the micro-training receipt
    without letting the diagnostic inspect the answer first.
    """

    def run(self, action: str, features: dict[str, Any], target: dict[str, Any]) -> HiddenGuess:
        target_hash = hashlib.sha256(repr(sorted(target.items())).encode("utf-8")).hexdigest()
        guess = self._guess(action, features)
        score = self._score(guess, target)
        return HiddenGuess(
            diagnostic_id=hashlib.sha256(f"{action}:{target_hash}".encode("utf-8")).hexdigest()[:16],
            action=action,
            hidden_target_hash=target_hash,
            guess=guess,
            revealed=target,
            score=score,
            status="pass" if score >= 0.66 else "review",
        )

    def _guess(self, action: str, features: dict[str, Any]) -> dict[str, Any]:
        token_count = int(features.get("token_count", 0))
        unique_ratio = float(features.get("unique_ratio", 0.0))
        line_count = int(features.get("line_count", 0))
        entropy_band = features.get("entropy_band", "unknown")
        return {
            "action": action,
            "likely_needs_structure": token_count > 80 or line_count > 8,
            "likely_repetitive": unique_ratio < 0.45 and token_count > 20,
            "likely_high_density": entropy_band == "high",
        }

    def _score(self, guess: dict[str, Any], target: dict[str, Any]) -> float:
        keys = [key for key in guess if key in target]
        if not keys:
            return 0.0
        hits = sum(1 for key in keys if guess[key] == target[key])
        return hits / len(keys)

