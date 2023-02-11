from typing import TypeVar, TypeVarTuple, Tuple

Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts2')


def f(x: Tuple[*Ts1], y: Tuple[*Ts2]) -> Tuple[*Ts2]:
    pass


def g(x: Tuple[*Ts2], y: Tuple[*Ts1]):
    return f(x, y)


expr = g((42, 'sdf'), (1, '2', [3]))
