from typing import TypeVar, TypeVarTuple, Callable, Tuple

T = TypeVar('T')
Ts = TypeVarTuple('Ts')


def foo(f: Callable[[int, *Ts, T], Tuple[T, *Ts]]) -> None: ...


def ok1(a: int, b: str, c: bool, d: list[int]) -> Tuple[list[int], str, bool]: ...
def ok2(a: int, b: str) -> Tuple[str]: ...


foo(ok1)
foo(ok2)


def err1(a: int, b: str, c: bool, d: list[int]) -> Tuple[list[int], str, str]: ...
def err2(a: int, b: str) -> Tuple[str, str]: ...


foo(err1)
foo(err2)
