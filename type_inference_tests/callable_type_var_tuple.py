from typing import TypeVar, TypeVarTuple, Callable, Tuple

Ts = TypeVarTuple('Ts')


def foo(f: Callable[[*Ts], Tuple[*Ts]]) -> Tuple[*Ts]: ...
def bar(a: int, b: str) -> Tuple[int, str]: ...


expr = foo(bar)
