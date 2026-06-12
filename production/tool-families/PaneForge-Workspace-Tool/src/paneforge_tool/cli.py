"""paneforge CLI - serve / demo / test / info / where.

Every subcommand resolves the product root first; the kernel itself is run
unmodified (it is the Event Law reference implementation and resolves its
own lib-forge relative to the product root).
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import webbrowser
from pathlib import Path

from . import __version__, data_dir, product_root

DEFAULT_PORT = 8770


def _require_product() -> Path:
    root = product_root()
    if root is None:
        sys.exit(
            "paneforge: PaneForge-Stick product not found.\n"
            "Set PANEFORGE_PRODUCT to a directory containing kernel/paneforge_kernel.py"
        )
    return root


def _kernel_env(args) -> dict:
    env = os.environ.copy()
    d = Path(args.data) if getattr(args, "data", None) else data_dir()
    d.mkdir(parents=True, exist_ok=True)
    env["PANEFORGE_DATA"] = str(d)
    return env


def _kernel_cmd(root: Path, port: int) -> list[str]:
    return [sys.executable, str(root / "kernel" / "paneforge_kernel.py"), str(port)]


def _get(port: int, path: str, timeout: float = 3.0):
    with urllib.request.urlopen(f"http://localhost:{port}{path}", timeout=timeout) as r:
        return json.loads(r.read())


def _wait_health(port: int, attempts: int = 20) -> bool:
    for _ in range(attempts):
        try:
            if _get(port, "/api/health").get("ok"):
                return True
        except (urllib.error.URLError, OSError, json.JSONDecodeError):
            time.sleep(0.5)
    return False


def cmd_where(args) -> int:
    root = product_root()
    print(f"paneforge-tool  v{__version__}")
    print(f"product root : {root if root else 'NOT FOUND'}")
    if root:
        lf = root / "lib-forge"
        forges = sorted(p.name for p in lf.iterdir() if p.is_dir()) if lf.is_dir() else []
        print(f"lib-forge    : {lf if lf.is_dir() else 'missing'}")
        print(f"forges       : {', '.join(forges)}")
        print(f"app          : {root / 'app'}")
    print(f"data dir     : {data_dir()}")
    return 0


def cmd_serve(args) -> int:
    root = _require_product()
    cmd = _kernel_cmd(root, args.port)
    print(f"paneforge: serving from {root} on port {args.port} (Ctrl+C to stop)")
    return subprocess.call(cmd, cwd=str(root), env=_kernel_env(args))


def cmd_demo(args) -> int:
    root = _require_product()
    proc = subprocess.Popen(_kernel_cmd(root, args.port), cwd=str(root), env=_kernel_env(args))
    if not _wait_health(args.port):
        proc.terminate()
        sys.exit(f"paneforge: kernel did not become healthy on port {args.port}")
    url = f"http://localhost:{args.port}/"
    print(f"paneforge: kernel healthy at {url} (pid {proc.pid})")
    webbrowser.open(url)
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
    return 0


def cmd_info(args) -> int:
    try:
        health = _get(args.port, "/api/health")
        kernel = _get(args.port, "/api/kernel")
        receipts = _get(args.port, "/api/receipts")
    except (urllib.error.URLError, OSError) as exc:
        sys.exit(f"paneforge: no kernel answering on port {args.port} ({exc})")
    print(json.dumps({"health": health, "kernel": kernel,
                      "receipt_head": receipts.get("head"),
                      "receipt_length": receipts.get("length")}, indent=2))
    return 0


def cmd_test(args) -> int:
    root = _require_product()
    test = root / "tests" / "test_demo.py"
    if not test.is_file():
        sys.exit(f"paneforge: test suite not found at {test}")
    env = _kernel_env(args)
    env["PYTHONPATH"] = str(root / "lib-forge") + os.pathsep + env.get("PYTHONPATH", "")
    print(f"paneforge: running product test suite ({test})")
    return subprocess.call([sys.executable, str(test)], cwd=str(root), env=env)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="paneforge",
                                description="PaneForge workspace tool (Event Law calendar kernel)")
    p.add_argument("--version", action="version", version=f"paneforge-tool {__version__}")
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("where", help="show resolved product root, forges, data dir")
    sp.set_defaults(fn=cmd_where)

    for name, fn, help_ in (("serve", cmd_serve, "run the kernel in the foreground"),
                            ("demo", cmd_demo, "start the kernel and open the calendar PWA")):
        sp = sub.add_parser(name, help=help_)
        sp.add_argument("--port", type=int, default=DEFAULT_PORT)
        sp.add_argument("--data", help="data dir for crystals/receipts (default ~/.paneforge)")
        sp.set_defaults(fn=fn)

    sp = sub.add_parser("info", help="query a running kernel (health, Event Law status, receipt chain)")
    sp.add_argument("--port", type=int, default=DEFAULT_PORT)
    sp.set_defaults(fn=cmd_info)

    sp = sub.add_parser("test", help="run the product test suite (PixelForge units + kernel HTTP integration)")
    sp.add_argument("--data", help="data dir override for the test run")
    sp.set_defaults(fn=cmd_test)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
