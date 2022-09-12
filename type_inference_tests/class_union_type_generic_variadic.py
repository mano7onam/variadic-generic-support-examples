from __future__ import annotations
from typing import TypeVarTuple, Generic, Tuple, TypeVar

T = TypeVar['T']
Ts = TypeVarTuple('Ts')


class A(Generic[*Ts]):
    def __init__(self, *args: *Ts) -> None:
        ...


x: int | str
expr = A(x, 42)
