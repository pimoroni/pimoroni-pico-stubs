from __future__ import annotations

ECC_LOW = 0x0
ECC_MEDIUM = 0x1
ECC_QUARTILE = 0x2
ECC_HIGH = 0x3

MASK_AUTO = -1
MASK_0 = 0
MASK_1 = 1
MASK_2 = 2
MASK_3 = 3
MASK_4 = 4
MASK_5 = 5
MASK_6 = 6
MASK_7 = 7

MODE_NUMERIC = 0x0
MODE_ALPHANUMERIC = 0x2
MODE_BYTE = 0x4
MODE_KANJI = 0x8
MODE_ECI = 0x7

class QRCode:
    def __init__(self, ecc=ECC_MEDIUM, mask=MASK_AUTO):
        ...

    def __del__(self) -> None:
        ...

    def set_text(self, text: str|bytes) -> bool:
        ...

    def get_size(self) -> tuple[int, int]:
        ...

    def get_module(self, x: int, y: int) -> bool:
        ...
