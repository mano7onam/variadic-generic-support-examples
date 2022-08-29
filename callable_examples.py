from typing import TypeVar, Callable, Tuple

from array_declaration import Ts

T = TypeVar('T')


def foo(f: Callable[[int, *Ts, T], Tuple[T, *Ts]]):
    ...


def foo1(*args: *Ts) -> None: ...
