from __future__ import annotations

from typing import TypeVarTuple
from typing import TypeVar
from typing import Generic
from typing import overload

Shape = TypeVarTuple("Shape")
Axis1 = TypeVar("Axis1")
Axis2 = TypeVar("Axis2")
Axis3 = TypeVar("Axis3")


class Array(Generic[*Shape]):
    @overload
    def transpose(self: Array[Axis1, Axis2]) -> Array[Axis2, Axis1]: ...

    @overload
    def transpose(self: Array[Axis1, Axis2, Axis3]) -> Array[Axis3, Axis2, Axis1]: ...

    def transpose(self): ...


a1: Array[Axis1, Axis2] = Array()
a2: Array[Axis1, Axis2, Axis3] = Array()

b1 = a1.transpose()
b2 = a2.transpose()
