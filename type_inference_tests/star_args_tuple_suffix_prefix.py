from typing import TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[int, *Ts, str]) -> Tuple[*Ts, int]: ...


expr = foo(1, '', [], {}, True, '')
