from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[int, *Tuple[str, ...], str]) -> None: ...


foo(1, '')
foo(1, '', '')
foo(1, '', '', '', '', '', '')

foo(1, 1)
foo('', '')
foo(1, '', '', 1, '', '', '')
