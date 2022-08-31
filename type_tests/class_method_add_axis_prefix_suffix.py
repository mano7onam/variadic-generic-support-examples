from __future__ import annotations
from typing import Generic, TypeVarTuple, Tuple, NewType, TypeVar

T1 = TypeVar('T1')
T2 = TypeVar('T2')
T3 = TypeVar('T3')
T4 = TypeVar('T4')
Shape = TypeVarTuple('Shape')


class Array(Generic[*Shape]):
    def __init__(self, shape: Tuple[*Shape]):
        self._shape: Tuple[*Shape] = shape

    def add_axis_prefix_suffix(self, t1: T1, t2: T2, t3: T3, t4: T4) -> Array[T1, T2, *Shape, T3, T4]: ...


shape = (42, '42')
arr: Array[int, str] = Array(shape)
expr = arr.add_axis_prefix_suffix([42], {42: '42'}, '42', True)
