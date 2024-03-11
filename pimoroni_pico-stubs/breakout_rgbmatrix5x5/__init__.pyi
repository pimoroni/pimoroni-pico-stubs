from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/libraries/breakout_rgbmatrix5x5/breakout_rgbmatrix5x5.hpp
__DEFAULT_I2C_ADDRESS    = 0x74
__ALTERNATE_I2C_ADDRESS  = 0x77

class BreakoutRGBMatrix5x5:
    WIDTH = 5
    HEIGHT = 5

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS):
        ...

    def set_pixel(self, col: int, row: int, r: int, g: int, b: int) -> None:
        ...

    def update(self) -> None:
        ...

    def clear(self) -> None:
        ...
