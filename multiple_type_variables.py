from typing import Generic, TypeVarTuple

from array_declaration import Ts2, Ts1


class Array(Generic[*Ts1, *Ts2]):  # Error
    ...


# x: Array[int, str, bool]  # Ts1 = ???, Ts2 = ???
