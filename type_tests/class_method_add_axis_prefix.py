from __future__ import annotations
from typing import Generic, TypeVarTuple, Tuple, NewType, TypeVar

T = TypeVar('T')
Shape = TypeVarTuple('Shape')


class Array(Generic[*Shape]):
    def __init__(self, shape: Tuple[*Shape]):
        self._shape: Tuple[*Shape] = shape

    def add_axis_prefix(self, t: T) -> Array[T, *Shape]: ...


shape = (42, 42)
arr: Array[int, int] = Array(shape)
expr = arr.add_axis_prefix(42)
