from typing import overload


class Channel:
  def __init__(self) -> None:
    ...

  def __del__(self) -> None:
    ...

  def configure(self, waveforms: int | None = None, frequency: int | None = None, volume: float | None = None, attack: float | None = None, decay: float | None = None, sustain: None = None, release: float | None = None, pulse_width: float | None = None) -> None:
    ...

  def restore(self) -> None:
    ...

  @overload
  def waveforms(self) -> int:
    ...

  @overload
  def waveforms(self, value: int) -> None:
    ...

  @overload
  def frequency(self) -> int:
    ...

  @overload
  def frequency(self, value: int) -> None:
    ...

  @overload
  def volume(self) -> float:
    ...

  @overload
  def volume(self, value: float) -> float:
    ...

  @overload
  def attack_duration(self) -> float:
    ...

  @overload
  def attack_duration(self, value: float) -> float:
    ...

  @overload
  def decay_duration(self) -> float:
    ...

  @overload
  def decay_duration(self, value: float) -> None:
    ...

  @overload
  def sustain_level(self) -> float:
    ...

  @overload
  def sustain_level(self, value: float) -> None:
    ...

  @overload
  def release_duration(self) -> float:
    ...

  @overload
  def release_duration(self, value: float) -> None:
    ...

  @overload
  def pulse_width(self) -> float:
    ...

  @overload
  def pulse_width(self, value: float) -> None:
    ...

  def trigger_attack(self) -> None:
    ...

  def trigger_release(self) -> None:
    ...

  def play_tone(self, frequency: int, volume: float | None = None, fade_in: float | None = None, fade_out: float | None = None) -> None:
    ...


class PicoSynth:
  def __init__(self, i2s_data: int = 26, i2s_bclk: int = 27, i2s_lrclk: int = 28, pio: int = 0, sm: int = 0) -> None:
    ...

  def __del__(self) -> None:
    ...

  def set_volume(self, value: float) -> None:
    ...

  def get_volume(self) -> float:
    ...

  def adjust_volume(self, delta: float) -> None:
    ...

  def play_sample(self, data: bytes) -> None:
    ...

  def play(self) -> None:
    ...

  def stop(self) -> None:
    ...

  def channel(self, channel: int) -> None:
    ...
