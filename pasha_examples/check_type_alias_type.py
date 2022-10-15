from typing import Generic, TypeVarTuple, TypeVar
from typing import NewType

Shape = TypeVarTuple("Shape")
Height = NewType("Height", int)
Width = NewType("Width", int)
DType = TypeVar("DType")


class Array(Generic[DType, *Shape]):
    ...


Float32Array = Array[float, *Shape]


def takes_float_array_of_specific_shape(arr: Float32Array[Height, Width]): ...


y: Float32Array[Height] = Array()
takes_float_array_of_specific_shape(y)
