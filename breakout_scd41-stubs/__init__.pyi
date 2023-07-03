from __future__ import annotations

from pimoroni_i2c import PimoroniI2C

def init(i2c: PimoroniI2C) -> None:
    ...

def start() -> None:
    ...

def stop() -> None:
    ...

def measure() -> tuple[float, float, float]:
    ...

def ready() -> bool:
    ...

def set_temperature_offset(offset: float) -> None:
    ...

def get_temperature_offset() -> int:
    ...

def set_sensor_altitude(altitude: int) -> None:
    ...

def set_ambient_pressure(pressure: int) -> None:
    ...
