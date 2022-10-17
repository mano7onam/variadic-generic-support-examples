from typing import TypeVar, Tuple

T = TypeVar('T')

MyType = Tuple[int, T]

t: MyType[str]
expr = t
