"""
REQUEST -> DATA -> PIXELS -> PICTURES -> VIDEO @ 30fps
=======================================================
The whole chain, every metric supplied by the system itself:

  1. REQUEST   a text request arrives (any bytes)
  2. DATA      the Binary Boundary Adapter registers it (Event Law:
               computed -> saved -> validated -> receipted)
  3. PIXELS    the system's OWN readings paint the palette:
                 - BBA head/tail Lie-conjugate states -> the two colors
                 - carry density -> the blend ratio
                 - content hash -> the Rule 30 texture seed
               and the raw request bytes are ENCODED as literal pixels
               (a data band: 3 bytes per pixel, length-prefixed)
  4. PICTURES  gradient (color blending) + emission-law texture + data band
  5. VIDEO     90 frames at 30fps; the MOTION comes from the superpermutation
               supervisor cursor (each frame's drift = the cursor's digits) —
               the schedule of all enumerations literally drives the movement.
               Toroidal transport conserves every pixel; superposition blends.
  6. PROOF     the AVI decodes back; the data band decodes back to the exact
               request text. data -> pixels -> video -> pixels -> data.
  7. CRYSTAL   the run finishes: receipt chain compressed to its bare spine,
               crystallized to the vault. Only crystals + the .avi survive.

Run:  python request_to_video.py "your request here"
"""
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
for up in (HERE.parent / "src", Path("D:/CQE_CMPLX/CQECMPLX-Production/lib-forge")):
    if up.is_dir() and str(up) not in sys.path:
        sys.path.insert(0, str(up))

from lattice_forge.binary_boundary_adapter import adapt          # the adapter
from ChromaForge import ChromaForgeEngine, CrystalVault, RunLifecycle
from GraphStax import superperm
from PixelForge import Picture, VideoSynth, translate_toroidal
from PixelForge.avi import write_avi, decode_avi

W, H, FPS, FRAMES = 320, 180, 30, 90


# ── 3a. the system paints the palette ────────────────────────────────────────
def state_color(state, bright=220, dim=30):
    """A Lie-conjugate (L,C,R) state -> a color: each wire lights its channel."""
    L, C, R = state
    return (bright if L else dim, bright if C else dim, bright if R else dim)


# ── 3b. data band codec: bytes <-> pixels (3 bytes per pixel, len-prefixed) ──
def encode_band(picture: Picture, data: bytes, rows=4):
    payload = len(data).to_bytes(4, "big") + data
    payload += b"\x00" * ((-len(payload)) % 3)
    i = 0
    for k in range(0, len(payload), 3):
        x, y = i % picture.width, picture.height - rows + (i // picture.width)
        picture.set(x, y, (payload[k], payload[k + 1], payload[k + 2]))
        i += 1
    return picture


def decode_band(picture: Picture, rows=4) -> bytes:
    raw = bytearray()
    for i in range(picture.width * rows):
        x, y = i % picture.width, picture.height - rows + (i // picture.width)
        raw += bytes(picture.get(x, y))
    n = int.from_bytes(raw[:4], "big")
    return bytes(raw[4:4 + n])


def main(request: str) -> None:
    t0 = time.time()
    out_dir = HERE / "request_demo"
    out_dir.mkdir(exist_ok=True)
    print(f"REQUEST  : {request!r}")

    # ── 2. DATA: Event Law — computed, saved, validated, receipted ──────────
    engine = ChromaForgeEngine()
    vault = CrystalVault(out_dir / "vault.jsonl")
    run = RunLifecycle(engine, vault, run_id="request-to-video")
    law = engine.execute(request)                       # BBA inside + receipt
    bba = adapt(request.encode())                       # the adapter readings
    run.activate("request", law["receipt"]["receipt_hash"], content=request)
    print(f"DATA     : receipt {law['receipt']['receipt_hash'][:12]} | "
          f"head {bba['head']} tail {bba['tail']} | "
          f"carry {bba['summary']['carry_density']:.3f} | arc {bba['arc_type']}")

    # ── 3. PIXELS: palette + seed from the system's own metrics ─────────────
    c_head, c_tail = state_color(bba["head"]), state_color(bba["tail"])
    blend_t = 0.25 + 0.5 * bba["summary"]["carry_density"]
    seed = int(law["derivation_key"][:8], 16) if law.get("derivation_key") else 42
    print(f"PIXELS   : palette {c_head}->{c_tail} | blend {blend_t:.2f} | seed {seed & 0xffff}")

    # ── 4. PICTURES: blending + the emission law painting ───────────────────
    sky = Picture.gradient(W, H, c_head, c_tail, horizontal=False)
    lattice = Picture.rule30_texture(W, H, c_tail, (8, 8, 24), seed=seed)
    print(f"PICTURES : sky {sky.content_hash()} | lattice {lattice.content_hash()}")

    # ── 5. VIDEO: the supervisor cursor drives the movement ─────────────────
    cursor = superperm(4)                                # 33-digit schedule
    def sky_motion(t):       # slow horizontal drift, cursor-modulated
        d = int(cursor[t % len(cursor)])
        return (t * 2 + d, 0)
    def lattice_motion(t):   # the schedule literally is the path
        d1 = int(cursor[t % len(cursor)])
        d2 = int(cursor[(t + 1) % len(cursor)])
        return (t * d1 % W, t * d2 % H)

    synth = VideoSynth(W, H, fps=FPS, background=(4, 4, 12))
    synth.add_layer(sky, motion=sky_motion, alpha=0.85)
    synth.add_layer(lattice, motion=lattice_motion, alpha=0.45)
    out = synth.render(FRAMES)

    # stamp the data band onto every frame (static, decodable)
    for pic in out["frames"]:
        encode_band(pic, request.encode())

    avi_path = str(out_dir / "request_demo.avi")
    write_avi(out["frames"], avi_path, fps=FPS)
    out["frames"][0].to_bmp(str(out_dir / "first_frame.bmp"))
    out["frames"][-1].to_bmp(str(out_dir / "last_frame.bmp"))
    size_kb = Path(avi_path).stat().st_size // 1024
    print(f"VIDEO    : {FRAMES} frames @ {FPS}fps = {FRAMES/FPS:.1f}s | "
          f"{avi_path} ({size_kb} KB) | video_hash {out['video_hash']}")

    # ── 6. PROOF: decode the video back to the request ──────────────────────
    decoded_frames, fps_back = decode_avi(avi_path)
    text_back = decode_band(decoded_frames[0]).decode()
    assert fps_back == FPS and text_back == request, "roundtrip failed"
    print(f"PROOF    : AVI decoded ({len(decoded_frames)} frames @ {fps_back}fps) | "
          f"data band -> {text_back!r}  [exact match]")

    # ── 7. CRYSTAL: compress the run to its bare spine ──────────────────────
    run.activate("video", content=out["video_hash"])
    crystal = run.finish()
    print(f"CRYSTAL  : {crystal['crystal_id']} | spine "
          f"{crystal['metadata']['spine_length']} receipts | vault {vault.count} crystals")
    print(f"DONE in {time.time() - t0:.1f}s — open {avi_path} and press play.")


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "dawn over the lattice")
