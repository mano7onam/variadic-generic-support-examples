from typing import TypeVar, TypeVarTuple, Tuple

from array_declaration import T, Ts


def prefix_tuple(
    x: T,
    y: Tuple[*Ts]
) -> Tuple[T, *Ts]: ...


def suffix_tuple(
    y: Tuple[*Ts],
    x: T
) -> Tuple[*Ts, T]: ...


z = prefix_tuple(x=0, y=(True, 'a'))
t = suffix_tuple(y=(True, 'a'), x=0)
# Inferred type of z is Tuple[int, bool, str]
