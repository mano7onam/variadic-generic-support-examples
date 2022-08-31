from typing import Generic, TypeVarTuple, NewType, Tuple

Ts = TypeVarTuple('Ts')


class Array(Generic[*Ts]):
    def __init__(self, shape: Tuple[*Ts]):
        ...


def add_suf_pref(x: Array[*Ts]) -> Array[int, *Ts, str]:
    ...


ts = ([42], True)
arr = Array(ts)
expr = add_suf_pref(arr)
