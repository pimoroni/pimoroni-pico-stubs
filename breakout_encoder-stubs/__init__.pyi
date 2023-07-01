from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/libraries/breakout_encoder/breakout_encoder.hpp
__DEFAULT_I2C_ADDRESS  = 0x0F
__DEFAULT_BRIGHTNESS   = 1.0
__DEFAULT_TIMEOUT      = 1

class BreakoutEncoder:
    DIRECTION_CW = 1
    DIRECTION_CCW = 0

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED):
        ...

    def set_address(self, address: int) -> None:
        ...

    def get_interrupt_flag(self) -> bool:
        ...

    def clear_interrupt_flag(self) -> None:
        ...

    def get_direction(self) -> bool:
        ...

    def set_direction(self, clockwise: bool) -> None:
        ...

    def set_brightness(self, brightness: float) -> None:
        ...

    def set_led(self, r: int, g: int, b: int) -> None:
        ...

    def available(self) -> bool:
        ...

    def read(self) -> int:
        ...

    def clear(self) -> None:
        ...
