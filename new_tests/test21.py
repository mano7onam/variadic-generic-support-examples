from typing import TypeVar, TypeVarTuple, Tuple

Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')


def f(x: Tuple[*Ts2]) -> Tuple[*Ts2]:
    pass


def g(x: Tuple[*Ts2]):
    return f(x)


expr = g((42, 'sdf'))
