from typing import Tuple, TypeVarTuple, TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


def foo(x: T, y: Tuple[*Ts]):
    pass


foo(10, (1, '1', [1]))
