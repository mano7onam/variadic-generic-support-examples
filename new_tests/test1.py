from typing import Generic, TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')
Ts1 = TypeVarTuple('Ts1')


class Super(Generic[*Ts]):
    pass


class Sub(Super[*Ts1]):
    def __init__(self, xs: Tuple[*Ts1]):
        pass


def func(xs: Tuple[*Ts]):
    expr = Sub(xs)
