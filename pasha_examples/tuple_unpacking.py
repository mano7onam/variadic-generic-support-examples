from __future__ import annotations

from typing import TypeVarTuple
from typing import Generic
from typing import NewType
from typing import Any

Shape = TypeVarTuple("Shape")

Height = NewType("Height", int)
Width = NewType("Width", int)
Batch = NewType("Batch", int)
Channels = NewType("Channels", int)


class Array(Generic[*Shape]):
    ...


y: Array[*tuple[Any, ...]] = Array()


def expect_variadic_array(x: Array[Batch, *Shape]) -> None:
    print(x)


expect_variadic_array(y)  # <- False positive


# def expect_precise_array(x: Array[Batch, Height, Width, Channels]) -> None:
#     print(x)
#
#
# expect_precise_array(y)