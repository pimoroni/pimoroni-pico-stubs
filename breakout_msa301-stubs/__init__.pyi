from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/msa301/msa301.hpp
__DEFAULT_I2C_ADDRESS    = 0x26


class BreakoutMSA301:
    X = 0
    Y = 1
    Z = 2

    PORTRAIT           = 0b00
    PORTRAIT_INVERTED  = 0b01
    LANDSCAPE          = 0b10
    LANDSCAPE_INVERTED = 0b11

    NORMAL  = 0b00
    LOW     = 0b01
    SUSPEND = 0b10

    G_2   = 0b00
    G_4   = 0b01
    G_8   = 0b10
    G_16  = 0b11

    BITS_14   = 0b0000
    BITS_12   = 0b0100
    BITS_10   = 0b1000
    BITS_8    = 0b1100

    INVERT_X  = 0b1000
    INVERT_Y  = 0b0100
    INVERT_Z  = 0b0010
    XY_SWAP   = 0b0001

    NONE          = 0,
    ACTIVE        = 0b0000111
    NEW_DATA      = 0b1000000000000
    FREEFALL      = 0b0100000000000
    ORIENTATION   = 0b1000000
    SINGLE_TAP    = 0b0100000
    DOUBLE_TAP    = 0b0010000
    Z_ACTIVE      = 0b0000100
    Y_ACTIVE      = 0b0000010
    X_ACTIVE      = 0b0000001

    LATCH_1MS     = 0b1001
    LATCH_2MS     = 0b1011
    LATCH_25MS    = 0b1100
    LATCH_50MS    = 0b1101
    LATCH_100MS   = 0b1110
    LATCH_250MS   = 0b0001
    LATCH_500MS   = 0b0010
    LATCH_1S      = 0b0011
    LATCH_2S      = 0b0100
    LATCH_4S      = 0b0101
    LATCH_8S      = 0b0110

    def __init__(self, i2c: PimoroniI2C, interrupt=__PIN_UNUSED):
        ...

    def part_id(self) -> int:
        ...

    def get_axis(self) -> float:
        ...

    def get_x_axis(self) -> float:
        ...

    def get_y_axis(self) -> float:
        ...

    def get_z_axis(self) -> float:
        ...

    def get_orientation(self) -> int:
        ...

    def set_power_mode(self, power_mode: int) -> None:
        ...

    def set_range_and_resolution(self, range: int, resolution: int) -> None:
        ...

    def set_axis_polarity(self, polarity: int) -> None:
        ...

    def disable_all_interrupts(self) -> None:
        ...

    def enable_interrupts(self, interrupts: int) -> None:
        ...

    def set_interrupt_latch(self, latch_period: int, reset_latched: bool) -> None:
        ...

    def read_interrupt(self, interrupt: int) -> bool:
        ...
