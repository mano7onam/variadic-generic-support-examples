from typing import Tuple, TypeVarTuple, TypeVar

T = TypeVar('T')
Ts = TypeVarTuple('Ts')

MyType = Tuple[int, T, *Ts]
MyType1 = MyType[str, bool, *Ts]

t: MyType1[list[str], dict[str, int]]  # first place  
expr = t
