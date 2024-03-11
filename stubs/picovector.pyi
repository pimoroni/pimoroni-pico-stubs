from typing import Iterator

from picographics import _IPicoGraphics

ANTIALIAS_NONE = 0
ANTIALIAS_X4 = 1
ANTIALIAS_X16 = 2


class Polygon():
    def __init__(self, *points: tuple[int, int]):
        ...

    def __del__(self) -> None:
        ...

    def centroid(self) -> tuple[int, int]:
        ...

    def bounds(self) -> tuple[int, int, int, int]:
        ...

    def __iter__(self) -> Iterator[tuple[int, int]]:
        ...


class RegularPolygon(Polygon):
    def __init__(self, x: int, y: int, sides: int, radius: float | None, rotation: float | None = None):
        ...


class Rectangle(Polygon):
    def __init__(self, x: int, y: int, w: int, h: int):
        ...


class PicoVector():
    def __init__(self, graphics: _IPicoGraphics):
        ...

    def set_font(self, font: str, size: int) -> bool:
        ...

    def set_font_size(self, size: int) -> None:
        ...

    def set_antialiasing(self, aa: int) -> None:
        ...

    def text(self, text: str | bytes, x: int, y: int, angle: float | None = None) -> None:
        ...

    def draw(self, *polygons: Polygon) -> None:
        ...

    def rotate(self, polygon: Polygon, angle: float, origin_x: int = 0, origin_y: int = 0) -> None:
        ...

    def translate(self, polygon: Polygon, x: int = 0, y: int = 0) -> None:
        ...
