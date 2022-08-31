from typing import TypeVarTuple, Generic, Tuple

Ts = TypeVarTuple('Ts')


class A(Generic[*Ts]):
    def __init__(self, value: Tuple[*Ts]) -> None:
        ...

    def foo(self) -> Tuple[int, *Ts, str]:
        ...


tpl = (True, 1.1)
a = A(tpl)
expr = a.foo()
