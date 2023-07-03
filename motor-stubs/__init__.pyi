from __future__ import annotations

from typing import overload

from pimoroni import NORMAL_DIR

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/motor/motor_state.hpp#L20
__DEFAULT_SPEED_SCALE = 1.0
__DEFAULT_ZEROPOINT = 0.0
__DEFAULT_DEADZONE = 0.05
__DEFAULT_DECAY_MODE = 1
__DEFAULT_FREQUENCY = 25000.0
__MIN_FREQUENCY = 10.0
__MAX_FREQUENCY = 400000.0
__ZERO_PERCENT = 0.0
__ONEHUNDRED_PERCENT = 1.0

FAST_DECAY = 0x00
SLOW_DECAY = 0x01

class Motor:
    def __init__(self, pins: list[int]|tuple[int,int], direction=NORMAL_DIR, speed_scale=__DEFAULT_SPEED_SCALE, zeropoint=__DEFAULT_ZEROPOINT, deadzone=__DEFAULT_DEADZONE, freq=__DEFAULT_FREQUENCY, mode=__DEFAULT_DECAY_MODE, ph_en_driver=False):
        ...

    def __del__(self) -> None:
        ...

    def pins(self) -> tuple[int, int]:
        ...

    def enable(self) -> None:
        ...

    def disable(self) -> None:
        ...

    def is_enabled(self) -> bool:
        ...

    @overload
    def duty(self) -> float:
        ...

    @overload
    def duty(self, duty: float) -> None:
        ...

    @overload
    def speed(self) -> float:
        ...

    @overload
    def speed(self, speed: float) -> None:
        ...

    @overload
    def frequency(self) -> float:
        ...

    @overload
    def frequency(self, freq: float) -> None:
        ...

    def stop(self) -> None:
        ...

    def coast(self) -> None:
        ...

    def brake(self) -> None:
        ...

    def full_negative(self) -> None:
        ...

    def full_positive(self) -> None:
        ...

    @overload
    def to_percent(self, in_: float) -> None:
        ...

    @overload
    def to_percent(self, in_: float, in_min: float, in_max: float) -> None:
        ...

    @overload
    def to_percent(self, in_: float, in_min: float, in_max: float, speed_min: float, speed_max: float) -> None:
        ...

    @overload
    def direction(self) -> int:
        ...

    @overload
    def direction(self, direction: int) -> None:
        ...

    @overload
    def speed_scale(self) -> float:
        ...

    @overload
    def speed_scale(self, speed_scale: float) -> None:
        ...

    @overload
    def zeropoint(self) -> float:
        ...

    @overload
    def zeropoint(self, zeropoint: float) -> None:
        ...

    @overload
    def deadzone(self) -> float:
        ...

    @overload
    def deadzone(self, deadzone: float) -> None:
        ...

    @overload
    def decay_mode(self) -> int:
        ...

    @overload
    def decay_mode(self, mode: int) -> None:
        ...


class MotorCluster:
    def __init__(self, pio: int, sm: int, pins: list[int]|tuple[int, int]|list[tuple[int, int]], direction=NORMAL_DIR, speed_scale=__DEFAULT_SPEED_SCALE, zeropoint=__DEFAULT_ZEROPOINT, deadzone=__DEFAULT_DEADZONE, freq=__DEFAULT_FREQUENCY, mode=__DEFAULT_DECAY_MODE, auto_phase=True):
        ...

    def count(self) -> int:
        ...

    def pins(self, motor: int) -> tuple[int, int]:
        ...

    def enable(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def enable_all(self, load=True) -> None:
        ...

    def disable(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def disable_all(self, load=True) -> None:
        ...

    def is_enabled(self) -> bool:
        ...

    @overload
    def duty(self, motor: int) -> float:
        ...

    @overload
    def duty(self, motor: int|list[int]|tuple[int, ...], duty: float, load=True) -> None:
        ...

    def all_to_duty(self, duty: float, load=True) -> None:
        ...

    @overload
    def speed(self, motor: int) -> float:
        ...

    @overload
    def speed(self, motor: int|list[int]|tuple[int, ...], speed: float, load=True) -> None:
        ...

    def all_to_speed(self, speed: float, load=True) -> None:
        ...

    @overload
    def phase(self, motor: int) -> float:
        ...

    @overload
    def phase(self, motor: int|list[int]|tuple[int, ...], phase: float, load=True) -> None:
        ...

    def all_to_phase(self, phase: float, load=True) -> None:
        ...

    @overload
    def frequency(self) -> float:
        ...

    @overload
    def frequency(self, freq: float) -> None:
        ...

    def stop(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def stop_all(self, load=True) -> None:
        ...

    def coast(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def coast_all(self, load=True) -> None:
        ...

    def brake(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def brake_all(self, load=True) -> None:
        ...

    def full_negative(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def all_full_negative(self, load=True) -> None:
        ...

    def full_positive(self, motors: int|list[int]|tuple[int, ...], load=True) -> None:
        ...

    def all_full_positive(self, load=True) -> None:
        ...

    @overload
    def to_percent(self, motors: int|list[int]|tuple[int, ...], in_: float, load=True) -> None:
        ...

    @overload
    def to_percent(self, motors: int|list[int]|tuple[int, ...], in_: float, in_min: float, in_max: float, load=True) -> None:
        ...

    @overload
    def to_percent(self, motors: int|list[int]|tuple[int, ...], in_: float, in_min: float, in_max: float, speed_min: float, speed_max: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, in_min: float, in_max: float, load=True) -> None:
        ...

    @overload
    def all_to_percent(self, in_: float, in_min: float, in_max: float, speed_min: float, speed_max: float, load=True) -> None:
        ...

    def load(self) -> None:
        ...

    @overload
    def direction(self, motor: int) -> int:
        ...

    @overload
    def direction(self, motor: int|list[int]|tuple[int, ...], direction: int) -> None:
        ...

    def all_directions(self, direction: int) -> None:
        ...

    @overload
    def speed_scale(self, motor: int) -> float:
        ...

    @overload
    def speed_scale(self, motor: int|list[int]|tuple[int, ...], speed_scale: float) -> None:
        ...

    def all_speed_scales(self, speed_scale: float) -> None:
        ...

    @overload
    def zeropoint(self, motor: int) -> float:
        ...

    @overload
    def zeropoint(self, motor: int|list[int]|tuple[int, ...], zeropoint: float) -> None:
        ...

    def all_zeropoints(self, zeropoint: float) -> None:
        ...

    @overload
    def deadzone(self, motor: int) -> float:
        ...

    @overload
    def deadzone(self, motor: int|list[int]|tuple[int, ...], deadzone: float) -> None:
        ...

    def all_deadzones(self, deadzone: float, load=True) -> None:
        ...

    @overload
    def decay_mode(self, motor: int, load=True) -> float:
        ...

    @overload
    def decay_mode(self, motor: int|list[int]|tuple[int, ...], mode: float, load=True) -> None:
        ...

    def all_decay_modes(self, mode: float, load=True) -> None:
        ...
