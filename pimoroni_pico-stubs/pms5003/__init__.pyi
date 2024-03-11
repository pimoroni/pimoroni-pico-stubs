from machine import UART, Pin

__version__: str


PMS5003_SOF: bytearray
PMS5003_CMD_MODE_PASSIVE = b'\xe1\x00\x00'
PMS5003_CMD_MODE_ACTIVE = b'\xe1\x00\x01'
PMS5003_CMD_READ = b'\xe2\x00\x00'
PMS5003_CMD_SLEEP = b'\xe4\x00\x00'
PMS5003_CMD_WAKEUP = b'\xe4\x00\x01'

PMSA003I_I2C_ADDR = 0x12


class ChecksumMismatchError(RuntimeError):
    pass


class FrameLengthError(RuntimeError):
    pass


class ReadTimeoutError(RuntimeError):
    pass


class SerialTimeoutError(RuntimeError):
    pass


class PMS5003Response:
    FRAME_LEN = None
    DATA_LEN = None
    DATA_FMT = None
    CHECKSUM_IDX = None

    @classmethod
    def check_data_len(cls, raw_data_len: int, desc="Data") -> None:
        ...

    def __init__(self, raw_data: bytearray, *, frame_length_bytes: int|None=None):
        self.raw_data: bytearray
        self.data: tuple[int, ...]
        self.checksum: int


class PMS5003CmdResponse(PMS5003Response):
    FRAME_LEN = 8
    DATA_LEN = FRAME_LEN - 4
    DATA_FMT = ">BBH"
    CHECKSUM_IDX = 2

    def __init__(self, raw_data: bytearray, *, frame_length_bytes: int|None=None):
        ...


class PMS5003Data(PMS5003Response):
    FRAME_LEN = 32
    DATA_LEN = FRAME_LEN - 4
    DATA_FMT = ">HHHHHHHHHHHHHH"
    CHECKSUM_IDX = 13

    def __init__(self, raw_data: bytearray, *, frame_length_bytes: int|None=None):
        ...

    def pm_ug_per_m3(self, size: float, atmospheric_environment=False) -> int:
        ...

    def pm_per_1l_air(self, size: float) -> int:
        ...


class PMS5003:
    MAX_RESET_TIME = 20_000
    MAX_RESP_TIME = 5_000
    MIN_CMD_INTERVAL = 0.1

    @staticmethod
    def _build_cmd_frame(cmd_bytes) -> bytearray:
        ...

    def __init__(self, uart: UART, pin_reset: Pin, pin_enable: Pin, mode='active', retries=5):
        ...

    def cmd_mode_passive(self) -> PMS5003CmdResponse|None:
        ...

    def cmd_mode_active(self) -> PMS5003CmdResponse|None:
        ...

    def _reset_input_buffer(self):
        ...

    def reset(self) -> bool:
        ...

    def data_available(self) -> bool:
        ...

    def read(self) -> PMS5003Data|None:
        ...

    def _wait_for_bytes(self, num_bytes: int, timeout=MAX_RESP_TIME):
        ...

    def _read_data(self, response_class=PMS5003Data) -> PMS5003Data:
        ...

    def _cmd_passive_read(self):
        ...
