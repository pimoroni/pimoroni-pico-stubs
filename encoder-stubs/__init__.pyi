from __future__ import annotations

from typing import NamedTuple, overload

from pimoroni import NORMAL_DIR

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED = 0XFFFFFFFF

MMME_CPR = 12
ROTARY_CPR = 24


class __Capture(NamedTuple):
    count: int
    delta: int
    frequency: float
    revolutions: float
    degrees: float
    radians: float
    revolutions_delta: float
    degrees_delta: float
    radians_delta: float
    revolutions_per_second: float
    revolutions_per_minute: float
    degrees_per_second: float
    radians_per_second: float


class Encoder:
    MMME_CPR   = 12
    ROTARY_CPR = 24

    def __init__(self, pio: int, sm: int, pins: list[int]|tuple[int, int], common_pin=__PIN_UNUSED, direction=NORMAL_DIR, counts_per_rev=Encoder.ROTARY_CPR, count_microsteps=False, freq_divider=1.0):
        ...

    def __del__(self) -> None:
        ...

    def pins(self) -> tuple[int, int]:
        ...

    def common_pin(self) -> int:
        ...

    def state(self) -> tuple[bool, bool]:
        ...

    def count(self) -> int:
        ...

    def delta(self) -> int:
        ...

    def zero(self) -> None:
        ...

    def step(self) -> int:
        ...

    def turn(self) -> int:
        ...

    def revolutions(self) -> float:
        ...

    def degrees(self) -> float:
        ...

    def radians(self) -> float:
        ...

    @overload
    def direction(self) -> int:
        ...

    @overload
    def direction(self, direction: int) -> None:
        ...

    @overload
    def counts_per_rev(self) -> float:
        ...

    @overload
    def counts_per_rev(self, counts_per_rev: float) -> None:
        ...

    def capture(self) -> __Capture:
        ...
