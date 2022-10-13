import typing_extensions

from typing import TypeVarTuple
from typing import Generic
from typing import Tuple
from typing import NewType

Shape = TypeVarTuple("Shape")

Height = NewType("Height", int)
Width = NewType("Width", int)


class Array(Generic[*Shape]):
    def __init__(self, shape: Tuple[Shape]) -> None:
        self.shape = shape
