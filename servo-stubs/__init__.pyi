from __future__ import annotations

from typing import overload

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/servo/servo_state.hpp#L13
__DEFAULT_FREQUENCY = 50.0

ANGULAR = 0x00
LINEAR = 0x01
CONTINUOUS = 0x02

class Calibration:
    def __init__(self, type: int|None=None):
        ...

    def __del__(self) -> None:
        ...

    def apply_blank_pairs(self, size: int) -> None:
        ...

    def apply_two_pairs(self, min_pulse: int, max_pulse: int, min_value: int, max_value: int) -> None:
        ...

    def apply_three_pairs(self, min_pulse: int, mid_pulse: int, max_pulse: int, min_value: int, mid_value: int, max_value: int) -> None:
        ...

    def apply_uniform_pairs(self, size: int, min_pulse: int, max_pulse: int, min_value: int, max_value: int) -> None:
        ...

    def apply_default_pairs(self, type: int) -> None:
        ...

    def size(self) -> int:
        ...

    @overload
    def pair(self, index: int) -> list[float]:
        ...

    @overload
    def pair(self, index: int, pair: list[float]|tuple[float, float]) -> None:
        ...

    @overload
    def pulse(self, index: int) -> float:
        ...

    @overload
    def pulse(self, index: int, pulse: float) -> None:
        ...

    @overload
    def value(self, index: int) -> float:
        ...

    @overload
    def value(self, index: int, value: float) -> None:
        ...

    @overload
    def first(self) -> list[float]:
        ...

    @overload
    def first(self, pair: list[float]|tuple[float, float]) -> None:
        ...

    @overload
    def first_pulse(self) -> float:
        ...

    @overload
    def first_pulse(self, pulse: float) -> None:
        ...

    @overload
    def first_value(self) -> float:
        ...

    @overload
    def first_value(self, value: float) -> None:
        ...

    @overload
    def last(self) -> list[float]:
        ...

    @overload
    def last(self, pair: list[float]|tuple[float, float]) -> None:
        ...

    @overload
    def last_pulse(self) -> float:
        ...

    @overload
    def last_pulse(self, pulse: float) -> None:
        ...

    @overload
    def last_value(self) -> float:
        ...

    @overload
    def last_value(self, value: float) -> None:
        ...

    def has_lower_limit(self) -> bool:
        ...

    def has_upper_limit(self) -> bool:
        ...

    def limit_to_calibration(self, lower: bool, upper: bool) -> None:
        ...

    def value_to_pulse(self, value: float) -> tuple[float, float]:
        ...

    def pulse_to_value(self, pulse: float) -> tuple[float, float]:
        ...



class Servo:
    def __init__(self, pin: int, calibration:int|Calibration=ANGULAR, freq=__DEFAULT_FREQUENCY):
        ...

    def __del__(self) -> None:
        ...

    def pin(self) -> int:
        ...

    def enable(self) -> None:
        ...

    def disable(self) -> None:
        ...

    def is_enabled(self) -> bool:
        ...

    @overload
    def pulse(self) -> float:
        ...

    @overload
    def pulse(self, pulse: float) -> None:
        ...

    @overload
    def value(self) -> float:
        ...

    @overload
    def value(self, value: float) -> None:
        ...

    @overload
    def frequency(self) -> float:
        ...

    @overload
    def frequency(self, freq: float) -> None:
        ...

    def min_value(self) -> float:
        ...

    def mid_value(self) -> float:
        ...

    def max_value(self) -> float:
        ...

    def to_min(self) -> None:
        ...

    def to_mid(self) -> None:
        ...

    def to_max(self) -> None:
        ...

    @overload
    def to_percent(self, in_: float) -> None:
        ...

    @overload
    def to_percent(self, in_: float, in_min: float, in_max: float) -> None:
        ...

    @overload
    def to_percent(self, in_: float, in_min: float, in_max: float, value_min: float, value_max: float) -> None:
        ...

    @overload
    def calibration(self) -> Calibration:
        ...

    @overload
    def calibration(self, calibration: Calibration) -> None:
        ...



class ServoCluster:
    def __init__(self, pio: int, sm: int, pins: int|list[int]|tuple[int, ...], calibration: int|Calibration=ANGULAR, freq=__DEFAULT_FREQUENCY, auto_phase=True):
        ...

    def __del__(self) -> None:
        ...

    def count(self) -> int:
        ...

    def pin(self, servo: int) -> int:
        ...

    def enable(self, servos: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def enable_all(self, load=True) -> None:
        ...

    def disable(self, servos: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def disable_all(self, load=True) -> None:
        ...

    def is_enabled(self, servo: int) -> bool:
        ...

    @overload
    def pulse(self, servo: int) -> float:
        ...

    @overload
    def pulse(self, servos: int|list[int]|tuple[int, ...], pulse: float, load=True) -> None:
        ...

    def all_to_pulse(self, pulse: float, load=True) -> None:
        ...

    @overload
    def value(self, servo: int) -> float:
        ...

    @overload
    def value(self, servos: int|list[int]|tuple[int, ...], value: float, load=True) -> None:
        ...

    def all_to_value(self, value: float, load=True) -> None:
        ...

    @overload
    def phase(self, servo: int) -> float:
        ...

    @overload
    def phase(self, servos: int|list[int]|tuple[int, ...], phase: float, load=True) -> None:
        ...

    def all_to_phase(self, phase: float, load=True) -> None:
        ...

    @overload
    def frequency(self) -> float:
        ...

    @overload
    def frequency(self, freq: float) -> None:
        ...

    def min_value(self, servo: int) -> float:
        ...

    def mid_value(self, servo: int) -> float:
        ...

    def max_value(self, servo: int) -> float:
        ...

    def to_min(self, servos: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def all_to_min(self, load=True) -> None:
        ...

    def to_mid(self, servos: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def all_to_mid(self, load=True) -> None:
        ...

    def to_max(self, servos: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def all_to_max(self, load=True) -> None:
        ...

    @overload
    def to_percent(self, servos: int|list[int]|tuple[int, ...], in_: float, load=True) -> None:
        ...

    @overload
    def to_percent(self, servos: int|list[int]|tuple[int, ...], in_: float, in_min: float, in_max: float, load=True) -> None:
        ...

    @overload
    def to_percent(self, servos: int|list[int]|tuple[int, ...], in_: float, in_min: float, in_max: float, value_min: float, value_max: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, in_min: float, in_max: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, in_min: float, in_max: float, value_min: float, value_max: float, load=True) -> None:
        ...

    @overload
    def calibration(self, servo: int) -> Calibration:
        ...

    @overload
    def calibration(self, servo: int, calibration: Calibration) -> None:
        ...

    def load(self) -> None:
        ...
