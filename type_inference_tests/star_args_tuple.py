from typing import TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')


def args_to_tuple(*args: *Ts) -> Tuple[*Ts]: ...


expr = args_to_tuple(1, 'a')
