from typing import Generic, TypeVarTuple, Tuple

Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')
Ts3 = TypeVarTuple('Ts3')

class Box(Generic[*Ts1]):
    pass

class StrBoxWithExtra(Box[str, int], Generic[*Ts2]):
    def __init__(self, extra: Tuple[*Ts2]):
        self.extra = extra

def func(b: Box[*Ts3]) -> Tuple[*Ts3]:
    pass

box = StrBoxWithExtra((42, 'a', 3.3))
expr = func(box)
