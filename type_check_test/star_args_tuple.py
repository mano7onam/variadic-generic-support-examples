from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(path: str, *args: *Tuple[*Ts, str]) -> None: ...


foo('', 1, True, [1], '')
foo('', '')
foo('')
foo('', 1, True, [1])
