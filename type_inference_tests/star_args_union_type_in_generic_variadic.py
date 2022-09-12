from typing import TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[*Ts]) -> Tuple[*Ts]: ...


x: int | str
expr = foo(x)
