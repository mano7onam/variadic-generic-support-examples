from typing import Callable, Tuple

from array_declaration import Ts


class Process:
    def __init__(
            self,
            target: Callable[[*Ts], None],
            args: Tuple[*Ts],
    ) -> None: ...


def func(arg1: int, arg2: str) -> None: ...


Process(target=func, args=(0, 'foo'))  # Valid
Process(target=func, args=('foo', 0))  # Error
