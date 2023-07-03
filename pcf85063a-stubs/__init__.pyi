from __future__ import annotations

from typing import overload

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/pcf85063a/pcf85063a.hpp#L17
__PARAM_UNUSED = -1
__TIMER_TICK_4096HZ       = 0b00,
__TIMER_TICK_64HZ         = 0b01,
__TIMER_TICK_1HZ          = 0b10,
__TIMER_TICK_1_OVER_60HZ  = 0b11

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

class PCF85063A:
    CLOCK_OUT_32768HZ = 0
    CLOCK_OUT_16384HZ = 1
    CLOCK_OUT_8192HZ = 2
    CLOCK_OUT_4096HZ = 3
    CLOCK_OUT_2048HZ = 4
    CLOCK_OUT_1024HZ = 5
    CLOCK_OUT_1HZ = 6
    CLOCK_OUT_OFF = 7
    TIMER_TICK_4096HZ = 0b00
    TIMER_TICK_64HZ = 0b01
    TIMER_TICK_1HZ = 0b10
    TIMER_TICK_1_OVER_60HZ = 0b11

    def __init__(self, i2c: PimoroniI2C, interrupt=__PIN_UNUSED):
        ...

    def reset(self) -> None:
        ...

    @overload
    def datetime(self) -> tuple[int, int, int, int, int, int, int]:
        ...

    @overload
    def datetime(self, time:list[int]|tuple[int, int, int, int, int, int, int]) -> None:
        ...

    def set_alarm(self, second: int=__PARAM_UNUSED, minute: int=__PARAM_UNUSED, hour: int=__PARAM_UNUSED, day: int=__PARAM_UNUSED) -> None:
        ...

    def set_weekday_alarm(self, second: int=__PARAM_UNUSED, minute: int=__PARAM_UNUSED, hour: int=__PARAM_UNUSED, day: int=__PARAM_UNUSED) -> None:
        ...

    def enable_alarm_interrupt(self, enable: bool) -> None:
        ...

    def read_alarm_flag(self) -> bool:
        ...

    def clear_alarm_flag(self) -> None:
        ...

    def unset_alarm(self) -> None:
        ...

    def set_timer(self, ticks: int, ttp=__TIMER_TICK_1HZ) -> None:
        ...

    def enable_timer_interrupt(self, enable: bool, flag_only=False) -> None:
        ...

    def read_timer_flag(self) -> bool:
        ...

    def clear_timer_flag(self) -> None:
        ...

    def unset_timer(self) -> None:
        ...

    def set_clock_output(self, co: int) -> None:
        ...

    def set_byte(self, v: int) -> None:
        ...

    def get_byte(self) -> int:
        ...
