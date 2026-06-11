from __future__ import annotations

import base64
import hashlib
import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BoundaryFrame:
    encoding: str
    byte_count: int
    sha256: str
    payload_b64: str


class BinaryBoundaryAdapter:
    """Stable binary frame for any host that can pass files or strings."""

    def pack_text(self, text: str, encoding: str = "utf-8") -> BoundaryFrame:
        data = text.encode(encoding)
        return BoundaryFrame(
            encoding=encoding,
            byte_count=len(data),
            sha256=hashlib.sha256(data).hexdigest(),
            payload_b64=base64.b64encode(data).decode("ascii"),
        )

    def unpack_text(self, frame: BoundaryFrame) -> str:
        data = base64.b64decode(frame.payload_b64.encode("ascii"))
        if hashlib.sha256(data).hexdigest() != frame.sha256:
            raise ValueError("boundary frame hash mismatch")
        return data.decode(frame.encoding)

    def pack_json(self, payload: dict[str, Any], encoding: str = "utf-8") -> BoundaryFrame:
        return self.pack_text(json.dumps(payload, indent=2, sort_keys=True), encoding=encoding)

    def pack_compose_insert(self, payload: dict[str, Any], encoding: str = "utf-8") -> BoundaryFrame:
        required = {"insert_id", "target_compose", "compose_overlay", "reason"}
        missing = sorted(required.difference(payload))
        if missing:
            raise ValueError(f"compose insert missing required fields: {', '.join(missing)}")
        if not isinstance(payload["compose_overlay"], dict):
            raise ValueError("compose_overlay must be an object")
        return self.pack_json(
            {
                "boundary_type": "docker_compose_insert",
                "policy": "base compose remains below kernel and read-only; new needs enter as override inserts",
                **payload,
            },
            encoding=encoding,
        )


class UniversalAdapter:
    """Minimal host handshake for file, repo, CLI, future MCP, or HTTP use."""

    def handshake(self, host: str, capabilities: list[str] | None = None) -> dict[str, Any]:
        return {
            "adapter": "CMPLX Universal Adapter",
            "host": host,
            "capabilities": capabilities or ["file", "stdin", "json"],
            "protocol": "token_string_in_receipt_out",
            "required_fields": ["token_string"],
            "optional_fields": ["task", "metadata", "host"],
        }

    def normalize_json(self, payload: str) -> dict[str, Any]:
        value = json.loads(payload)
        if not isinstance(value, dict):
            raise ValueError("adapter payload must be a JSON object")
        if "token_string" not in value:
            raise ValueError("adapter payload missing token_string")
        return value
