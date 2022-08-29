from typing import TypeVarTuple, Generic, NewType

from array_declaration import Array, Height, Width, Batch, Time

x: Array[Height, Width] = Array()

y: Array[Batch, Height, Width] = Array()
z: Array[Time, Batch, Height, Width] = Array()
