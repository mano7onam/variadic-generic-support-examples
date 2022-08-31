from typing import Generic, TypeVarTuple, Tuple, Any

Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    def __init__(self, shape: Tuple[*Ts]):
        ...


def foo(x: Array[int, *Tuple[Any, ...], str]) -> None:
    ...


x: Array[int, list[str], bool, str]
foo(x)

y: Array[int, str]
foo(x)

z: Array[int]
foo(x)  # Error

t: Array[str]
foo(x)  # Error

k: Array[int, int]
foo(x)  # Error
