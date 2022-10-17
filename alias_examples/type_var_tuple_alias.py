from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')

MyType = Tuple[int, *Ts]

t: MyType[str, bool]
expr = t
