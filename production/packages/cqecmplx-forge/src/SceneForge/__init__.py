"""
SceneForge — world composition + intent + real-image casting.

The shot/scene layer of the suite, grown from the historical donors:
  worldforge.py  the original operator-chain compose (P5 -> B_obs -> Rrho
                 -> B_soft -> B_higgs -> B_ward -> Bridge), receipt-trailed
  intent.py      Scene8's Intent-as-Slice: prompt -> three E8-lattice
                 trajectory candidates -> system-scored -> best slice wins
  imagedb.py     the saved-pictures database: real PNG/BMP files decoded,
                 hashed, indexed, deterministically cast

Position: WorldForge (world) -> SceneForge (THIS: shots/intent/cast)
          -> PixelForge (pixels/pictures/video) -> the .avi in your player.

Stdlib only.
"""
from SceneForge.worldforge import compose
from SceneForge.intent import (
    Intent, understand, apply_action, nearest_root, E8_ROOTS,
    UNITY, TERNARY, ATTRACTOR, ACTIONS,
)
from SceneForge.imagedb import ImageDB, fit_to

__version__ = "0.1.0"

__all__ = [
    "compose", "Intent", "understand", "apply_action", "nearest_root",
    "E8_ROOTS", "UNITY", "TERNARY", "ATTRACTOR", "ACTIONS",
    "ImageDB", "fit_to",
]
