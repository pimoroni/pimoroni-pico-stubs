from picographics import PicoGraphics

WIDTH = 16
HEIGHT = 7
BUTTON_A = 0
BUTTON_B = 1
BUTTON_X = 2
BUTTON_Y = 3

class PicoUnicorn:
    WIDTH = 16
    HEIGHT = 7
    BUTTON_A = BUTTON_A # type: ignore
    BUTTON_B = BUTTON_B # type: ignore
    BUTTON_X = BUTTON_X # type: ignore
    BUTTON_Y = BUTTON_Y # type: ignore

    def init(self) -> None:
        ...

    def __del__(self) -> None:
        ...

    def update(self, graphics: PicoGraphics) -> None:
        ...

    def set_pixel(self, x: int, y: int, r: int, g: int, b: int) -> None:
        ...

    def set_pixel_value(self, x: int, y: int, val: int) -> None:
        ...

    def clear(self) -> None:
        ...

    def is_pressed(self, button: int) -> bool:
        ...

    def get_width(self) -> int:
        ...

    def get_height(self) -> int:
        ...
