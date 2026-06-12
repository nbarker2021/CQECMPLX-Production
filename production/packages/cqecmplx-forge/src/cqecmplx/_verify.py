"""cqecmplx-verify — run the ring's own verifiers as an install check.

Every check is a real verifier from the packaged modules, not a mock.
Exit code 0 = the installed wheel is healthy.
"""
import sys


def main() -> int:
    checks = []

    def run(name, fn):
        try:
            r = fn()
            ok = (r is True) or (isinstance(r, dict) and r.get("status", "pass") in ("pass", "ok", True))
            checks.append((name, ok, "" if ok else str(r)[:80]))
        except Exception as exc:
            checks.append((name, False, f"{type(exc).__name__}: {exc}"))

    from cqecmplx.lattice.centroid_voa import verify_gluon_invariance
    from cqecmplx.lattice.rule90_linearization import verify_rule90_linearization
    from cqecmplx.lattice.binary_boundary_adapter import adapt
    from cqecmplx.engines import chroma, graphstax

    run("gluon invariance (Theorem 0)", verify_gluon_invariance)
    run("rule90 linearization (O2')", verify_rule90_linearization)
    run("BBA adapt round-trip", lambda: bool(adapt(b"cqecmplx")["summary"]["n_bits"]))
    run("superperm n4 coverage", lambda: graphstax.coverage_check(graphstax.SUPERPERM_N4, 4))
    run("superperm n5 octad coverage", lambda: all(
        graphstax.coverage_check(s, 5) for s in graphstax.N5_OCTAD))
    run("Event Law mint+reuse", lambda: (
        lambda e: e.execute("verify") and e.execute("verify").get("receipt") is not None
    )(chroma.ChromaForgeEngine()))

    def _lifecycle_check():
        import tempfile, os
        e = chroma.ChromaForgeEngine()
        vault = chroma.CrystalVault(os.path.join(tempfile.mkdtemp(), "v.jsonl"))
        run_ = chroma.RunLifecycle(e, vault, run_id="verify")
        for _ in range(10):
            out = e.execute("lifecycle verify item")
            r = run_.activate("k", out["receipt"]["receipt_hash"], content="x")
        c = run_.finish()
        return bool(r["promoted"] and c["metadata"]["spine_length"] >= 1
                    and vault.count == 2 and len(e.speedlight._cache) == 0)
    run("two-tier law: promote+compress+crystal-only", _lifecycle_check)

    width = max(len(n) for n, _, _ in checks)
    fails = 0
    for name, ok, note in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {name.ljust(width)} {note}")
        fails += 0 if ok else 1
    print(f"cqecmplx-verify: {len(checks) - fails}/{len(checks)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
