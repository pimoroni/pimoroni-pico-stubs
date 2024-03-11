from __future__ import annotations

import typing
from typing import Literal, overload

# Displays
DISPLAY_LCD_240X240 = 0
DISPLAY_ROUND_LCD_240X240 = 1
DISPLAY_PICO_DISPLAY = 2
DISPLAY_PICO_DISPLAY_2 = 3
DISPLAY_PICO_EXPLORER = 4
DISPLAY_TUFTY_2040 = 5
DISPLAY_ENVIRO_PLUS = 6
DISPLAY_LCD_160X80 = 7
DISPLAY_I2C_OLED_128X128 = 8
DISPLAY_INKY_PACK = 9
DISPLAY_INKY_FRAME = 10
DISPLAY_INKY_FRAME_4 = 11
DISPLAY_GALACTIC_UNICORN = 12
DISPLAY_GFX_PACK = 13
DISPLAY_INTERSTATE75_32X32 = 14
DISPLAY_INTERSTATE75_64X32 = 15
DISPLAY_INTERSTATE75_96X32 = 16
DISPLAY_INTERSTATE75_128X32 = 17
DISPLAY_INTERSTATE75_64X64 = 18
DISPLAY_INTERSTATE75_128X64 = 19
DISPLAY_INTERSTATE75_192X64 = 20
DISPLAY_INTERSTATE75_256X64 = 21
DISPLAY_INKY_FRAME_7 = 22
DISPLAY_COSMIC_UNICORN = 23
DISPLAY_STELLAR_UNICORN = 24
DISPLAY_UNICORN_PACK = 25
DISPLAY_SCROLL_PACK = 26
DISPLAY_PICO_W_EXPLORER = 27

# Pen Types
PEN_1BIT = 0
PEN_P4 = 3
PEN_P8 = 4
PEN_RGB332 = 5
PEN_RGB565 = 6
PEN_RGB888 = 7


# Utility Functions
def RGB_to_RGB332(r: int, g: int, b: int) -> int:
    """Convert a 24-bit RGB888 colour to 8-bit RGB332."""
    ...


def RGB_to_RGB565(r: int, g: int, b: int) -> int:
    """Convert a 24-bit RGB888 colour to 16-bit RGB565."""
    ...


def RGB332_to_RGB(rgb332: int) -> tuple[int, int, int]:
    """Convert an 8-bit RGB332 colour to 24-bit RGB888."""
    ...


def RGB565_to_RGB(rgb565: int) -> tuple[int, int, int]:
    """Convert a 16-bit RGB565 colour to 24-bit RGB888."""
    ...


@typing.type_check_only
class _IPicoGraphics:
    ...


class PicoGraphics(_IPicoGraphics):
    def __init__(self, display, rotate: int = -1, bus: object = None, buffer: object = None, pen_type: int = -1, extra_pins: tuple | None = None, i2_address: int = -1):
        ...

    def pixel(self, x: int, y: int) -> None:
        ...

    def set_pen(self, pen: int) -> None:
        ...

    def set_thickness(self, thickness: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def update(self) -> None:
        ...

    def partial_update(self, x: int, y: int, w: int, h: int) -> None:
        ...

    def set_update_speed(self, update_speed: int) -> None:
        ...

    def set_clip(self, x: int, y: int, w: int, h: int) -> None:
        ...

    def remove_clip(self) -> None:
        ...

    def pixel_span(self, x: int, y: int, length: int) -> None:
        ...

    def rectangle(self, x: int, y: int, w: int, h: int) -> None:
        ...

    def circle(self, x: int, y: int, radius: int) -> None:
        ...

    def character(self, char: int, x: int, y: int, scale: int = 2, rotation: int = 0, codepage: Literal[194] | Literal[195] = 195) -> None:
        ...

    def text(self, text: str, x: int, y: int, wordwrap: int = 0x7fffffff, scale: float | None = None, angle: int = 0, spacing: int = 1, fixed_width: bool = False, rotation: int = 0) -> None:
        ...

    def measure_text(self, text: str, scale: float | None = None, spacing: int = 1, fixed_width: bool = False) -> int:
        ...

    def polygon(self, *xy: tuple[int, int]) -> None:
        ...

    def triangle(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> None:
        ...

    @overload
    def line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        ...

    @overload
    def line(self, x1: int, y1: int, x2: int, y2: int, thickness: int) -> None:
        ...

    def set_spritesheet(self, spritedata: bytearray) -> None:
        ...

    def load_spritesheet(self, filename: str) -> None:
        ...

    def sprite(self, sprite_x: int, sprite_y: int, x: int, y: int, scale: int = 1, transparent: int = 0) -> None:
        ...

    def create_pen(self, r: int, g: int, b: int) -> int:
        ...

    def create_pen_hsv(self, h: float, s: float, v: float) -> int:
        ...

    def update_pen(self, index: int, r: int, g: int, b: int) -> None:
        ...

    def reset_pen(self, index: int) -> None:
        ...

    def set_palette(self, colors: list[tuple[int, int, int]]) -> None:
        ...

    def set_backlight(self, brightness: float) -> None:
        ...

    def get_bounds(self) -> tuple[int, int]:
        ...

    def set_font(self, font: str | bytearray) -> None:
        ...

    def set_framebuffer(self, buffer: bytearray) -> None:
        ...
