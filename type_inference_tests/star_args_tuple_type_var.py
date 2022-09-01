from typing import TypeVarTuple, Tuple, TypeVar

Ts = TypeVarTuple('Ts')
T1 = TypeVar('T1')
T2 = TypeVar('T2')


def args_to_tuple(t1: T1, t2: T2, *args: *Tuple[T2, *Ts, int]) -> Tuple[T2, *Ts, T1]: ...


expr = args_to_tuple(1, 'a', 'a', [1], True, 3)
