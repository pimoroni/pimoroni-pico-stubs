FIXED_HEAP = 0
MICROPYTHON = 1

def alloc_bytes() -> int:
    ...

def alloc_count() -> int:
    ...

def free_count() -> int:
    ...

def set_mode(mode: int) -> int:
    ...

def get_mode() -> int:
    ...
