from typing import TypeVar, TypeVarTuple, Callable, Tuple

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


def foo(f: Callable[[int, *Ts, T], Tuple[T, *Ts]]) -> Tuple[str, *Ts, int, T]: ...
def bar(a: int, b: str, c: float, d: bool) -> Tuple[bool, str, float]: ...


expr = foo(bar)
