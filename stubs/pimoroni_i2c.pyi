from __future__ import annotations

import machine

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp
__I2C_DEFAULT_BAUDRATE = 400000
__I2C_DEFAULT_SDA = 20
__I2C_DEFAULT_SCL = 21
__I2C_DEFAULT_INT = 22

class PimoroniI2C(machine.I2C):
    def __init__(self, sda=__I2C_DEFAULT_SDA, scl=__I2C_DEFAULT_SCL, baudrate=__I2C_DEFAULT_BAUDRATE):
        ...

    def __del__(self) -> None:
        ...
