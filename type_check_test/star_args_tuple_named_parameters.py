from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(a: str, *args: *Tuple[*Ts, int], b: str, c: bool) -> None: ...


foo('', 1, True, [1], 42, '', True)
foo('', 1, [2], True, 42, '', True)
foo('', 42, '', c=True)
foo('', 1, [2], True, 42, c=True, b='')
foo('', 1, [2], True, 42, b='', c=True)

foo('', '', True)
foo('', 1, True, [1], '', '', True)
foo('', 1, [2], True, 42, True, True)
foo('', 1, [2], True, 42, '', '')
