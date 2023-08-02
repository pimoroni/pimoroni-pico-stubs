from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

class BreakoutICP10125:
    # https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/icp10125/icp10125.hpp
    NORMAL = 0x6825
    LOW_POWER = 0x609C
    LOW_NOISE = 0x70DF
    ULTRA_LOW_NOISE = 0x7866
    STATUS_OK = 0
    STATUS_CRC_FAIL = 1

    def __init__(self, i2c: PimoroniI2C):
        ...

    def measure(self, command=BreakoutICP10125.NORMAL) -> tuple[float, float, int]:
        ...

    def soft_reset(self) -> None:
        ...
