from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

__DEFAULT_I2C_ADDRESS    = 0x76
__ALTERNATE_I2C_ADDRESS  = 0x77

FILTER_COEFF_OFF = 0x00
FILTER_COEFF_2 = 0x01
FILTER_COEFF_4 = 0x02
FILTER_COEFF_8 = 0x03
FILTER_COEFF_16 = 0x04

NO_OVERSAMPLING = 0x00
OVERSAMPLING_1X = 0x01
OVERSAMPLING_2X = 0x02
OVERSAMPLING_4X = 0x03
OVERSAMPLING_8X = 0x04
OVERSAMPLING_16X = 0x05

SLEEP_MODE = 0x00
FORCED_MODE = 0x01
NORMAL_MODE = 0x03

STANDBY_TIME_0_5_MS = 0x00
STANDBY_TIME_62_5_MS = 0x01
STANDBY_TIME_125_MS = 0x02
STANDBY_TIME_250_MS = 0x03
STANDBY_TIME_500_MS = 0x04
STANDBY_TIME_1000_MS = 0x05
STANDBY_TIME_2000_MS = 0x06
STANDBY_TIME_4000_MS = 0x07


class BreakoutBMP280:
    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED):
        ...

    def read(self) -> tuple[float, float]:
        ...

    def configure(self, filter=FILTER_COEFF_2, standby_time=STANDBY_TIME_0_5_MS, os_pressure=OVERSAMPLING_16X, os_temp=OVERSAMPLING_2X, mode=NORMAL_MODE) -> None:
        ...
