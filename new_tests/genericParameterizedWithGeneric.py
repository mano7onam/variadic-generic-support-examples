from typing import Generic, TypeVar, TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')


class Box(Generic[*Ts]):
    def get(self) -> Tuple[*Ts]:
        pass


class ListBox(Box[Tuple[*Ts]]):
    pass


xs: ListBox[int, str] = ...
expr = xs.get()
