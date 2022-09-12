from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(a: str, *args: *Tuple[*Ts, int], b: str, c: bool) -> None: ...


foo('', '', True, b='', c=True)
