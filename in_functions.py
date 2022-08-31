from __future__ import annotations
from typing import Generic, Tuple

from array_declaration import Shape, Width, Height, DType


class Array(Generic[*Shape]):

    def __init__(self, shape: Tuple[*Shape]):
        self._shape: Tuple[*Shape] = shape

    def __abs__(self) -> Array[DType, *Shape]: ...

    def __add__(self, other: Array[DType, *Shape]) -> Array[DType, *Shape]: ...

    def get_shape(self) -> Tuple[*Shape]:
        return self._shape


shape = (Height(480), Width(640))
x: Array[Height, Width] = Array(shape)
y = abs(x)  # Inferred type is Array[Height, Width]
z = x + x   #        ...    is Array[Height, Width]


def pointwise_multiply(
    x: Array[*Shape],
    y: Array[*Shape]
) -> Array[*Shape]: ...


shape = (Height(480),)
x: Array[Height] = Array(shape)
shape = (Width(480),)
y: Array[Width] = Array(shape)
shape = (Height(480), Width(640))
z: Array[Height, Width] = Array(shape)

pointwise_multiply(x, x)  # Valid
pointwise_multiply(x, y)  # Error
pointwise_multiply(x, z)  # Error
