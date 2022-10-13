from __future__ import annotations

from typing import Generic, TypeVar, TypeVarTuple

DType = TypeVar('DType')
Shape = TypeVarTuple('Shape')


class Array(Generic[DType, *Shape]):
    def __abs__(self) -> Array[DType, *Shape]:
        ...

