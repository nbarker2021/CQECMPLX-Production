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

    def _rgb_lcr_check():
        from cqecmplx.engines.pixel import (pixel_planes, planes_pixel,
                                            pixel_gluon, Picture, VideoSynth)
        for rgb in [(0,0,0),(255,255,255),(137,201,77),(255,0,128)]:
            if planes_pixel(pixel_planes(*rgb)) != rgb:
                return False
            if pixel_gluon(*rgb) != pixel_gluon(rgb[2], rgb[1], rgb[0]):
                return False
        r30 = Picture.rule30_texture(48, 27, (255,255,255), (0,0,32), seed=7)
        v1 = VideoSynth(48, 27); v1.add_layer(r30, motion=lambda t: (t, 0))
        v2 = VideoSynth(48, 27); v2.add_layer(r30, motion=lambda t: (t, 0))
        return v1.render(6)["video_hash"] == v2.render(6)["video_hash"]
    run("rgb=lcr: roundtrip+gluon+video determinism", _rgb_lcr_check)

    def _genesis_check():
        from cqecmplx.engines.pixel import Picture, GenesisField
        target = Picture.rule30_texture(48, 27, (250, 180, 60), (8, 8, 30), seed=5)
        g = GenesisField.from_picture(target)
        exact = g.regenerate().content_hash() == target.content_hash()
        d = g.density()["total"]
        cont = g.regenerate(extra_rows=10).height == 37
        return bool(exact and 0.0 <= d <= 1.0 and cont)
    run("genesis: rule90+correction regenerates exactly", _genesis_check)

    width = max(len(n) for n, _, _ in checks)
    fails = 0
    for name, ok, note in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {name.ljust(width)} {note}")
        fails += 0 if ok else 1
    print(f"cqecmplx-verify: {len(checks) - fails}/{len(checks)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
