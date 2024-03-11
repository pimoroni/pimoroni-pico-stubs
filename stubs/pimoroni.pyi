from __future__ import annotations

from typing import Iterator

from machine import ADC, PWM, Pin

BREAKOUT_GARDEN_I2C_PINS = {"sda": 4, "scl": 5}
PICO_EXPLORER_I2C_PINS = {"sda": 20, "scl": 21}
HEADER_I2C_PINS = {"sda": 20, "scl": 21}
PICOVISION_I2C_PINS = {"sda": 6, "scl": 7}

# Motor and encoder directions
NORMAL_DIR = 0x00
REVERSED_DIR = 0x01

BREAKOUT_GARDEN_SPI_SLOT_FRONT = 0
BREAKOUT_GARDEN_SPI_SLOT_BACK = 1
PICO_EXPLORER_SPI_ONBOARD = 2


class Analog:
    def __init__(self, pin: int, amplifier_gain=1.0, resistor=0.0, offset=0.0):
        self.gain: float
        self.resistor: float
        self.offset: float
        self.pin: ADC

    def read_voltage(self) -> float:
        ...

    def read_current(self) -> float:
        ...


class AnalogMux:
    def __init__(self, addr0: int, addr1: int | None=None, addr2: int | None=None, en: int | None=None, muxed_pin: Pin | None=None):
        self.addr0_pin: Pin
        self.addr1_pin: Pin | None
        self.addr2_pin: Pin | None
        self.en_pin: Pin | None
        self.max_address: int
        self.pulls: list[int | None]
        self.muxed_pin: Pin | None

    def select(self, address: int) -> None:
        ...

    def disable(self) -> None:
        ...

    def configure_pull(self, address: int, pull: int | None=None) -> None:
        ...

    def read(self) -> int:
        ...


class Button:
    def __init__(self, button: int, invert=True, repeat_time=200, hold_time=1000):
        self.invert: bool
        self.repeat_time: int
        self.hold_time: int
        self.pin: Pin
        self.last_state: bool
        self.pressed: bool
        self.pressed_time: int

    def read(self) -> bool:
        ...

    def raw(self) -> bool:
        ...

    @property
    def is_pressed(self) -> bool:
        ...


class RGBLED:
    def __init__(self, r: int, g: int, b: int, invert=True):
        self.invert: bool
        self.led_r: PWM
        self.led_g: PWM
        self.led_b: PWM

    def set_rgb(self, r: int, g: int, b: int):
        ...


# A simple class for handling Proportional, Integral & Derivative (PID) control calculations
class PID:
    def __init__(self, kp: float, ki: float, kd: float, sample_rate: float):
        self.kp: float
        self.ki: float
        self.kd: float
        self.setpoint: float


    def calculate(self, value: float, value_change: float | None=None) -> float:
        ...


class Buzzer:
    def __init__(self, pin: int):
        self.pwm: PWM

    def set_tone(self, freq: float, duty=0.5) -> bool:
        ...


class ShiftRegister:
    def __init__(self, clk: int, lat: int, dat: int):
        self.clk: Pin
        self.lat: Pin
        self.dat: Pin

    def __iter__(self) -> Iterator[int]:
        ...

    def __getitem__(self, k) -> int:
        ...

    def read(self) -> int:
        ...

    def is_set(self, mask: int) -> bool:
        ...


# A basic wrapper for PWM with regular on/off and toggle functions from Pin
# Intended to be used for driving LEDs with brightness control & compatibility with Pin
class PWMLED:
    def __init__(self, pin: int, invert=False):
        ...

    def brightness(self, brightness: float) -> None:
        ...

    def on(self) -> None:
        ...

    def off(self) -> None:
        ...

    def toggle(self) -> None:
        ...
