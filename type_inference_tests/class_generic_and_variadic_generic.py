from __future__ import annotations
from typing import TypeVarTuple, Generic, Tuple, TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


class A(Generic[T, *Ts]):
    def __init__(self, t: T, tpl: Tuple[*Ts]) -> None:
        ...


x: int | str
expr = A(x, (x,))
