from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/bh1745/bh1745.hpp
__DEFAULT_I2C_ADDRESS      = 0x38
__I2C_ADDRESS_ALTERNATE    = 0x39

BH1745_I2C_ADDRESS_DEFAULT = 0b0
BH1745_I2C_ADDRESS_ALTERNATE = 0b0

class BreakoutBH1745:
    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS):
        ...

    def chip_id(self) -> int:
        ...

    def manufacturer_id(self) -> int:
        ...

    def rgbc_raw(self) -> tuple[int, int, int, int]:
        ...

    def rgbc_clamped(self) -> tuple[int, int, int, int]:
        ...

    def rgbc_scaled(self) -> tuple[int, int, int, int]:
        ...

    def threshold(self, lower: int, upper: int) -> None:
        ...

    def measurement_time_ms(self, time: int) -> None:
        ...

    def leds(self, led_state: bool) -> None:
        ...
