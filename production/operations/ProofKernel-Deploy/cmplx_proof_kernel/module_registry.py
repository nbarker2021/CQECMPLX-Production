from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_MODULES: list[dict[str, Any]] = [
    {
        "module_id": "sidecar-runtime",
        "title": "Sidecar Runtime",
        "kind": "runtime",
        "status": "preinstalled",
        "entrypoint": "boot.py",
        "capabilities": ["stdin", "file", "request-json", "training-mode"],
    },
    {
        "module_id": "operator-web",
        "title": "Operator Web Console",
        "kind": "frontend",
        "status": "preinstalled",
        "entrypoint": "python boot.py --serve",
        "capabilities": ["local-http", "process-token", "inspect-modules", "inspect-events"],
    },
    {
        "module_id": "kernel-state-store",
        "title": "Kernel State Store",
        "kind": "database",
        "status": "preinstalled",
        "entrypoint": "cmplx_kernel.state_store.KernelStateStore",
        "capabilities": ["sqlite", "event-log", "module-state"],
    },
    {
        "module_id": "kernel-ring-loader",
        "title": "Kernel Ring Loader",
        "kind": "companion-kernel",
        "status": "preinstalled",
        "entrypoint": "../kernel_ring/KERNEL_RING_MANIFEST.json",
        "capabilities": ["lib-kernel", "lattice-kernel", "reforge-kernel"],
    },
    {
        "module_id": "docker-tool-root",
        "title": "Docker Tool Root",
        "kind": "external-tool-adapter",
        "status": "preinstalled-readonly",
        "entrypoint": "cmplx_kernel.docker_adapter.DockerToolAdapter",
        "capabilities": ["docker-status", "compose-inventory", "compose-ps", "gated-compose-up", "gated-compose-down"],
    },
    {
        "module_id": "kernel-explorer",
        "title": "Kernel Explorer",
        "kind": "read-only-browser",
        "status": "preinstalled",
        "entrypoint": "cmplx_kernel.kernel_explorer.KernelExplorer",
        "capabilities": ["proof-index", "repo-form-index", "package-manifest"],
    },
    {
        "module_id": "operator-security",
        "title": "Operator Security",
        "kind": "operator-guardrail",
        "status": "preinstalled",
        "entrypoint": "cmplx_kernel.operator_security.OperatorSecurity",
        "capabilities": ["bearer-token-auth", "cors-policy", "request-size-limit", "rate-limit"],
    },
]


class ModuleRegistry:
    """Registry for built-in and future modular kernel tools."""

    def __init__(self, path: str | Path = "modules/MODULE_REGISTRY.json") -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            self.path.write_text(
                json.dumps({"modules": DEFAULT_MODULES}, indent=2, sort_keys=True),
                encoding="utf-8",
            )

    def list_modules(self) -> list[dict[str, Any]]:
        payload = json.loads(self.path.read_text(encoding="utf-8"))
        modules = payload.get("modules", [])
        if not isinstance(modules, list):
            raise ValueError("module registry must contain a modules list")
        return modules

    def get(self, module_id: str) -> dict[str, Any] | None:
        for module in self.list_modules():
            if module.get("module_id") == module_id:
                return module
        return None

    def summary(self) -> dict[str, Any]:
        modules = self.list_modules()
        return {
            "path": str(self.path),
            "module_count": len(modules),
            "modules": modules,
        }
