"""
Policy system.

The kernel is policy-governed. Every operation consults the active
policy before performing any side effect. The default policy is strict
and source-bound: nothing is read from or written to the host, and
external compute is forbidden.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict


_DEFAULTS: Dict[str, Any] = {
    "allow_firmware": False,
    "allow_external_io": False,
    "allow_mutation": False,
    "allow_compute": False,
    "allow_conjectural_output": False,
    "require_receipts": True,
    "require_replay": True,
    "allow_host_write": False,
}


@dataclass
class Policy:
    """Strict-by-default policy for kernel operations."""

    allow_firmware: bool = False
    allow_external_io: bool = False
    allow_mutation: bool = False
    allow_compute: bool = False
    allow_conjectural_output: bool = False
    require_receipts: bool = True
    require_replay: bool = True
    allow_host_write: bool = False
    extras: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def strict(cls) -> "Policy":
        """Return the canonical strict default policy."""
        return cls(**_DEFAULTS)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Policy":
        """Build a policy from a dict; unknown keys go to ``extras``."""
        kwargs: Dict[str, Any] = {}
        extras: Dict[str, Any] = {}
        for k, v in data.items():
            if k in _DEFAULTS:
                kwargs[k] = v
            else:
                extras[k] = v
        kwargs["extras"] = extras
        return cls(**kwargs)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return d

    def check(self, action: str) -> None:
        """Consult the policy. Raises ``KernelPolicyError`` on violation.

        Actions:
          "firmware"     -> requires ``allow_firmware``
          "external_io"  -> requires ``allow_external_io``
          "mutation"     -> requires ``allow_mutation``
          "compute"      -> requires ``allow_compute``
          "conjecture"   -> requires ``allow_conjectural_output``
          "host_write"   -> requires ``allow_host_write``
        """
        from .errors import KernelPolicyError

        table = {
            "firmware": self.allow_firmware,
            "external_io": self.allow_external_io,
            "mutation": self.allow_mutation,
            "compute": self.allow_compute,
            "conjecture": self.allow_conjectural_output,
            "host_write": self.allow_host_write,
        }
        if action not in table:
            raise KernelPolicyError(f"unknown policy action: {action!r}")
        if not table[action]:
            raise KernelPolicyError(
                f"policy forbids {action!r} (strict defaults in effect)"
            )
