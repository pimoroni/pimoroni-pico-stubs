from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/bme280/bme280.hpp
__DEFAULT_I2C_ADDRESS    = 0x76
__ALTERNATE_I2C_ADDRESS  = 0x77

BME280_FILTER_COEFF_OFF = 0b0
BME280_FILTER_COEFF_2 = 0b0
BME280_FILTER_COEFF_4 = 0b0
BME280_FILTER_COEFF_8 = 0b0
BME280_FILTER_COEFF_16 = 0b0

BME280_NO_OVERSAMPLING = 0b0
BME280_OVERSAMPLING_1X = 0b0
BME280_OVERSAMPLING_2X = 0b0
BME280_OVERSAMPLING_4X = 0b0
BME280_OVERSAMPLING_8X = 0b0
BME280_OVERSAMPLING_16X = 0b0

BME280_SLEEP_MODE = 0b0
BME280_FORCED_MODE = 0b0
BME280_NORMAL_MODE = 0b0

BME280_STANDBY_TIME_0_5_MS = 0b0
BME280_STANDBY_TIME_62_5_MS = 0b0
BME280_STANDBY_TIME_125_MS = 0b0
BME280_STANDBY_TIME_250_MS = 0b0
BME280_STANDBY_TIME_500_MS = 0b0
BME280_STANDBY_TIME_1000_MS = 0b0
BME280_STANDBY_TIME_10_MS = 0b0
BME280_STANDBY_TIME_20_MS = 0b0

class BreakoutBME280:
    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=__PIN_UNUSED):
        ...

    def read(self) -> tuple[float, float, float]:
        ...

    def configure(self, filter = BME280_FILTER_COEFF_2, standby_time = BME280_STANDBY_TIME_0_5_MS, os_pressure = BME280_OVERSAMPLING_16X, os_temp = BME280_OVERSAMPLING_2X, os_humidity = BME280_OVERSAMPLING_1X, mode = BME280_NORMAL_MODE) -> None:
        ...
