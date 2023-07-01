from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/ltp305/ltp305.hpp
__DEFAULT_I2C_ADDRESS      = 0x61
__I2C_ADDRESS_ALTERNATE1   = 0x62
__I2C_ADDRESS_ALTERNATE2   = 0x63
__DEFAULT_BRIGHTNESS       = 64
__MAX_BRIGHTNESS           = 127
__DEFAULT_ON_LEVEL         = 0x7f

class BreakoutDotMatrix:
    WIDTH = 10
    HEIGHT = 7

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS):
        ...

    def set_brightness(self, brightness: float, update=False) -> None:
        ...

    def set_decimal(self, left: bool, right: bool) -> None:
        ...

    def set_pixel(self, col: int, row: int, on: bool) -> None:
        ...

    def set_character(self, col: int, char: str|bytes|int) -> None:
        ...

    def set_image(self, image: bytearray, width: int, height: int, offset_x=0, offset_y=0, wr=False, bg=False, on_level=__DEFAULT_ON_LEVEL, padding=0) -> None:
        ...

    def clear(self) -> None:
        ...

    def show(self) -> None:
        ...
