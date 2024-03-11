from __future__ import annotations

import hub75
import picographics
from pimoroni_i2c import PimoroniI2C

# Index Constants
SWITCH_A = 0
SWITCH_B = 1
SWITCH_BOOT = 1

DISPLAY_INTERSTATE75_32X32 = picographics.DISPLAY_INTERSTATE75_32X32
DISPLAY_INTERSTATE75_64X32 = picographics.DISPLAY_INTERSTATE75_64X32
DISPLAY_INTERSTATE75_96X32 = picographics.DISPLAY_INTERSTATE75_96X32
DISPLAY_INTERSTATE75_128X32 = picographics.DISPLAY_INTERSTATE75_128X32
DISPLAY_INTERSTATE75_64X64 = picographics.DISPLAY_INTERSTATE75_64X64
DISPLAY_INTERSTATE75_128X64 = picographics.DISPLAY_INTERSTATE75_128X64
DISPLAY_INTERSTATE75_192X64 = picographics.DISPLAY_INTERSTATE75_192X64
DISPLAY_INTERSTATE75_256X64 = picographics.DISPLAY_INTERSTATE75_256X64


class Interstate75:
    I2C_SDA_PIN = 20
    I2C_SCL_PIN = 21
    SWITCH_PINS = (14, 23)
    SWITCH_PINS_W = (14, 15)
    LED_R_PIN = 16
    LED_G_PIN = 17
    LED_B_PIN = 18

    # Display Types
    DISPLAY_INTERSTATE75_32X32 = picographics.DISPLAY_INTERSTATE75_32X32
    DISPLAY_INTERSTATE75_64X32 = picographics.DISPLAY_INTERSTATE75_64X32
    DISPLAY_INTERSTATE75_96X32 = picographics.DISPLAY_INTERSTATE75_96X32
    DISPLAY_INTERSTATE75_128X32 = picographics.DISPLAY_INTERSTATE75_128X32
    DISPLAY_INTERSTATE75_64X64 = picographics.DISPLAY_INTERSTATE75_64X64
    DISPLAY_INTERSTATE75_128X64 = picographics.DISPLAY_INTERSTATE75_128X64
    DISPLAY_INTERSTATE75_192X64 = picographics.DISPLAY_INTERSTATE75_192X64
    DISPLAY_INTERSTATE75_256X64 = picographics.DISPLAY_INTERSTATE75_256X64

    PANEL_GENERIC = hub75.PANEL_GENERIC
    PANEL_FM6126A = hub75.PANEL_FM6126A
    COLOR_ORDER_RGB = hub75.COLOR_ORDER_RGB
    COLOR_ORDER_RBG = hub75.COLOR_ORDER_RBG
    COLOR_ORDER_GRB = hub75.COLOR_ORDER_GRB
    COLOR_ORDER_GBR = hub75.COLOR_ORDER_GBR
    COLOR_ORDER_BRG = hub75.COLOR_ORDER_BRG
    COLOR_ORDER_BGR = hub75.COLOR_ORDER_BGR

    # Count Constants
    NUM_SWITCHES = 2

    def __init__(self, display: int, panel_type=hub75.PANEL_GENERIC, stb_invert=False, color_order=hub75.COLOR_ORDER_RGB):
        self.interstate75w: bool
        self.display: picographics.PicoGraphics
        self.width: int
        self.height: int
        self.hub75: hub75.Hub75
        self.i2c: PimoroniI2C

    def update(self, buffer=None) -> None:
        ...

    def switch_pressed(self, switch: int) -> bool:
        ...

    def set_led(self, r: int, g: int, b: int):
        ...
