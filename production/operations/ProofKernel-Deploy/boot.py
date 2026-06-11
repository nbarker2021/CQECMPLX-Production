from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cmplx_proof_kernel.kernel_core import ProofKernelRequest, ProofSidecarKernel
from cmplx_proof_kernel.harness import ProofHarness
from cmplx_proof_kernel.falsifier import Falsifier


def _read_input(args: argparse.Namespace) -> str:
    if args.demo:
        return Path("examples/sample_token_stream.txt").read_text(encoding="utf-8")
    if args.file:
        return Path(args.file).read_text(encoding="utf-8")
    if args.stdin:
        return sys.stdin.read()
    if not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def _request_from_input(args: argparse.Namespace, raw_input: str) -> ProofKernelRequest:
    if args.request_json:
        payload = json.loads(raw_input)
        if not isinstance(payload, dict):
            raise ValueError("request JSON must be an object")
        kernel_options = dict(payload.get("kernel_options", {}))
        if args.training_mode:
            kernel_options["training_mode"] = True
        if args.local_full_program:
            kernel_options["training_mode"] = True
            kernel_options["require_guess_mode"] = True
        return ProofKernelRequest(
            token_string=str(payload.get("token_string", "")),
            task=str(payload.get("task", args.task)),
            host=str(payload.get("host", args.host)),
            metadata=dict(payload.get("metadata", {})) | {"entrypoint": "boot.py"},
            kernel_options=kernel_options,
            paper_id=payload.get("paper_id"),
            theorem_id=payload.get("theorem_id"),
            validation_mode=payload.get("validation_mode", args.validation_mode),
        )
    
    kernel_options = {
        "training_mode": bool(args.training_mode or args.local_full_program),
        "require_guess_mode": bool(args.local_full_program),
    }
    return ProofKernelRequest(
        token_string=raw_input,
        task=args.task,
        host=args.host,
        metadata={"entrypoint": "boot.py"},
        kernel_options=kernel_options,
        validation_mode=args.validation_mode,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="CQECMPLX ProofValidatedSuite Kernel")
    parser.add_argument("--file", help="Read token string from a file.")
    parser.add_argument("--stdin", action="store_true", help="Read token string from stdin.")
    parser.add_argument("--demo", action="store_true", help="Run the bundled demo input.")
    parser.add_argument("--json", action="store_true", help="Emit full JSON receipt.")
    parser.add_argument("--request-json", action="store_true", help="Parse input as sidecar request JSON.")
    parser.add_argument("--training-mode", action="store_true", help="Enable Hidden Guess Result receipts.")
    parser.add_argument("--local-full-program", action="store_true", help="Require training-mode guess diagnostics for local operation.")
    parser.add_argument("--serve", action="store_true", help="Run the local operator web console.")
    parser.add_argument("--serve-host", default="127.0.0.1", help="Operator web console host.")
    parser.add_argument("--serve-port", type=int, default=8765, help="Operator web console port.")
    parser.add_argument("--task", default="validate_proof", help="Host task label.")
    parser.add_argument("--host", default="proof-reviewer", help="Host AI/runtime label.")
    parser.add_argument("--validation-mode", default="full", choices=["full", "theorem", "paper", "falsifier", "workbook"], help="Validation mode.")
    parser.add_argument("--paper-id", help="Paper ID for paper/theorem validation.")
    parser.add_argument("--theorem-id", help="Theorem ID for theorem validation.")
    args = parser.parse_args()

    if args.serve:
        print("Operator web console not yet implemented for ProofValidatedSuite")
        return 1

    raw_input = _read_input(args)
    if not raw_input.strip():
        parser.error("no token string supplied; use --demo, --file, --stdin, or pipe text")

    kernel = ProofSidecarKernel()
    receipt = kernel.process(_request_from_input(args, raw_input))

    if args.json:
        print(json.dumps(asdict(receipt), indent=2, sort_keys=True))
    else:
        print(receipt.metadata.get("enriched_text", ""))
        print("\n--- CQECMPLX PROOF RECEIPT ---")
        print(json.dumps(asdict(receipt), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())