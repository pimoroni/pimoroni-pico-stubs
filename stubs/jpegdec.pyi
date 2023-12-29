from __future__ import annotations

from picographics import _IPicoGraphics

JPEG_SCALE_FULL = 0
JPEG_SCALE_HALF = 2
JPEG_SCALE_QUARTER = 4
JPEG_SCALE_EIGHTH = 8


class JPEG:
    def __init__(self, picographics: _IPicoGraphics):
        ...

    def __del__(self) -> None:
        ...

    def open_RAM(self, buffer: bytearray) -> None:
        ...

    def open_file(self, filename: str) -> bool:
        ...

    def decode(self, x=0, y=0, scale=0, dither=True) -> bool:
        ...

    def get_width(self) -> int:
        ...

    def get_height(self) -> int:
        ...
