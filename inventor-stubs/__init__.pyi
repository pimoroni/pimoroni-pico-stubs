from __future__ import annotations

from typing import overload

from encoder import Encoder
from machine import PWM
from motor import Motor
from pimoroni_i2c import PimoroniI2C
from plasma import WS2812
from servo import Servo

# IO Pin Constants
GP0 = 0
GP1 = 1
GP2 = 2

A0 = 26
A1 = 27
A2 = 28

GPIOS = (GP0, GP1, GP2, A0, A1, A2)
ADCS = (A0, A1, A2)


# Index Constants
MOTOR_A = 0
MOTOR_B = 1

SERVO_1 = 0
SERVO_2 = 1
SERVO_3 = 2
SERVO_4 = 3
SERVO_5 = 4
SERVO_6 = 5

LED_GP0 = 0
LED_GP1 = 1
LED_GP2 = 2
LED_A0 = 3
LED_A1 = 4
LED_A2 = 5
LED_SERVO_1 = 6
LED_SERVO_2 = 7
LED_SERVO_3 = 8
LED_SERVO_4 = 9
LED_SERVO_5 = 10
LED_SERVO_6 = 11


# Count Constants
NUM_GPIOS = 6
NUM_ADCS = 3
NUM_MOTORS = 2
NUM_SERVOS = 6
NUM_LEDS = 12


class Inventor2040W():
    AMP_EN_PIN = 3
    I2C_SDA_PIN = 4
    I2C_SCL_PIN = 5
    MOTOR_A_PINS = (6, 7)
    MOTOR_B_PINS = (8, 9)
    ENCODER_A_PINS = (19, 18)
    ENCODER_B_PINS = (17, 16)

    SERVO_1_PIN = 10
    SERVO_2_PIN = 11
    SERVO_3_PIN = 12
    SERVO_4_PIN = 13
    SERVO_5_PIN = 14
    SERVO_6_PIN = 15

    LED_DATA_PIN = 20
    PWM_AUDIO_PIN = 21
    USER_SW_PIN = 22

    AMP_CORRECTION = 4
    DEFAULT_VOLUME = 0.2

    def __init__(self, motor_gear_ratio=50, init_motors=True, init_servos=True):
        self.motors: list[Motor]|None
        self.encoders: list[Encoder]|None
        self.servos: list[Servo]|None
        self.i2c: PimoroniI2C
        self.audio_pwm: PWM
        self.leds: WS2812

    def switch_pressed(self) -> bool:
        ...

    def play_tone(self, frequency: float) -> None:
        ...

    def play_silence(self) -> None:
        ...

    def stop_playing(self) -> None:
        ...

    @overload
    def volume(self) -> float:
        ...

    @overload
    def volume(self, volume: float) -> None:
        ...

    def mute_audio(self) -> None:
        ...

    def unmute_audio(self) -> None:
        ...
