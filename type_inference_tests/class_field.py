from typing import TypeVarTuple, Generic, Tuple

Ts = TypeVarTuple('Ts')


class A(Generic[*Ts]):
    def __init__(self, value: Tuple[int, *Ts]) -> None:
        self.field: Tuple[int, *Ts] = value

    def foo(self) -> None:
        expr = self.field
