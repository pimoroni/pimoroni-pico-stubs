import machine


def get_number(pin: machine.Pin) -> int:
    ...


def get_chip(pin: machine.Pin) -> int:
    ...


def change_output_mask(chip: int, mask: int, state: int) -> None:
    ...


def change_config_mask(chip: int, mask: int, state: int) -> None:
    ...


def change_polarity_mask(chip: int, mask: int, state: int) -> None:
    ...


def read_input(chip: int) -> int:
    ...


def read_output(chip: int) -> int:
    ...


def read_config(chip: int) -> int:
    ...


def read_polarity(chip: int) -> int:
    ...


def stored_output(chip: int) -> int:
    ...


def stored_config(chip: int) -> int:
    ...


def stored_polarity(chip: int) -> int:
    ...
