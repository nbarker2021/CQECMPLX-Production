"""
PixelForge — pixel layer of the Forge suite (surfaces, ink, projection, frames).

Position in the suite:
  WorldForge  -> world state
  SceneForge  -> shot / scene graph            (grown as we work)
  PixelForge  -> THIS: surfaces, input, pixels, frames
  GVS/Viewer  -> generative video + witness probes

What it prebuilds (so future needs need no model change):
  - STYLUS / TOUCH / POINTER: one normalized sample model with pressure+tilt
    carried end-to-end now (InkEngine); strokes are logical-space, replayable,
    canonical-byte serializable (Event Law / BBA doorway).
  - VARIABLE / ADAPTIVE RESOLUTION: Surface logical space [0,1]^2 with
    physical descriptors; resize/rotate are events; every surface snaps to
    an MDHG resolution rung (grain..universe).
  - PIXEL -> VIDEO: E8 projection lookup tables (donor renderer strip),
    Frame / FrameStream with DR/parity/entropy governance and the
    deterministic e8lossless artifact form.

Kernel law compliance: every record this engine emits (surface descriptor,
stroke, frame, stream artifact) is canonical-serializable so the host kernel
can run it through compute->save->validate->receipt(2 links)->reuse.

Stdlib only. One instance per context; module singleton `engine` provided.
"""
from typing import Any, Dict, List, Optional

from PixelForge.surface import (
    Surface, SurfaceRegistry, mdhg_level_for, device_class_for,
    _MDHG_LEVELS,
)
from PixelForge.ink import (
    InkEngine, Stroke, PointerSample, simplify,
    POINTER_KINDS, DEFAULT_TOLERANCE,
)
from PixelForge.projection import (
    PROJECTIONS, PROJECTION_NAMES,
    project, to_screen, project_state,
    digital_root, parity, entropy,
)
from PixelForge.frame import Frame, FrameStream
from PixelForge.rgb import (
    pixel_planes, planes_pixel, pixel_gluon, pixel_emission,
    pixel_carry, blend_rgb, BITS,
)
from PixelForge.picture import Picture
from PixelForge.video import VideoSynth, Layer, translate_toroidal
from PixelForge.avi import write_avi, decode_avi
from PixelForge.paint import (paint, chart_numbering, anneal_numbering,
                              carry_numbering, CHART_PALETTE,
                              CARRY_PALETTE, ANNEAL_PALETTE, VOA_PALETTE,
                              DR_PALETTE)


class PixelForgeEngine:
    """Composite: surfaces + ink + projection + frame streams, one context."""

    def __init__(self, ink_tolerance: float = DEFAULT_TOLERANCE):
        self.surfaces = SurfaceRegistry()
        self.ink = InkEngine(tolerance=ink_tolerance)
        self._streams: Dict[str, FrameStream] = {}

    # ── surfaces ─────────────────────────────────────────────────────────────
    def register_surface(self, width: int, height: int, dpr: float = 1.0,
                         kind: str = "screen", surface_id: Optional[str] = None,
                         input_caps: Optional[Dict[str, bool]] = None,
                         metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        s = self.surfaces.register(width, height, dpr, kind, surface_id,
                                   input_caps, metadata)
        return s.descriptor()

    def resize_surface(self, surface_id: str, width: int, height: int,
                       dpr: Optional[float] = None) -> Optional[Dict[str, Any]]:
        s = self.surfaces.resize(surface_id, width, height, dpr)
        return s.descriptor() if s else None

    # ── ink (bulk ingest path for HTTP kernels) ──────────────────────────────
    def ingest_stroke(self, surface_id: str, points: List[Dict[str, Any]],
                      kind: str = "pen", color: str = "#e8eaed",
                      target: Optional[str] = None) -> Optional[Dict[str, Any]]:
        s = self.surfaces.get(surface_id)
        if s is None:
            return None
        return self.ink.ingest(s, points, kind=kind, color=color, target=target)

    # ── frame streams ────────────────────────────────────────────────────────
    def new_stream(self, fps: float = 30.0, projection: str = "standard",
                   parity_rule: str = "free") -> str:
        fs = FrameStream(fps=fps, projection=projection, parity_rule=parity_rule)
        self._streams[fs.stream_id] = fs
        return fs.stream_id

    def stream(self, stream_id: str) -> Optional[FrameStream]:
        return self._streams.get(stream_id)

    # ── status ───────────────────────────────────────────────────────────────
    def status(self) -> Dict[str, Any]:
        return {
            "surfaces": self.surfaces.stats(),
            "ink": self.ink.stats(),
            "streams": {sid: fs.stats() for sid, fs in self._streams.items()},
            "projections": list(PROJECTION_NAMES),
        }


engine = PixelForgeEngine()

__version__ = "0.1.0"

__all__ = [
    "PixelForgeEngine", "engine",
    # surfaces
    "Surface", "SurfaceRegistry", "mdhg_level_for", "device_class_for",
    # ink
    "InkEngine", "Stroke", "PointerSample", "simplify",
    "POINTER_KINDS", "DEFAULT_TOLERANCE",
    # projection
    "PROJECTIONS", "PROJECTION_NAMES", "project", "to_screen",
    "project_state", "digital_root", "parity", "entropy",
    # frames
    "Frame", "FrameStream",
    # rgb = lcr (pixel as ribbon)
    "pixel_planes", "planes_pixel", "pixel_gluon", "pixel_emission",
    "pixel_carry", "blend_rgb", "BITS",
    # pictures + video
    "Picture", "VideoSynth", "Layer", "translate_toroidal",
    "write_avi", "decode_avi",
    # paint-by-numbers machine
    "paint", "chart_numbering", "anneal_numbering", "carry_numbering",
    "CHART_PALETTE", "CARRY_PALETTE", "ANNEAL_PALETTE", "VOA_PALETTE",
    "DR_PALETTE",
]
