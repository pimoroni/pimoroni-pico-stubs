from __future__ import annotations

from typing import Literal

import machine
from picographics import PicoGraphics

BUTTON_DOWN = 11
BUTTON_A = 12
BUTTON_B = 13
BUTTON_C = 14
BUTTON_UP = 15
BUTTON_USER: Literal[23] | None

BUTTON_MASK = 0b11111 << 11

SYSTEM_VERY_SLOW = 0
SYSTEM_SLOW = 1
SYSTEM_NORMAL = 2
SYSTEM_FAST = 3
SYSTEM_TURBO = 4

UPDATE_NORMAL = 0
UPDATE_MEDIUM = 1
UPDATE_FAST = 2
UPDATE_TURBO = 3

ALARM_RTC: Literal[8] | None
LED: Literal[22] | Literal[25]
ENABLE_3V3 = 10
BUSY = 26

WIDTH = 296
HEIGHT = 128

SYSTEM_FREQS = [
    4000000,
    12000000,
    48000000,
    133000000,
    250000000
]

BUTTONS: dict[int, machine.Pin]

WAKEUP_MASK = 0

enable: machine.Pin


def is_wireless() -> bool:
    ...


def woken_by_rtc() -> bool:
    ...


def woken_by_button() -> bool:
    ...


def pressed_to_wake(button: int) -> bool:
    ...


def reset_pressed_to_wake() -> None:
    ...


def pressed_to_wake_get_once(button: int) -> bool:
    ...


def system_speed(speed: int) -> None:
    ...


def turn_on() -> None:
    ...


def turn_off() -> None:
    ...


def sleep_for(minutes: int) -> None:
    ...


pico_rtc_to_pcf = pcf_to_pico_rtc = sleep_for


class Badger2040(PicoGraphics):
    def __init__(self):
        ...

    def update(self) -> None:
        ...

    def set_update_speed(self, speed: int) -> None:
        ...

    def led(self, brightness: int) -> None:
        ...

    def invert(self, invert: bool) -> None:
        ...

    def thickness(self, thickness: int) -> None:
        ...

    def halt(self) -> None:
        ...

    def keepalive(self) -> None:
        ...

    def pressed(self, button: int) -> None:
        ...

    def pressed_any(self) -> bool:
        ...

    def icon(self, data: bytes, index: int, data_w: int, icon_size: int, x: int, y: int) -> None:
        ...

    def image(self, data: bytes, w: int, h: int, x: int, y: int) -> None:
        ...

    def isconnected(self) -> bool:
        ...

    def ip_address(self) -> tuple[int, int, int, int]:
        ...

    def connect(self) -> None:
        ...
