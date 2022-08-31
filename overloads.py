from __future__ import annotations
from typing import TypeVar, Generic, overload

from array_declaration import Shape

Axis1 = TypeVar('Axis1')
Axis2 = TypeVar('Axis2')
Axis3 = TypeVar('Axis3')


class Array(Generic[*Shape]):
    @overload
    def transpose(
            self: Array[Axis1, Axis2]
    ) -> Array[Axis2, Axis1]: ...

    @overload
    def transpose(
            self: Array[Axis1, Axis2, Axis3]
    ) -> Array[Axis3, Axis2, Axis1]: ...


x: Array[Axis1, Axis2] = Array()
expr = x.transpose()

y: Array[Axis1, Axis2, Axis3] = Array()
expr = y.transpose()
