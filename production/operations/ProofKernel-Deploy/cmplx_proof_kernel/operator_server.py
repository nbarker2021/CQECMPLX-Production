from __future__ import annotations

import argparse
import json
import os
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from .docker_adapter import DockerToolAdapter
from .kernel_explorer import KernelExplorer
from .module_registry import ModuleRegistry
from .operator_security import OperatorSecurity
from .state_store import KernelStateStore
from .token_sidecar import KernelRequest, TokenSidecarKernel


class OperatorServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 8765) -> None:
        self.host = host
        self.port = port

    def serve(self) -> None:
        handler = self._handler()
        httpd = ThreadingHTTPServer((self.host, self.port), handler)
        print(f"CMPLX operator console: http://{self.host}:{self.port}")
        httpd.serve_forever()

    def _handler(self) -> type[BaseHTTPRequestHandler]:
        kernel = TokenSidecarKernel()
        registry = ModuleRegistry()
        store = KernelStateStore()
        security = OperatorSecurity()
        docker = DockerToolAdapter()
        explorer = KernelExplorer()
        web_root = Path(__file__).resolve().parent.parent / "web"
        ring_manifest = Path(
            os.environ.get(
                "CMPLX_KERNEL_RING_MANIFEST",
                str(Path(__file__).resolve().parent.parent.parent / "kernel_ring" / "KERNEL_RING_MANIFEST.json"),
            )
        )

        class Handler(BaseHTTPRequestHandler):
            server_version = "CMPLXOperator/0.1"

            def do_OPTIONS(self) -> None:
                self.send_response(HTTPStatus.NO_CONTENT)
                for key, value in security.response_headers().items():
                    self.send_header(key, value)
                self.end_headers()

            def do_GET(self) -> None:
                if not self._authorized():
                    return
                parsed = urlparse(self.path)
                if parsed.path in ("", "/"):
                    self._send_file(web_root / "index.html", "text/html; charset=utf-8")
                    return
                if parsed.path == "/api/health":
                    self._send_json({"status": "ok", "kernel": "CMPLX-Kernel", "security": security.summary()})
                    return
                if parsed.path == "/api/modules":
                    self._send_json(registry.summary())
                    return
                if parsed.path == "/api/proofs":
                    self._send_json(explorer.proof_index())
                    return
                if parsed.path == "/api/repo-forms":
                    self._send_json(explorer.repo_forms())
                    return
                if parsed.path == "/api/package/manifest":
                    limit = int(parse_qs(parsed.query).get("limit", ["200"])[0])
                    self._send_json(explorer.package_manifest(limit=limit))
                    return
                if parsed.path == "/api/docker/status":
                    self._send_json(docker.status())
                    return
                if parsed.path == "/api/docker/inventory":
                    self._send_json(docker.inventory())
                    return
                if parsed.path == "/api/docker/ps":
                    compose_file = parse_qs(parsed.query).get("compose_file", ["docker-compose.yml"])[0]
                    self._send_adapter_result(lambda: docker.compose_ps(compose_file))
                    return
                if parsed.path == "/api/events":
                    limit = parse_qs(parsed.query).get("limit", ["50"])[0]
                    self._send_json({"events": store.list_events(int(limit))})
                    return
                if parsed.path == "/api/kernel-ring":
                    if ring_manifest.exists():
                        self._send_json(json.loads(ring_manifest.read_text(encoding="utf-8-sig")))
                    else:
                        self._send_json({"status": "missing", "path": str(ring_manifest)}, HTTPStatus.NOT_FOUND)
                    return
                if parsed.path.startswith("/static/"):
                    target = web_root / parsed.path.removeprefix("/static/")
                    self._send_file(target, self._content_type(target))
                    return
                self._send_json({"error": "not_found"}, HTTPStatus.NOT_FOUND)

            def do_POST(self) -> None:
                if not self._authorized() or not self._body_allowed():
                    return
                parsed = urlparse(self.path)
                if parsed.path == "/api/process":
                    payload = self._read_json()
                    options = dict(payload.get("kernel_options", {}))
                    request = KernelRequest(
                        token_string=str(payload.get("token_string", "")),
                        task=str(payload.get("task", "operator_console")),
                        host=str(payload.get("host", "operator-web")),
                        metadata=dict(payload.get("metadata", {})) | {"entrypoint": "operator_server"},
                        kernel_options=options,
                    )
                    result = kernel.process(request)
                    event = store.record_event(
                        event_type="kernel_process",
                        module_id="operator-web",
                        token_sha256=result["boundary_frame"]["sha256"],
                        payload={
                            "task": request.task,
                            "host": request.host,
                            "kernel_options": result["receipt"]["kernel_options"],
                            "features": result["receipt"]["features"],
                        },
                    )
                    result["state_event"] = event
                    self._send_json(result)
                    return
                if parsed.path == "/api/module-state":
                    payload = self._read_json()
                    module_id = str(payload["module_id"])
                    state = dict(payload.get("state", {}))
                    self._send_json(store.set_module_state(module_id, state))
                    return
                if parsed.path == "/api/docker/up":
                    payload = self._read_json()
                    self._send_adapter_result(
                        lambda: docker.compose_up(str(payload.get("compose_file", "docker-compose.yml")), payload.get("service"))
                    )
                    return
                if parsed.path == "/api/docker/down":
                    payload = self._read_json()
                    self._send_adapter_result(lambda: docker.compose_down(str(payload.get("compose_file", "docker-compose.yml"))))
                    return
                if parsed.path == "/api/docker/boundary-insert":
                    payload = self._read_json()
                    self._send_adapter_result(lambda: docker.frame_compose_insert(payload))
                    return
                self._send_json({"error": "not_found"}, HTTPStatus.NOT_FOUND)

            def log_message(self, format: str, *args: Any) -> None:
                return

            def _read_json(self) -> dict[str, Any]:
                length = int(self.headers.get("content-length", "0"))
                raw = self.rfile.read(length).decode("utf-8")
                value = json.loads(raw) if raw else {}
                if not isinstance(value, dict):
                    raise ValueError("request body must be a JSON object")
                return value

            def _authorized(self) -> bool:
                client = self.client_address[0] if self.client_address else "unknown"
                ok, status, message = security.check_headers(self.headers, client)
                if not ok:
                    self._send_json({"error": message}, status)
                    return False
                return True

            def _body_allowed(self) -> bool:
                ok, status, message = security.check_length(self.headers)
                if not ok:
                    self._send_json({"error": message}, status)
                    return False
                return True

            def _send_adapter_result(self, fn: Any) -> None:
                try:
                    self._send_json(fn())
                except PermissionError as exc:
                    self._send_json({"error": str(exc)}, HTTPStatus.FORBIDDEN)
                except FileNotFoundError as exc:
                    self._send_json({"error": str(exc)}, HTTPStatus.NOT_FOUND)
                except ValueError as exc:
                    self._send_json({"error": str(exc)}, HTTPStatus.BAD_REQUEST)

            def _send_json(self, payload: dict[str, Any], status: HTTPStatus = HTTPStatus.OK) -> None:
                data = json.dumps(payload, indent=2, sort_keys=True).encode("utf-8")
                self.send_response(status)
                self.send_header("content-type", "application/json; charset=utf-8")
                self.send_header("content-length", str(len(data)))
                for key, value in security.response_headers().items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(data)

            def _send_file(self, path: Path, content_type: str) -> None:
                if not path.exists() or not path.is_file():
                    self._send_json({"error": "not_found", "path": str(path)}, HTTPStatus.NOT_FOUND)
                    return
                data = path.read_bytes()
                self.send_response(HTTPStatus.OK)
                self.send_header("content-type", content_type)
                self.send_header("content-length", str(len(data)))
                for key, value in security.response_headers().items():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(data)

            def _content_type(self, path: Path) -> str:
                if path.suffix == ".css":
                    return "text/css; charset=utf-8"
                if path.suffix == ".js":
                    return "text/javascript; charset=utf-8"
                if path.suffix == ".json":
                    return "application/json; charset=utf-8"
                return "application/octet-stream"

        return Handler


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CMPLX local operator web console")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args(argv)
    OperatorServer(host=args.host, port=args.port).serve()
    return 0
