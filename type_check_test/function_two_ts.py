from typing import TypeVarTuple, Generic

Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    ...


def foo(x: Array[*Ts], y: Array[*Ts]) -> Array[*Ts]:
    ...


x = Array[int]
y = Array[str]
z = Array[int, str]

foo(x, x)

foo(x, y)
foo(x, z)
