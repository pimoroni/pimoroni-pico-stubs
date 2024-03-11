from __future__ import annotations

from picographics import PicoGraphics

PANEL_GENERIC = 0
PANEL_FM6126A = 1
BUTTON_A = 14
BUTTON_USER = 23
LED_R = 16
LED_G = 17
LED_B = 18
PIN_A0 = 26
PIN_A1 = 27
PIN_A2 = 28
PIN_INT = 19
PIN_SDA = 20
PIN_SCL = 21
CURRENT_SENSE = 29

COLOR_ORDER_RGB = 0x00
COLOR_ORDER_RBG = 0x01
COLOR_ORDER_GRB = 0x02
COLOR_ORDER_GBR = 0x03
COLOR_ORDER_BRG = 0x04
COLOR_ORDER_BGR = 0x05


class Hub75:
    def __init__(self, width: int, height: int, panel_type=PANEL_GENERIC, stb_invert=False, color_order=COLOR_ORDER_RGB):
        ...

    def __del__(self) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def update(self, graphics: PicoGraphics) -> None:
        pass
