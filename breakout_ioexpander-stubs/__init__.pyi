from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/ioexpander/ioexpander.hpp
__DEFAULT_I2C_ADDRESS = 0x18

IN = 0b00010
IN_PU = 0b10000
OUT = 0b00001
PWM = 0b00101
ADC = 0b01010

class BreakoutIOExpander:
    PIN_IN      = IN
    PIN_IN_PU   = IN_PU
    PIN_OUT     = OUT
    PIN_OD      = 0b00011
    PIN_PWM     = PWM
    PIN_ADC     = ADC

    NUM_PINS    = 14

    LOW         = 0
    HIGH        = 1

    def __init__(self, i2c: PimoroniI2C, address=__DEFAULT_I2C_ADDRESS, interrupt=0XFFFFFFFF):
        ...

    def get_chip_id(self) -> int:
        ...

    def set_address(self, address) -> None:
        ...

    def get_adc_vref(self) -> float:
        ...

    def set_adc_vref(self, vref: float) -> None:
        ...

    def enable_interrupt_out(self, pin_swap=False) -> None:
        ...

    def disable_interrupt_out(self) -> None:
        ...

    def get_interrupt_flag(self) -> bool:
        ...

    def clear_interrupt_flag(self) -> None:
        ...

    def set_pin_interrupt(self, exp_pin: int, enabled: bool) -> None:
        ...

    def pwm_load(self, wait_for_load=True) -> None:
        ...

    def pwm_loading(self) -> bool:
        ...

    def pwm_clear(self, wait_for_clear=True) -> None:
        ...

    def pwm_clearing(self) -> bool:
        ...

    def set_pwm_control(self, divider: int) -> None:
        ...

    def set_pwm_period(self, value: int, load=True) -> None:
        ...

    def get_mode(self, exp_pin: int) -> int:
        ...

    def set_mode(self, exp_pin: int, mode: int, schmitt_trigger=False, invert=True) -> None:
        ...

    def input(self, exp_pin: int) -> int:
        ...

    def input_as_voltage(self, exp_pin: int) -> int:
        ...

    def output(self, exp_pin: int, value: int, load=True) -> None:
        ...

    def setup_rotary_encoder(self, channel: int, pin_a: int, pin_b: int, pin_c=0, count_microsteps=False) -> None:
        ...

    def read_rotary_encoder(self, channel: int) -> int:
        ...
