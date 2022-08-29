from typing import TypeVarTuple, NewType

from array_declaration import Array, Shape, Width, Height

Batch = NewType('Batch', int)
Channels = NewType('Channels', int)


def add_batch_axis(x: Array[*Shape]) -> Array[Batch, *Shape]: ...
def del_batch_axis(x: Array[Batch, *Shape]) -> Array[*Shape]: ...


def add_batch_channels(
  x: Array[*Shape]
) -> Array[Batch, *Shape, Channels]: ...


shape = (Height(10), Width(20))
a: Array[Height, Width] = Array(shape)

# TODO: type evaluation here
b = add_batch_axis(a)      # Inferred type is Array[Batch, Height, Width]
c = del_batch_axis(b)      # Array[Height, Width]
d = add_batch_channels(a)  # Array[Batch, Height, Width, Channels]
