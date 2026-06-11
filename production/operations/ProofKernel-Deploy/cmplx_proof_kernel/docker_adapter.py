from __future__ import annotations

import os
import subprocess
from pathlib import Path
from typing import Any

from .adapters import BinaryBoundaryAdapter


class DockerToolAdapter:
    """Controlled adapter for an external Docker tool root."""

    def __init__(self, root: str | Path | None = None) -> None:
        self.root = Path(root or os.environ.get("CMPLX_DOCKER_ROOT", "D:/DockerContainers"))
        self.boundary = BinaryBoundaryAdapter()

    def status(self) -> dict[str, Any]:
        return {
            "root": str(self.root),
            "root_exists": self.root.exists(),
            "docker": self._run(["docker", "--version"]),
            "compose": self._run(["docker", "compose", "version"]),
            "control_enabled": self.control_enabled,
        }

    def inventory(self) -> dict[str, Any]:
        compose_files = []
        docs = []
        dockerfiles = []
        if self.root.exists():
            for path in self.root.rglob("*"):
                if not path.is_file() or self._excluded(path):
                    continue
                rel = str(path.relative_to(self.root))
                lower = path.name.lower()
                if lower.startswith("docker-compose") and lower.endswith((".yml", ".yaml")):
                    compose_files.append(rel)
                elif lower.startswith("dockerfile"):
                    dockerfiles.append(rel)
                elif path.suffix.lower() == ".md":
                    docs.append(rel)
        return {
            "root": str(self.root),
            "compose_files": sorted(compose_files),
            "dockerfiles": sorted(dockerfiles),
            "docs": sorted(docs)[:100],
        }

    def compose_ps(self, compose_file: str = "docker-compose.yml") -> dict[str, Any]:
        target = self._resolve_compose(compose_file)
        return {
            "compose_file": str(target),
            "result": self._run(["docker", "compose", "-f", str(target), "ps"]),
        }

    def compose_up(self, compose_file: str = "docker-compose.yml", service: str | None = None) -> dict[str, Any]:
        self._require_control()
        target = self._resolve_compose(compose_file)
        cmd = ["docker", "compose", "-f", str(target), "up", "-d"]
        if service:
            cmd.append(service)
        return {"compose_file": str(target), "result": self._run(cmd, timeout=300)}

    def compose_down(self, compose_file: str = "docker-compose.yml") -> dict[str, Any]:
        self._require_control()
        target = self._resolve_compose(compose_file)
        return {"compose_file": str(target), "result": self._run(["docker", "compose", "-f", str(target), "down"], timeout=300)}

    def frame_compose_insert(self, payload: dict[str, Any]) -> dict[str, Any]:
        self._resolve_compose(str(payload["target_compose"]))
        frame = self.boundary.pack_compose_insert(payload)
        return {
            "boundary": "BinaryBoundaryAdapter",
            "mode": "compose-insert",
            "target_root": str(self.root),
            "target_compose": payload["target_compose"],
            "frame": {
                "encoding": frame.encoding,
                "byte_count": frame.byte_count,
                "sha256": frame.sha256,
                "payload_b64": frame.payload_b64,
            },
        }

    @property
    def control_enabled(self) -> bool:
        return os.environ.get("CMPLX_DOCKER_ENABLE_CONTROL", "").lower() in {"1", "true", "yes", "on"}

    def _resolve_compose(self, compose_file: str) -> Path:
        target = (self.root / compose_file).resolve()
        root = self.root.resolve()
        if not str(target).lower().startswith(str(root).lower()):
            raise ValueError("compose file must stay inside Docker tool root")
        if not target.exists():
            raise FileNotFoundError(str(target))
        return target

    def _require_control(self) -> None:
        if not self.control_enabled:
            raise PermissionError("set CMPLX_DOCKER_ENABLE_CONTROL=1 to allow Docker start/stop actions")

    def _excluded(self, path: Path) -> bool:
        parts = {part.lower() for part in path.parts}
        return "__pycache__" in parts or ".git" in parts or "secrets" in parts

    def _run(self, cmd: list[str], timeout: int = 30) -> dict[str, Any]:
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(self.root) if self.root.exists() else None,
                capture_output=True,
                text=True,
                timeout=timeout,
                shell=False,
            )
            return {
                "ok": proc.returncode == 0,
                "returncode": proc.returncode,
                "stdout": proc.stdout.strip(),
                "stderr": proc.stderr.strip(),
            }
        except FileNotFoundError as exc:
            return {"ok": False, "returncode": None, "stdout": "", "stderr": str(exc)}
        except subprocess.TimeoutExpired:
            return {"ok": False, "returncode": None, "stdout": "", "stderr": "command timed out"}
