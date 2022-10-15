from typing import TypeVarTuple

Ts = TypeVarTuple("Ts")

x: tuple[int, *Ts, str, *Ts]
y: tuple[int, *tuple[int, ...], str, *tuple[str, ...]]
