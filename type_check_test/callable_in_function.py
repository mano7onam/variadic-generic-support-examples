from typing import Callable, TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')


def foo(a: int, f: Callable[[*Ts], None], args: Tuple[*Ts]) -> None: ...
def bar(a: int, b: str) -> None: ...


foo(1, bar, args=(0, 'foo'))

foo(1, bar, args=('foo', 0))
