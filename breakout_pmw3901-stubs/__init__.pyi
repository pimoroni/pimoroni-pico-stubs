from __future__ import annotations

from typing import overload

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED  = 0XFFFFFFFF

# https://github.com/pimoroni/pimoroni-pico/blob/40f0554259a1d5d5a246072c51f70fbcd692a5b2/common/pimoroni_common.hpp#L40
__SPI_DEFAULT_MOSI = 19
__SPI_DEFAULT_MISO = 16
__SPI_DEFAULT_SCK  = 18
__SPI_BG_FRONT_CS  = 17

class BreakoutPMW3901:
    DEGREES_0   = 0x00
    DEGREES_90  = 0x01
    DEGREES_180 = 0x02
    DEGREES_270 = 0x03
    FRAME_SIZE  = 35
    FRAME_BYTES = 1225

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, slot: int):
        ...

    @overload
    def __init__(self, spi: int, cs=__SPI_BG_FRONT_CS, sck=__SPI_DEFAULT_SCK, mosi=__SPI_DEFAULT_MOSI, miso=__SPI_DEFAULT_MISO, interrupt=__PIN_UNUSED):
        ...

    def __del__(self) -> None:
        ...

    def get_id(self) -> int:
        ...

    def get_revision(self) -> int:
        ...

    def set_rotation(self, degrees: int = 0) -> None:
        ...

    def set_orientation(self, invert_x=True, invert_y=True, swap_xy=True) -> None:
        ...

    def get_motion(self, timeout: float|None=None) -> tuple[int, int]:
        ...

    def get_motion_slow(self, timeout: float|None=None) -> tuple[int, int]:
        ...

    def frame_capture(self, buffer: bytearray, timeout: float|None=None) -> int:
        ...
