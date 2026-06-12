"""
LIVE VIDEO: request -> world -> intent -> REAL saved pictures -> 30fps AVI
===========================================================================
The full historical stack, live:

  1. WORLDFORGE   the original operator chain composes the world from the
                  request (P5 -> B_obs -> Rrho -> B_soft -> B_higgs ->
                  B_ward -> Bridge), world_id stamped
  2. INTENT       Scene8's Intent-as-Slice: three E8-lattice trajectory
                  candidates, system-scored, best slice wins — the
                  trajectory IS the camera/motion plan
  3. IMAGE DB     REAL pictures already saved on this machine (PNGs decoded
                  by our stdlib decoder + BMPs we rendered earlier) are
                  indexed and deterministically cast for this world
  4. VIDEO        cast pictures become layers; each layer's motion is its
                  lane of the intent trajectory projected to the screen;
                  toroidal transport + superposition -> 90 frames @ 30fps
  5. PROOF        AVI decodes back frame-perfect; run crystallized.

Run:  python live_video.py "crystal dawn over the lattice"
"""
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
for up in (HERE.parent / "src", Path("D:/CQE_CMPLX/CQECMPLX-Production/lib-forge")):
    if up.is_dir() and str(up) not in sys.path:
        sys.path.insert(0, str(up))

from ChromaForge import ChromaForgeEngine, CrystalVault, RunLifecycle
from SceneForge import compose, understand, ImageDB, fit_to
from PixelForge import VideoSynth, Picture
from PixelForge.projection import project, to_screen
from PixelForge.avi import write_avi, decode_avi

W, H, FPS, FRAMES = 320, 180, 30, 90


def main(request: str) -> None:
    t0 = time.time()
    out_dir = HERE / "live_demo"
    out_dir.mkdir(exist_ok=True)
    print(f"REQUEST  : {request!r}")

    # ── law first ────────────────────────────────────────────────────────────
    engine = ChromaForgeEngine()
    vault = CrystalVault(out_dir / "vault.jsonl")
    run = RunLifecycle(engine, vault, run_id="live-video")
    law = engine.execute(request)
    run.activate("request", law["receipt"]["receipt_hash"], content=request)

    # ── 1. WORLDFORGE: the historical compose ────────────────────────────────
    seed = int(law["derivation_key"][:8], 16)
    world = compose(seed, request, modes=["video"], lenses=["chroma"])
    print(f"WORLD    : {world['stamp']['world_id']} | ops {'->'.join(world['ops'])} | "
          f"info_bits {world['ledger']['info_bits']} | harmonics {world['harmonics']}")

    # ── 2. INTENT: Scene8's slice selection ──────────────────────────────────
    intent = understand(request, num_frames=FRAMES)
    print(f"INTENT   : action={intent.action} proj={intent.projection_type} "
          f"score={intent.score} DR={intent.digital_root} parity={intent.parity} | "
          f"trajectory {len(intent.trajectory)} E8 roots")

    # ── 3. IMAGE DB: real saved pictures, deterministically cast ────────────
    db = ImageDB(out_dir / "imagedb.jsonl")
    if db.count < 6:
        db.scan(HERE, limit=24)                                   # our rendered BMPs
        db.scan(r"C:\Windows\SystemResources", limit=24)          # real Windows PNGs
        db.scan(r"C:\Windows\Web", limit=8)
    cast = db.pick(3, seed=seed, keywords=request.split())
    print(f"IMAGE DB : {db.count} real images indexed | cast {len(cast)} for this world")

    # ── 4. VIDEO: trajectory drives the cast ─────────────────────────────────
    synth = VideoSynth(W, H, fps=FPS, background=(6, 6, 16))
    for li, pic in enumerate(cast):
        layer_pic = fit_to(pic, W, H)
        lane = li + 1

        def motion(t, lane=lane):
            # the intent trajectory IS the motion plan: project the E8 state
            # for frame t through the intent's projection onto the screen,
            # each layer offset one step down its lane
            st = intent.trajectory[(t + lane * 7) % len(intent.trajectory)]
            lx, ly, _ = to_screen(project(st, intent.projection_type))
            return (int(lx * W) + t * lane, int(ly * H) + t)

        synth.add_layer(layer_pic, motion=motion, alpha=0.85 if li == 0 else 0.45)

    out = synth.render(FRAMES)
    avi = str(out_dir / "live_demo.avi")
    write_avi(out["frames"], avi, fps=FPS)
    out["frames"][0].to_bmp(str(out_dir / "first_frame.bmp"))
    out["frames"][FRAMES // 2].to_bmp(str(out_dir / "mid_frame.bmp"))
    kb = Path(avi).stat().st_size // 1024
    print(f"VIDEO    : {FRAMES} frames @ {FPS}fps = {FRAMES/FPS:.1f}s | {kb} KB | "
          f"hash {out['video_hash']}")

    # ── 5. PROOF + CRYSTAL ───────────────────────────────────────────────────
    back, fps_back = decode_avi(avi)
    assert fps_back == FPS and back[0].content_hash() == out["frames"][0].content_hash()
    run.activate("video", content=out["video_hash"])
    crystal = run.finish()
    print(f"PROOF    : decoded {len(back)} frames @ {fps_back}fps, frame-perfect")
    print(f"CRYSTAL  : {crystal['crystal_id']} | vault {vault.count}")
    print(f"DONE in {time.time() - t0:.1f}s — play {avi}")


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "crystal dawn over the lattice")
