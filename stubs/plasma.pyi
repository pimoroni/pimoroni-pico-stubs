from __future__ import annotations

COLOR_ORDER_RGB = 0
COLOR_ORDER_RBG = 1
COLOR_ORDER_GRB = 2
COLOR_ORDER_GBR = 3
COLOR_ORDER_BRG = 4
COLOR_ORDER_BGR = 5


class APA102:
    def __init__(self, num_leds: int, pio: int, sm: int, dat: int, clk: int, freq: int = 20_000_000, buffer: object = None):
        """Create a new APA102 (a.k.a. DotStar) driver."""
        ...

    def set_brightness(self, brightness: int):
        """Set the brightness of all APA102 pixels."""
        ...

    def set_rgb(self, index: int, r: int, g: int, b: int) -> None:
        """Set a single pixel at index to an RGB color."""
        ...

    def set_hsv(self, index: int, h: float, s: float = 1.0, v: float = 1.0) -> None:
        """Set a single pixel at index to an HSV color."""
        ...

    def start(self, fps: int = 60) -> None:
        """Start automatic updates at desired framerate."""
        ...

    def get(self, index: int) -> tuple[int, int, int, int]:
        """Get a single pixel's RGBW values."""
        ...

    def clear(self) -> None:
        """Clear all pixels to 0,0,0,0."""
        ...

    def update(self) -> None:
        """Output the pixel values to the hardware."""
        ...


class WS2812:
    def __init__(self, num_leds: int, pio: int, sm: int, dat: int, freq: int = 800000, buffer: object = None, rgbw: bool = False, color_order: int = COLOR_ORDER_GRB):
        """Create a new WS2812 (a.k.a. NeoPixel) driver."""
        ...

    def set_rgb(self, index: int, r: int, g: int, b: int, w: int = 0) -> None:
        """Set a single pixel at index to an RGB color."""
        ...

    def set_hsv(self, index: int, h: float, s: float = 1.0, v: float = 1.0, w: int = 0) -> None:
        """Set a single pixel at index to an HSV color."""
        ...

    def start(self, fps: int = 60) -> None:
        """Start automatic updates at desired framerate."""
        ...

    def get(self, index: int) -> tuple[int, int, int, int]:
        """Get a single pixel's RGB values."""
        ...

    def clear(self) -> None:
        """Clear all pixels to 0,0,0."""
        ...

    def update(self) -> None:
        """Output the pixel values to the hardware."""
        ...
