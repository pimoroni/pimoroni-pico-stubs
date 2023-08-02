from __future__ import annotations

# https://github.com/pimoroni/pimoroni-pico/blob/main/common/pimoroni_common.hpp#L16
__PIN_UNUSED = 0XFFFFFFFF

__SPI_DEFAULT_MOSI = 19
__SPI_DEFAULT_MISO = 16
__SPI_DEFAULT_DC = 16
__SPI_DEFAULT_SCK = 18

__SPI_BG_FRONT_PWM = 20
__SPI_BG_FRONT_CS = 17

__SPI_BG_BACK_PWM = 21
__SPI_BG_BACK_CS = 22

class SPIBus:
    def __init__(self, cs=__SPI_BG_FRONT_CS, dc=__SPI_DEFAULT_MISO, sck=__SPI_DEFAULT_SCK, mosi=__SPI_DEFAULT_MOSI, miso=__PIN_UNUSED, bl=__PIN_UNUSED):
        ...


class ParallelBus:
    def __init__(self, cs=10, dc=11, wr_sck=12, rd_sck=13, d0=14, bl=2):
        ...


def SPISlot(in_: int) -> SPIBus:
    ...
