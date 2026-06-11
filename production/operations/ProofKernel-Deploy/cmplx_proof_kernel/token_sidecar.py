from __future__ import annotations

import hashlib
import math
import re
from dataclasses import asdict, dataclass, field
from typing import Any

from .adapters import BinaryBoundaryAdapter, UniversalAdapter
from .diagnostics import HiddenGuessResultLayer
from .schemas import receipt


KERNEL_VERSION = "2.1.0-sidecar"


@dataclass(frozen=True)
class KernelRequest:
    token_string: str
    task: str = "extend_token_work"
    host: str = "generic-ai"
    metadata: dict[str, Any] = field(default_factory=dict)
    kernel_options: dict[str, Any] = field(default_factory=dict)


class TokenSidecarKernel:
    def __init__(self) -> None:
        self.boundary = BinaryBoundaryAdapter()
        self.adapter = UniversalAdapter()
        self.hidden_guess = HiddenGuessResultLayer()

    def process(self, request: KernelRequest) -> dict[str, Any]:
        frame = self.boundary.pack_text(request.token_string)
        features = self._features(request.token_string)
        options = self._options(request.kernel_options)
        diagnostics = self._diagnostics(features, options)
        enriched = self._enrich(request.token_string, features, diagnostics)
        base_receipt = receipt(
            kernel_version=KERNEL_VERSION,
            host=request.host,
            task=request.task,
            token_sha256=frame.sha256,
            features=features,
            diagnostics=diagnostics,
            adapter=self.adapter.handshake(request.host),
            kernel_options=options,
        )
        return {
            "enriched_text": enriched,
            "receipt": base_receipt,
            "boundary_frame": asdict(frame),
            "metadata": request.metadata,
        }

    def _features(self, text: str) -> dict[str, Any]:
        tokens = re.findall(r"\S+", text)
        lower_tokens = [token.lower() for token in tokens]
        unique = len(set(lower_tokens))
        token_count = len(tokens)
        chars = list(text)
        entropy = self._entropy(chars)
        centroid = self._centroid(tokens)
        return {
            "char_count": len(text),
            "line_count": text.count("\n") + 1 if text else 0,
            "token_count": token_count,
            "unique_token_count": unique,
            "unique_ratio": round(unique / token_count, 4) if token_count else 0.0,
            "entropy": round(entropy, 4),
            "entropy_band": self._entropy_band(entropy),
            "centroid": centroid,
            "wave": self._wave(tokens),
        }

    def _options(self, options: dict[str, Any]) -> dict[str, Any]:
        training_mode = bool(options.get("training_mode", False))
        require_guess_mode = bool(options.get("require_guess_mode", False))
        return {
            "training_mode": training_mode,
            "guess_mode": "hidden_guess_result" if training_mode else "quiet",
            "require_guess_mode": require_guess_mode,
        }

    def _diagnostics(self, features: dict[str, Any], options: dict[str, Any]) -> list[dict[str, Any]]:
        target = {
            "likely_needs_structure": features["token_count"] > 96 or features["line_count"] > 10,
            "likely_repetitive": features["unique_ratio"] < 0.4 and features["token_count"] > 20,
            "likely_high_density": features["entropy"] >= 4.2,
        }
        if options["training_mode"]:
            hidden = self.hidden_guess.run(
                action="token_stream_readiness",
                features=features,
                target=target,
            )
            return [asdict(hidden)]
        return [
            {
                "diagnostic_id": "quiet-token-stream-readiness",
                "action": "token_stream_readiness",
                "mode": "quiet",
                "status": "pass" if not target["likely_needs_structure"] else "review",
                "summary": {
                    "needs_structure": target["likely_needs_structure"],
                    "high_density": target["likely_high_density"],
                },
            }
        ]

    def _enrich(self, text: str, features: dict[str, Any], diagnostics: list[dict[str, Any]]) -> str:
        notes = [
            "CMPLX sidecar extension:",
            f"- token_count={features['token_count']} unique_ratio={features['unique_ratio']} entropy_band={features['entropy_band']}",
            f"- centroid={features['centroid']} wave={features['wave']}",
            "- route through CQE: engine -> math/proof anchor -> product surface -> receipt",
            "- use Hidden Guess Result when training_mode is enabled for non-math validation or diagnostic choices",
            "- preserve reusable behavior for lib promotion; keep identity, lineage, and receipts staged",
        ]
        if diagnostics and diagnostics[0].get("status") == "review":
            notes.append("- diagnostic_status=review: add structure before acting on this token stream")
        else:
            notes.append("- diagnostic_status=pass: token stream is ready for sidecar-assisted continuation")
        if diagnostics and diagnostics[0].get("mode") == "quiet":
            notes.append("- guess_mode=quiet: enable training_mode for Hidden Guess Result receipts")
        return text.rstrip() + "\n\n" + "\n".join(notes)

    def _entropy(self, chars: list[str]) -> float:
        if not chars:
            return 0.0
        counts: dict[str, int] = {}
        for char in chars:
            counts[char] = counts.get(char, 0) + 1
        total = len(chars)
        return -sum((count / total) * math.log2(count / total) for count in counts.values())

    def _entropy_band(self, entropy: float) -> str:
        if entropy >= 4.2:
            return "high"
        if entropy >= 3.0:
            return "medium"
        return "low"

    def _centroid(self, tokens: list[str]) -> dict[str, Any]:
        if not tokens:
            return {"index": 0, "token": "", "sha8": ""}
        mid = len(tokens) // 2
        token = tokens[mid]
        return {
            "index": mid,
            "token": token[:48],
            "sha8": hashlib.sha256(token.encode("utf-8")).hexdigest()[:8],
        }

    def _wave(self, tokens: list[str]) -> dict[str, Any]:
        if not tokens:
            return {"period_hint": 0, "amplitude": 0}
        lengths = [len(token) for token in tokens]
        amplitude = max(lengths) - min(lengths)
        period_hint = self._period_hint(lengths)
        return {"period_hint": period_hint, "amplitude": amplitude}

    def _period_hint(self, values: list[int]) -> int:
        if len(values) < 4:
            return len(values)
        best_period = 1
        best_error = float("inf")
        max_period = min(12, len(values) // 2)
        for period in range(1, max_period + 1):
            error = 0
            comparisons = 0
            for idx in range(period, len(values)):
                error += abs(values[idx] - values[idx - period])
                comparisons += 1
            mean_error = error / comparisons if comparisons else float("inf")
            if mean_error < best_error:
                best_error = mean_error
                best_period = period
        return best_period
