from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/ltr559/ltr559.hpp
__DEFAULT_I2C_ADDRESS    = 0x23

class BreakoutLTR559:
    PROXIMITY        = 0
    ALS_0            = 1
    ALS_1            = 2
    INTEGRATION_TIME = 3
    GAIN             = 4
    RATIO            = 5
    LUX              = 6

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS):
        ...

    def part_id(self) -> int:
        ...

    def revision_id(self) -> int:
        ...

    def manufacturer_id(self) -> int:
        ...

    def get_reading(self) -> tuple[int, int, int, int, int, float, float]|None:
        ...

    def interrupts(self, light: bool, proximity: bool) -> None:
        ...

    def proximity_led(self, current: int, duty_cycle: int, pulse_freq: int, num_pulses: int) -> None:
        ...

    def light_control(self, active: bool, gain: int) -> None:
        ...

    def proximity_control(self, active: bool, saturation_indicator: bool) -> None:
        ...

    def light_threshold(self, lower: int, upper: int) -> None:
        ...

    def proximity_threshold(self, lower: int, upper: int) -> None:
        ...

    def light_measurement_rate(self, integration_time: int, rate: int) -> None:
        ...

    def proximity_measurement_rate(self, rate: int) -> None:
        ...

    def proximity_offset(self, offset: int) -> None:
        ...
