from typing import Generic, TypeVarTuple, Tuple, NewType

Shape = TypeVarTuple('Shape')
Height = NewType('Height', int)
Width = NewType('Width', int)


class Array(Generic[*Shape]):

    def __init__(self, shape: Tuple[*Shape]):
        self._shape: Tuple[*Shape] = shape

    def get_shape(self) -> Tuple[*Shape]:
        return self._shape


shape = (Height(480), Width(640))
x: Array[Height, Width] = Array(shape)

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
