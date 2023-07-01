from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

class BreakoutSGP30:
    ECO2    = 0
    TVOC    = 1
    H2      = 0
    ETHANOL = 1

    def __init__(self, i2c: PimoroniI2C):
        ...

    def retrieve_unique_id(self) -> bool:
        ...

    def get_unique_id(self) -> tuple[int, int, int]:
        ...

    def start_measurement(self, wait_for_setup: bool) -> None:
        ...

    def get_air_quality(self) -> tuple[int, int]|None:
        ...

    def get_air_quality_raw(self) -> tuple[int, int]|None:
        ...

    def soft_reset(self) -> None:
        ...

    def get_baseline(self) -> tuple[int, int]|None:
        ...

    def set_baseline(self, eco2: int, tvoc: int) -> None:
        ...

    def set_humidity(self, absolute_humidity: int) -> None:
        ...
