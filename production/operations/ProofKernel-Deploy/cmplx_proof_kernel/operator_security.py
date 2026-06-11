from __future__ import annotations

import os
import time
from http import HTTPStatus
from typing import Any


class OperatorSecurity:
    """Local-first operator guardrails for auth, CORS, size, and rate limits."""

    def __init__(self) -> None:
        self.token = os.environ.get("CMPLX_OPERATOR_TOKEN", "")
        self.cors_origin = os.environ.get("CMPLX_OPERATOR_CORS_ORIGIN", "")
        self.max_body_bytes = int(os.environ.get("CMPLX_OPERATOR_MAX_BODY_BYTES", "1048576"))
        self.rate_limit_per_minute = int(os.environ.get("CMPLX_OPERATOR_RATE_LIMIT_PER_MINUTE", "120"))
        self._requests: dict[str, list[float]] = {}

    @property
    def auth_required(self) -> bool:
        return bool(self.token)

    def check_headers(self, headers: Any, client_id: str) -> tuple[bool, HTTPStatus, str]:
        allowed, status, message = self._check_rate(client_id)
        if not allowed:
            return allowed, status, message
        if self.token:
            supplied = headers.get("authorization", "")
            if supplied != f"Bearer {self.token}":
                return False, HTTPStatus.UNAUTHORIZED, "missing or invalid bearer token"
        return True, HTTPStatus.OK, "ok"

    def check_length(self, headers: Any) -> tuple[bool, HTTPStatus, str]:
        length = int(headers.get("content-length", "0"))
        if length > self.max_body_bytes:
            return False, HTTPStatus.REQUEST_ENTITY_TOO_LARGE, "request body too large"
        return True, HTTPStatus.OK, "ok"

    def response_headers(self) -> dict[str, str]:
        headers = {
            "x-cmplx-auth-required": "true" if self.auth_required else "false",
            "x-cmplx-rate-limit-per-minute": str(self.rate_limit_per_minute),
        }
        if self.cors_origin:
            headers["access-control-allow-origin"] = self.cors_origin
            headers["access-control-allow-headers"] = "authorization, content-type"
            headers["access-control-allow-methods"] = "GET, POST, OPTIONS"
        return headers

    def summary(self) -> dict[str, Any]:
        return {
            "auth_required": self.auth_required,
            "cors_enabled": bool(self.cors_origin),
            "max_body_bytes": self.max_body_bytes,
            "rate_limit_per_minute": self.rate_limit_per_minute,
        }

    def _check_rate(self, client_id: str) -> tuple[bool, HTTPStatus, str]:
        now = time.time()
        window_start = now - 60
        recent = [stamp for stamp in self._requests.get(client_id, []) if stamp >= window_start]
        if len(recent) >= self.rate_limit_per_minute:
            self._requests[client_id] = recent
            return False, HTTPStatus.TOO_MANY_REQUESTS, "rate limit exceeded"
        recent.append(now)
        self._requests[client_id] = recent
        return True, HTTPStatus.OK, "ok"
