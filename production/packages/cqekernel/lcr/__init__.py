"""
LCR windows: the channel-level resolution surface.

The LCR window machine is the kernel's primary surface. Every
observation produces at most ceil(N/4) 2x2 windows, ceil(N/16)
4x4 windows, and (at most) one 8x8 window — the same fixed
small channel budget regardless of input size.
"""

from ..carrier.lcr import LocalGluon, admit
from .windows import (
    WindowSize,
    WINDOW_BITS,
    LCRWindow,
    LCRChannel,
    LCRGluon,
    envelope_into_windows,
    gluon_stream_from_bits,
    resolve_channel,
)

__all__ = [
    "WindowSize",
    "WINDOW_BITS",
    "LCRWindow",
    "LCRChannel",
    "LCRGluon",
    "LocalGluon",
    "admit",
    "envelope_into_windows",
    "gluon_stream_from_bits",
    "resolve_channel",
]