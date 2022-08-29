from typing import TypeVarTuple, Tuple

from array_declaration import Env

Ts = TypeVarTuple('Ts')


def args_to_tuple(*args: *Ts) -> Tuple[*Ts]: ...


expr = args_to_tuple(1, 'a')  # Inferred type is Tuple[int, str]


# ----------------------------------------------------


# what the difference???
def execle(path: str, *args: *Tuple[*Ts, Env]) -> None: ...


# different
def execle_1(path: str, *args: *Ts, env: Env) -> None: ...
# ------------------------------------------


def foo(*args: *Tuple[int, ...]) -> None: ...


# equivalent to:
def foo1(*args: int) -> None: ...
# ----------------------------------------------


def foo2(*args: *Tuple[int, *Tuple[str, ...], str]) -> None: ...
# -----------------------------------------------


def foo3(*args: *Tuple[int, str]) -> None: ...


foo(1, "hello")  # OK
# ----------------------------------------------


def foo4(*args: Ts): ...  # NOT valid
# ----------------------------------------------


def foo5(*args: Tuple[*Ts]): ...


foo((0,), (1,))    # Valid
foo((0,), (1, 2))  # Error
foo((0,), ('1',))  # Error
# ---------------------------------------------


