from typing import Generic, TypeVar, TypeVarTuple, Tuple

Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')


class Box(Generic[*Ts1]):
    def get(self) -> Tuple[*Ts1]:
        pass


class Pair(Box[*Ts2], Generic[*Ts1]):
    pass


xs: Pair[int, str] = ...
expr = xs.get()
