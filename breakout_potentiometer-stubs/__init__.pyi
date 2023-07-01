from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/libraries/breakout_potentiometer/breakout_potentiometer.hpp
__DEFAULT_I2C_ADDRESS  = 0x0E


class BreakoutPotentiometer:
    DIRECTION_CW = 1
    DIRECTION_CCW = 0

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED):
        ...

    def set_address(self, address: int) -> None:
        ...

    def get_adc_vref(self) -> float:
        ...

    def set_adc_vref(self, vref: float) -> None:
        ...

    def get_direction(self) -> bool:
        ...

    def set_direction(self, clockwise: bool) -> None:
        ...

    def set_brightness(self, brightness: float) -> None:
        ...

    def set_led(self, r: int, g: int, b: int) -> None:
        ...

    def read(self) -> float:
        ...

    def read_raw(self) -> int:
        ...
