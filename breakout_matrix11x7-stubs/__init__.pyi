from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/is31fl3731/is31fl3731.hpp
__DEFAULT_I2C_ADDRESS      = 0x74
__I2C_ADDRESS_ALTERNATE1   = 0x75
__I2C_ADDRESS_ALTERNATE2   = 0x76
__I2C_ADDRESS_ALTERNATE3   = 0x77

class BreakoutMatrix11x7:
    # https://github.com/pimoroni/pimoroni-pico/blob/main/micropython/modules/breakout_matrix11x7/breakout_matrix11x7.h
    WIDTH = 11
    HEIGHT = 7

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS):
        ...

    def set_pixel(self, col: int, row: int, val: int) -> None:
        ...

    def update(self) -> None:
        ...

    def clear(self) -> None:
        ...
