from typing import Callable, TypeVar, TypeVarTuple, Tuple

Ss = TypeVarTuple('Ss')
Ts = TypeVarTuple('Ts')

def dec(ts: Tuple[*Ts]):
    def g(fun: Callable[[], Tuple[*Ss]]) -> Callable[[*Ts], Tuple[*Ss]]:
        ...

    return g

def func() -> Tuple[int, str, float]:
    ...

expr = dec(('foo', 42))(func)