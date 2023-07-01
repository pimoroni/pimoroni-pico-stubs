from __future__ import annotations

from typing import NamedTuple

from pimoroni_i2c import PimoroniI2C

# https://github.com/ST-mirror/VL53L5CX_ULD_driver/blob/en/VL53L5CX_ULD_API/inc/vl53l5cx_api.h
__VL53L5CX_DEFAULT_I2C_ADDRESS = 0x52

TARGET_ORDER_CLOSEST = 1
TARGET_ORDER_STRONGEST = 2
RESOLUTION_4X4 = 16
RESOLUTION_8X8 = 64
RANGING_MODE_CONTINUOUS = 1
RANGING_MODE_AUTONOMOUS = 3
POWER_MODE_SLEEP = 0
POWER_MODE_WAKEUP = 1

class __MotionFields(NamedTuple):
    global_indicator_1: int
    global_indicator_2: int
    motion: tuple[int, ...]

class __Data(NamedTuple):
    distance_avg: int
    reflectance_avg: int
    motion_indicator: __MotionFields
    results: int
    distance: tuple[int, ...]
    reflectance: tuple[int, ...]

class VL53L5CX:
    def __init__(self, i2c: PimoroniI2C, address=__VL53L5CX_DEFAULT_I2C_ADDRESS, firmware: bytearray|None=None):
        ...

    def __del__(self) -> None:
        ...

    def start_ranging(self) -> None:
        ...

    def stop_ranging(self) -> None:
        ...

    def enable_motion_indicator(self, value: int) -> None:
        ...

    def set_motion_distance(self, distance_min: int, distance_max: int) -> None:
        ...

    def set_i2c_address(self, value: int) -> None:
        ...

    def set_ranging_mode(self, value: int) -> None:
        ...

    def set_ranging_frequency_hz(self, value: int) -> None:
        ...

    def set_resolution(self, value: int) -> None:
        ...

    def set_integration_time_ms(self, value: int) -> None:
        ...

    def set_sharpener_percent(self, value: int) -> None:
        ...

    def set_target_order(self, value: int) -> None:
        ...

    def set_power_mode(self, value: int) -> None:
        ...

    def data_ready(self) -> bool:
        ...

    def get_data(self) -> __Data:
        ...
