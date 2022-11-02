from __future__ import annotations

from typing import Generic
from typing import TypeVar
from typing import TypeVarTuple

Shape = TypeVarTuple("Shape")
T = TypeVar("T")
T1 = TypeVar("T1")


class Array(Generic[*Shape]):
    ...


y: Array[int, *tuple[float, ...], int, str] = Array()


def expect_variadic_array(x: Array[int, T, *Shape, T1]) -> Array[*Shape, T, T1]:
    ...


expr = expect_variadic_array(y)
