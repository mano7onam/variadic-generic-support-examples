from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[int, *Tuple[str, ...], str]) -> None: ...


foo(42, '')
foo(42, '', '')
foo(42, '', '', '', '')

foo(42, '', '', '', 42)
foo(42, 42, '', '', '')
foo(42, 42, '')
