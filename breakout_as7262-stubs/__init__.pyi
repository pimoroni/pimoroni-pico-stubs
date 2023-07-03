from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/as7262/as7262.hpp
__DEFAULT_I2C_ADDRESS  = 0x49

class BreakoutAS7262:
    X1 = 0b00
    X3_7 = 0b01
    X16 = 0b10
    X64 = 0b11

    MA12 = 0b00
    MA25 = 0b01
    MA50 = 0b10
    MA100 = 0b11

    MA1 = 0b00
    MA2 = 0b01
    MA4 = 0b10
    MA8 = 0b11

    CONT_YGNV = 0b00
    CONT_ROYG = 0b01
    CONT_ROYGBR = 0b10
    ONESHOT = 0b11

    def __init__(self, i2c: PimoroniI2C, interrupt=__PIN_UNUSED):
        ...

    def reset(self) -> None:
        ...

    def device_type(self) -> int:
        ...

    def hardware_version(self) -> int:
        ...

    def firmware_version(self) -> tuple[int, float, float]:
        ...

    def read(self) -> tuple[float, float, float, float, float, float]:
        ...

    def temperature(self) -> int:
        ...

    def set_gain(self, value: int) -> None:
        ...

    def set_measurement_mode(self, value: int) -> None:
        ...

    def set_indicator_current(self, value: int) -> None:
        ...

    def set_illumination_current(self, value: int) -> None:
        ...

    def set_integration_time(self, value: float) -> None:
        ...

    def set_leds(self, illumination: bool, indicator: bool) -> None:
        ...
