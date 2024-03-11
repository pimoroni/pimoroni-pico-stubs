from __future__ import annotations

from picographics import PicoGraphics
from pimoroni_i2c import PimoroniI2C

# Index Constants
SWITCH_A = 0
SWITCH_B = 1
SWITCH_C = 2
SWITCH_D = 3
SWITCH_E = 4


class GfxPack:
    I2C_SDA_PIN = 4
    I2C_SCL_PIN = 5
    SWITCH_PINS = (12, 13, 14, 15, 22)
    LED_R_PIN = 6
    LED_G_PIN = 7
    LED_B_PIN = 8

    # Count Constants
    NUM_SWITCHES = 5

    def __init__(self):
        self.display: PicoGraphics
        self.i2c: PimoroniI2C

    def switch_pressed(self, switch: int) -> bool:
        ...

    def set_backlight(self, r: int, g: int, b: int, w: int|None=None):
        ...
