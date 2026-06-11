from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def receipt(
    *,
    kernel_version: str,
    host: str,
    task: str,
    token_sha256: str,
    features: dict[str, Any],
    diagnostics: list[dict[str, Any]],
    adapter: dict[str, Any],
    kernel_options: dict[str, Any],
) -> dict[str, Any]:
    return {
        "kernel": "CMPLX-Kernel",
        "kernel_version": kernel_version,
        "created_at": now_utc(),
        "host": host,
        "task": task,
        "token_sha256": token_sha256,
        "features": features,
        "diagnostics": diagnostics,
        "adapter": adapter,
        "kernel_options": kernel_options,
    }
