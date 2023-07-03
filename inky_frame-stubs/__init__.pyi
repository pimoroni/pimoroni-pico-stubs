from __future__ import annotations

import pcf85063a
from machine import I2C, Pin
from micropython import const
from pimoroni import PWMLED, ShiftRegister

BLACK = const(0)
WHITE = const(1)

GREEN = const(2)
BLUE = const(3)
RED = const(4)
YELLOW = const(5)
ORANGE = const(6)
TAUPE = const(7)

SR_CLOCK = const(8)
SR_LATCH = const(9)
SR_OUT = const(10)

LED_A = const(11)
LED_B = const(12)
LED_C = const(13)
LED_D = const(14)
LED_E = const(15)

LED_BUSY = const(6)
LED_WIFI = const(7)

HOLD_VSYS_EN = const(2)

RTC_ALARM = const(2)
EXTERNAL_TRIGGER = const(1)
EINK_BUSY = const(0)

SHIFT_STATE: int

i2c: I2C
rtc: pcf85063a.PCF85063A

vsys: Pin


def woken_by_rtc() -> bool:
    ...


def woken_by_ext_trigger() -> bool:
    ...


def woken_by_button() -> bool:
    ...


def pico_rtc_to_pcf():
    ...


def pcf_to_pico_rtc() -> bool:
    ...


def sleep_for(minutes: int):
    ...


def turn_off():
    ...


def set_time():
    ...


class Button:
    def __init__(self, sr: ShiftRegister, idx: int, led: int, debounce=50):
        self.sr = sr
        self.startup_state: bool
        self.led: PWMLED

    def led_on(self):
        ...

    def led_off(self):
        ...

    def led_brightness(self, brightness: float):
        ...

    def led_toggle(self):
        ...

    def read(self) -> bool:
        ...

    @property
    def is_pressed(self) -> bool:
        ...


sr: ShiftRegister

button_a: Button
button_b: Button
button_c: Button
button_d: Button
button_e: Button

led_busy: PWMLED
led_wifi: PWMLED
