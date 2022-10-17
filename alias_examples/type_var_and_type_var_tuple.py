from typing import Tuple, TypeVarTuple, TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')

MyType = Tuple[int, T, *Ts]

t: MyType[str, bool, float]
expr = t
