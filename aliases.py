from typing import Tuple, Generic, Any, TypeVar

from array_declaration import Ts, Array, Height, Shape, Width
from main import DType

IntTuple = Tuple[int, *Ts]
NamedArray = Tuple[str, Array[*Ts]]

expr = IntTuple[float, bool]  # Equivalent to Tuple[int, float, bool]
expr = NamedArray[Height]  # Equivalent to Tuple[str, Array[Height]]


class Array(Generic[DType, *Shape]):
    ...


Float32Array = Array[float, *Shape]

Array1D = Array[DType, Any]

expr = IntTuple[()]  # Equivalent to Tuple[int]
expr = NamedArray[()]  # Equivalent to Tuple[str, Array[()]]


def takes_float_array_of_any_shape(x: Float32Array): ...


x: Float32Array[Height, Width] = Array()
takes_float_array_of_any_shape(x)  # Valid


def takes_float_array_with_specific_shape(
        y: Float32Array[Height, Width]
): ...


y: Float32Array = Array()
takes_float_array_with_specific_shape(y)  # Valid


T = TypeVar('T')
Foo = Tuple[T, *Ts]

# T bound to str, Ts to Tuple[int]
expr = Foo[str, int]
# T bound to float, Ts to Tuple[()]
expr = Foo[float]
# T bound to Any, Ts to an Tuple[Any, ...]
expr = Foo
