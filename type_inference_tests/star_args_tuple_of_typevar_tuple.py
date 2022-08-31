from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[*Ts]) -> Tuple[*Ts]: ...


expr = foo((0, '1'), (1, '0'))

