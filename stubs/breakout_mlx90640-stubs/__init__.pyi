from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

# https://github.com/pimoroni/pimoroni-pico/blob/main/drivers/mlx90640/mlx90640.hpp
__MLX90640_DEFAULT_I2C_ADDRESS = 0x33

class MLX90640:
    def __init__(self, i2c: PimoroniI2C, address=__MLX90640_DEFAULT_I2C_ADDRESS):
        ...

    def setup(self, fps: int) -> None:
        ...

    def get_frame(self) -> list[float]:
        ...
