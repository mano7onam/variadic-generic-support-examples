from typing import Generic, TypeVarTuple, Tuple

Shape = TypeVarTuple('Shape')

t: Tuple[*Shape]


class Array(Generic[*Shape]):
    ...
