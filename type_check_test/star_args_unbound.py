from typing import Tuple


def foo(*args: *Tuple[int, ...]) -> None: ...


foo()
foo(1)
foo(1, 2, 3)

foo('')
foo(1, '')
