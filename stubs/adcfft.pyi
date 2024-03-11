from __future__ import annotations


class ADCFFT:
    """"""
    def __init__(self, channel: int = 0, gpio: int = 26, sample_rate: int = 10000):
        ...

    def update(self):
        ...

    def get_scaled(self, index: int, scale: int) -> int:
        ...
