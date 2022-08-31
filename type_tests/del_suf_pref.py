from typing import Generic, TypeVarTuple, NewType, Tuple

Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    def __init__(self, shape: Tuple[*Ts]):
        ...


def del_suf_pref(x: Array[int, *Ts, str]) -> Array[*Ts]:
    ...


ts = (42, [42], True, '42')
arr = Array(ts)
expr = del_suf_pref(arr)
