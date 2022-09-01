from typing import TypeVarTuple, Generic, Tuple

Ts = TypeVarTuple('Ts')


class A(Generic[*Ts]):
    def __init__(self, value: Tuple[int, *Ts]) -> None:
        self.field: Tuple[int, *Ts] = value


tpl = (42, 1.1, True, ['42'])
a = A(tpl)
expr = a.field
