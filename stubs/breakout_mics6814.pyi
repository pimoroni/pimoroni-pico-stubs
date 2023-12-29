from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/libraries/breakout_mics6814/breakout_mics6814.hpp
__DEFAULT_I2C_ADDRESS  = 0x19
__PIN_UNUSED  = 0XFFFFFFFF

class BreakoutMICS6814:
    REF = 0
    REDUCING = 1
    NH3 = 2
    OXIDISING = 3

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED) -> None:
        ...

    def set_address(self, address: int) -> None:
        ...

    def get_adc_vref(self) -> float:
        ...

    def set_adc_vref(self, vref: float) -> None:
        ...

    def set_brightness(self, brightness: float) -> None:
        ...

    def set_led(self, r: int, g: int, b: int) -> None:
        ...

    def set_heater(self, on: bool) -> None:
        ...

    def disable_heater(self) -> None:
        ...

    def get_raw_ref(self) -> float:
        ...

    def get_raw_red(self) -> float:
        ...

    def get_raw_nh3(self) -> float:
        ...

    def get_raw_oxd(self) -> float:
        ...

    def read_all(self) -> tuple[float, float, float, float]:
        ...

    def read_ref(self) -> float:
        ...

    def read_reducing(self) -> float:
        ...

    def read_nh3(self) -> float:
        ...

    def read_oxidising(self) -> float:
        ...
