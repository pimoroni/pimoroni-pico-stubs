from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/trackball/trackball.hpp
__DEFAULT_I2C_ADDRESS        = 0x0A
__I2C_ADDRESS_ALTERNATIVE    = 0x0B

class BreakoutTrackball:
    LEFT       = 0
    RIGHT      = 1
    UP         = 2
    DOWN       = 3
    SW_CHANGED = 4
    SW_PRESSED = 5

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED):
        ...

    def change_address(self, address: int) -> None:
        ...

    def enable_interrupt(self, interrupt: bool) -> None:
        ...

    def get_interrupt(self) -> bool:
        ...

    def set_rgbw(self, r: int, g: int, b: int, w: int) -> None:
        ...

    def set_red(self, value: int) -> None:
        ...

    def set_green(self, value: int) -> None:
        ...

    def set_blue(self, value: int) -> None:
        ...

    def set_white(self, value: int) -> None:
        ...

    def read(self) -> tuple[int, int, int, int, int, int]:
        ...
