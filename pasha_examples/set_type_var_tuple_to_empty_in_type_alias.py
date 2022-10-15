from typing import TypeVarTuple

Ts = TypeVarTuple("Ts")

IntTuple = tuple[int, *Ts]

c: IntTuple[()] = (1, "")
