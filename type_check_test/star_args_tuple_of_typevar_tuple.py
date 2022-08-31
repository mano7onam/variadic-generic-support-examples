from typing import Tuple, TypeVarTuple

Ts = TypeVarTuple('Ts')


def foo(*args: *Tuple[*Ts]): ...


foo((0,), (1,))    # Valid
foo((0,), (1, 2))  # Error
foo((0,), ('1',))  # Error
