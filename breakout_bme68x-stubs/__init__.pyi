from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/bme68x/bme68x.hpp
__DEFAULT_I2C_ADDRESS    = 0x76
__ALTERNATE_I2C_ADDRESS  = 0x77

FILTER_COEFF_OFF = 0
FILTER_COEFF_1 = 1
FILTER_COEFF_3 = 2
FILTER_COEFF_7 = 3
FILTER_COEFF_15 = 4
FILTER_COEFF_31 = 5
FILTER_COEFF_63 = 6
FILTER_COEFF_127 = 7

NO_OVERSAMPLING = 0
OVERSAMPLING_1X = 1
OVERSAMPLING_2X = 2
OVERSAMPLING_4X = 3
OVERSAMPLING_8X = 4
OVERSAMPLING_16X = 5

STANDBY_TIME_OFF = 8
STANDBY_TIME_0_59_MS = 0
STANDBY_TIME_62_5_MS = 1
STANDBY_TIME_125_MS = 2
STANDBY_TIME_250_MS = 3
STANDBY_TIME_500_MS = 4
STANDBY_TIME_1000_MS = 5
STANDBY_TIME_10_MS = 6
STANDBY_TIME_20_MS = 7

STATUS_GAS_VALID = 0x20
STATUS_HEATER_STABLE = 0x10

I2C_ADDRESS_DEFAULT = __DEFAULT_I2C_ADDRESS
I2C_ADDRESS_ALT = 0x77

class BreakoutBME68X:
    def __init__(self, i2c: PimoroniI2C, address=I2C_ADDRESS_DEFAULT, interrupt=__PIN_UNUSED):
        ...

    def read(self) -> tuple[float, float, float, float, int, int, int]:
        ...

    def configure(self, filter=FILTER_COEFF_3, standby_time=STANDBY_TIME_0_59_MS, os_pressure=OVERSAMPLING_16X, os_temp=OVERSAMPLING_2X, os_humidity=OVERSAMPLING_1X) -> None:
        ...
