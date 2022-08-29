from __future__ import annotations
from typing import TypeVar, TypeVarTuple, Generic, NewType
from typing import Literal as L

DType = TypeVar('DType')
Shape = TypeVarTuple('Shape')


class Array(Generic[DType, *Shape]):

    def __abs__(self) -> Array[DType, *Shape]: ...

    def __add__(self, other: Array[DType, *Shape]) -> Array[DType, *Shape]: ...


Height = NewType('Height', int)
Width = NewType('Width', int)

x: Array[float, Height, Width] = Array()
y: Array[float, L[480], L[640]] = Array()

