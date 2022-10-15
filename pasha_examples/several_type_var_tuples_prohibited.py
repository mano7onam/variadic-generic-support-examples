from typing import TypeVarTuple
from typing import Generic

Ts1 = TypeVarTuple("Ts1")
Ts2 = TypeVarTuple("Ts2")


class Array(Generic[*Ts1, *Ts2]):
    ...
