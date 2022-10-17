from typing import Tuple, TypeVarTuple, TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')
Ts1 = TypeVarTuple('Ts1')

MyType = Tuple[int, T, *Ts]
MyType1 = MyType[str, bool, *Ts1]

t: MyType1[list[str], dict[str, int]]
expr = t
