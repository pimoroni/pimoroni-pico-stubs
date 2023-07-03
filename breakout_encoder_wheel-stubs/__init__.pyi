from __future__ import annotations

from typing import overload

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

DEFAULT_IOE_I2C_ADDR = 0x13
DEFAULT_LED_I2C_ADDR = 0x77
ALTERNATE_LED_I2C_ADDR = 0x74
NUM_LEDS = 24
NUM_BUTTONS = 5
NUM_GPIOS = 3
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
CENTRE = 4
GP7 = 7
GP8 = 8
GP9 = 9
GPIOS = (GP7, GP8, GP9)

class BreakoutEncoderWheel:
    def __init__(self, i2c: PimoroniI2C, ioe_address=DEFAULT_IOE_I2C_ADDR, led_address=DEFAULT_LED_I2C_ADDR, interrupt=__PIN_UNUSED):
        ...

    def set_ioe_address(self, address: int) -> None:
        ...

    def get_interrupt_flag(self) -> bool:
        ...

    def clear_interrupt_flag(self) -> None:
        ...

    def pressed(self, button: int) -> bool:
        ...

    def count(self) -> int:
        ...

    def delta(self) -> int:
        ...

    def step(self) -> int:
        ...

    def turn(self) -> int:
        ...

    def zero(self) -> None:
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

    def set_rgb(self, index: int, r: int, g: int, b: int) -> None:
        ...

    def set_hsv(self, index: int, h: float, s=1.0, v=1.0) -> None:
        ...

    def clear(self) -> None:
        ...

    def show(self) -> None:
        ...

    @overload
    def gpio_pin_mode(self, gpio: int) -> int:
        ...

    @overload
    def gpio_pin_mode(self, gpio: int, mode: int) -> None:
        ...

    def gpio_pin_value(self, gpio: int, value: float|None = None, load=True, wait_for_load=False) -> float|int|None:
        ...

    def gpio_pwm_load(self, wait_for_load=True) -> None:
        ...

    def gpio_pwm_frequency(self, frequency: float, load=True, wait_for_load=False) -> int:
        ...
