from picographics import PicoGraphics

WIDTH = 17
HEIGHT = 7
BUTTON_A = 0
BUTTON_B = 1
BUTTON_X = 2
BUTTON_Y = 3

class PicoScroll:
    WIDTH = 17
    HEIGHT = 7
    BUTTON_A = BUTTON_A # type: ignore
    BUTTON_B = BUTTON_B # type: ignore
    BUTTON_X = BUTTON_X # type: ignore
    BUTTON_Y = BUTTON_Y # type: ignore

    def __del__(self) -> None:
        ...

    def update(self, graphics: PicoGraphics) -> None:
        ...

    def show(self) -> None:
        ...

    def get_width(self) -> int:
        ...

    def get_height(self) -> int:
        ...

    def set_pixel(self, x: int, y: int, val: int) -> None:
        ...

    def set_pixels(self, buffer: bytearray) -> None:
        ...

    def show_text(self, text: str|bytes, brightness: int, offset: int) -> None:
        ...

    def scroll_text(self, text: str|bytes, brightness: int, delay_ms: int) -> None:
        ...

    def show_bitmap_1d(self, buffer: bytearray, brightness: int, offset: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def is_pressed(self, button: int) -> bool:
        ...
