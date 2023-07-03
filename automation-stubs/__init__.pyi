from __future__ import annotations

from typing import overload

from pimoroni_i2c import PimoroniI2C

# IO Pin Constants
GP0 = 0
GP1 = 1
GP2 = 2

# Index Constants
RELAY_1 = 0
RELAY_2 = 1
RELAY_3 = 2

OUTPUT_1 = 0
OUTPUT_2 = 1
OUTPUT_3 = 2

ADC_1 = 0
ADC_2 = 1
ADC_3 = 2

INPUT_1 = 0
INPUT_2 = 1
INPUT_3 = 2
INPUT_4 = 3

SWITCH_A = 0
SWITCH_B = 1


class Automation2040W():
    CONN_LED_PIN = 3
    I2C_SDA_PIN = 4
    I2C_SCL_PIN = 5
    ADC_LED_PINS = (6, 7, 8)
    RELAY_PINS = (9, 10, 11)
    USER_SW_PINS = (12, 13)
    USER_LED_PINS = (14, 15)
    OUTPUT_PINS = (16, 17, 18)
    IN_BUFFERED_PINS = (19, 20, 21, 22)
    ADC_PINS = (26, 27, 28)

    # Count Constants
    NUM_GPIOS = 3
    NUM_RELAYS = 3
    NUM_OUTPUTS = 3
    NUM_ADCS = 3
    NUM_INPUTS = 4
    NUM_SWITCHES = 2

    VOLTAGE_GAIN = 0.06  # 56 / (56 + 820)
    VOLTAGE_OFFSET = -0.06
    MAX_ADC_LED_VOLTAGE = 45.0

    def __init__(self):
        self.i2c: PimoroniI2C

    def conn_led(self, brightness: bool|float) -> None:
        ...

    def switch_pressed(self, switch: int) -> None:
        ...

    def switch_led(self, switch: int, brightness: bool|float) -> None:
        ...

    @overload
    def relay(self, relay: int) -> int:
        ...

    @overload
    def relay(self, relay: int, actuate:bool|int) -> None:
        ...

    def actuate_relay(self, relay: int) -> None:
        ...

    def release_relay(self, relay: int) -> None:
        ...

    @overload
    def output(self, output: int) -> bool:
        ...

    @overload
    def output(self, output: int, value:float|bool) -> None:
        ...

    def output_percent(self, output: int) -> int:
        ...

    def change_output_freq(self, output: int, freq: float) -> None:
        ...

    def read_input(self, input: int) -> int:
        ...

    def read_adc(self, adc: int) -> int:
        ...

    def reset(self) -> None:
        ...


class Automation2040WMini():
    CONN_LED_PIN = 3
    I2C_SDA_PIN = 4
    I2C_SCL_PIN = 5
    ADC_LED_PINS = (6, 7, 8)
    RELAY_PIN = 9
    USER_SW_PINS = (12, 13)
    USER_LED_PINS = (14, 15)
    OUTPUT_PINS = (16, 17)
    IN_BUFFERED_PINS = (19, 20)
    ADC_PINS = (26, 27, 28)

    # Count Constants
    NUM_GPIOS = 3
    NUM_RELAYS = 1
    NUM_OUTPUTS = 2
    NUM_ADCS = 3
    NUM_INPUTS = 2
    NUM_SWITCHES = 2

    VOLTAGE_GAIN = 0.06  # 56 / (56 + 820)
    VOLTAGE_OFFSET = -0.06
    MAX_ADC_LED_VOLTAGE = 45.0

    def __init__(self):
        self.i2c: PimoroniI2C

    def conn_led(self, brightness: bool|float) -> None:
        ...

    def switch_pressed(self, switch) -> bool:
        ...

    def switch_led(self, switch: int, brightness: bool|float) -> None:
        ...

    @overload
    def relay(self) -> int:
        ...

    @overload
    def relay(self, actuate:bool|int) -> None:
        ...

    def actuate_relay(self) -> None:
        ...

    def release_relay(self) -> None:
        ...

    @overload
    def output(self, output: int) -> bool:
        ...

    @overload
    def output(self, output: int, value:float|bool) -> None:
        ...

    def output_percent(self, output: int) -> int:
        ...

    def change_output_freq(self, output: int, freq: float) -> None:
        ...

    def read_input(self, input: int) -> int:
        ...

    def read_adc(self, adc: int) -> int:
        ...

    def reset(self) -> None:
        ...
