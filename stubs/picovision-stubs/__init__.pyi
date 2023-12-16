from __future__ import annotations

from typing import Literal, overload

from picographics import _IPicoGraphics
from pimoroni_i2c import PimoroniI2C

# PicoGraphicsPenType
PEN_RGB888 = 9
PEN_RGB555 = 10
PEN_P5 = 11

BLEND_TARGET = 0
BLEND_FIXED = 1

SPRITE_OVERWRITE = 0
SPRITE_UNDER = 1
SPRITE_OVER = 2
SPRITE_BLEND_UNDER = 3
SPRITE_BLEND_OVER = 4

WIDESCREEN = True
WIDESCREEN = False


class PicoVision(_IPicoGraphics):
    def __init__(self, pen_type: int = PEN_RGB888, width: int = 320, height: int = 240, frame_width: int = -1, frame_height: int = -1):
        ...

    def pixel(self, x: int, y: int) -> None:
        ...

    def set_pen(self, pen: int) -> None:
        ...

    def set_thickness(self, thickness: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def set_bg(self, pen: int) -> None:
        ...

    def set_blend_mode(self, pen: int) -> None:
        ...

    def set_depth(self, depth: int) -> None:
        ...

    def set_scroll_group_offset(self, scroll_group: int = 1, x: int | None = 0, y: int | None = 0, wrap_x: int | None = 0, wrap_y: int | None = 0, wrap_x_to: int | None = 0, wrap_y_to: int | None = 0) -> None:
        ...

    def set_scroll_group_for_lines(self, scroll_index: int, min_y: int, max_y: int) -> None:
        ...

    def update(self) -> None:
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

    def load_sprite(self, filename: str | bytes, index: int = -1, source: tuple[int, int, int, int] | None = None) -> bool:
        ...

    def display_sprite(self, slot: int, sprite_index: int, x: int, y: int, blend_mode: int = 1, v_scale: int = 1) -> None:
        ...

    def clear_sprite(self, slot: int) -> None:
        ...

    def tilemap(self, tilemap: bytes, bounds: tuple[int, int, int, int], tile_data: tuple[int, int, bytes]) -> None:
        ...

    def load_animation(self, slot: int, data: str | tuple[int, int, bytes], frame_size: tuple[int, int], source: tuple[int, int, int, int] | None = None) -> list[int]:
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

    def set_remote_palette(self, index: int) -> None:
        ...

    def set_local_palette(self, index: int) -> None:
        ...

    def get_bounds(self) -> tuple[int, int]:
        ...

    def set_font(self, font: str | bytearray) -> None:
        ...

    def get_i2c(self) -> PimoroniI2C:
        ...

    def is_button_x_pressed(self) -> bool:
        ...

    def is_button_a_pressed(self) -> bool:
        ...

    def get_gpu_io_value(self, pin: int) -> bool:
        ...

    def set_gpu_io_value(self, pin: int, value: bool) -> None:
        ...

    def set_gpu_io_output_enable(self, pin: int, enable: bool) -> None:
        ...

    def set_gpu_io_pull_up(self, pin: int, enable: bool) -> None:
        ...

    def set_gpu_io_pull_down(self, pin: int, enable: bool) -> None:
        ...

    def set_gpu_io_adc_enable(self, pin: int, enable: bool) -> None:
        ...

    def get_gpu_io_adc_voltage(self, pin: int) -> float:
        ...

    def get_gpu_temp(self) -> float:
        ...

    def loop(self, update: function, render: function) -> None:
        ...
