from typing import Generic, TypeVarTuple, Tuple

Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')

class Box(Generic[*Ts1]):
    pass

class StrBoxWithExtra(Box[str], Generic[*Ts2]):
    def __init__(self, extra: Tuple[*Ts2]):
        self.extra = extra

expr = StrBoxWithExtra((42, 'a', 3.3))
