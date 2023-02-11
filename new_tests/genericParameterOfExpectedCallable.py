from typing import Callable, Generic, TypeVar, TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')

class Super(Generic[*Ts]):
    pass

class Sub(Super[*Ts]):
    pass

def f(x: Callable[[Sub[*Ts]], None]) -> Tuple[*Ts]:
    pass

def g(x: Super[int, str, float]):
    pass

expr = f(g)
