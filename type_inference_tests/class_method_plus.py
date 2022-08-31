from __future__ import annotations
from typing import TypeVarTuple, Generic, Tuple, TypeVar

T = TypeVar['T']
Ts = TypeVarTuple('Ts')


class A(Generic[T, *Ts]):
    def __init__(self, t: T, *args: *Ts) -> None:
        ...

    def __add__(self, other: A[T, *Ts]) -> A[T, *Ts, T]:
        ...


a = A(1, '', True)
b = A(1, '', True)
expr = a + b
