from __future__ import annotations

from picographics import PicoGraphics

class Channel:
    NOISE = 128
    SQUARE = 64
    SAW = 32
    TRIANGLE = 16
    SINE = 8
    WAVE = 1

    def __init__(self) -> None:
        ...

    def __del__(self) -> None:
        ...

    def configure(self, waveforms: int|None=None, frequency: int|None=None, volume: float|None=None, attack: float|None=None, decay: float|None=None, sustain: float|None=None, release: float|None=None, pulse_width: float|None=None) -> None:
        ...

    def restore(self) -> None:
        ...

    def waveforms(self, waveforms: int) -> None:
        ...

    def frequency(self, freq: int) -> None:
        ...

    def volume(self, volume: float) -> None:
        ...

    def attack_duration(self, attack_ms: float) -> None:
        ...

    def decay_duration(self, decay_ms: float) -> None:
        ...

    def sustain_level(self, sustain: float) -> None:
        ...

    def release_duration(self, release_ms: float) -> None:
        ...

    def pulse_width(self, pulse_width: float) -> None:
        ...

    def trigger_attack(self) -> None:
        ...

    def trigger_release(self) -> None:
        ...

    def play_tone(self, freq: int, volume: float|None=None, fade_in: float|None=None, fade_out: float|None=None) -> None:
        ...

class StellarUnicorn:
    WIDTH = 16
    HEIGHT = 16

    SWITCH_A = 0
    SWITCH_B = 1
    SWITCH_C = 3
    SWITCH_D = 6
    SWITCH_SLEEP = 27
    SWITCH_VOLUME_UP = 7
    SWITCH_VOLUME_DOWN = 8
    SWITCH_BRIGHTNESS_UP = 21
    SWITCH_BRIGHTNESS_DOWN = 26

    NOISE = 128
    SQUARE = 64
    SAW = 32
    TRIANGLE = 16
    SINE = 8
    WAVE = 1

    def set_brightness(self, value: float) -> None:
        ...

    def get_brightness(self) -> float:
        ...

    def adjust_brightness(self, delta: float) -> None:
        ...

    def set_volume(self, value: float) -> None:
        ...

    def get_volume(self) -> float:
        ...

    def adjust_volume(self, delta: float) -> None:
        ...

    def light(self) -> int:
        ...

    def is_pressed(self, button: int) -> bool:
        ...

    def update(self, graphics: PicoGraphics) -> None:
        ...

    def clear(self) -> None:
        ...

    def play_sample(self, data: bytearray):
        ...

    def synth_channel(self, channel):
        ...

    def play_synth(self) -> None:
        ...

    def stop_playing(self) -> None:
        ...
