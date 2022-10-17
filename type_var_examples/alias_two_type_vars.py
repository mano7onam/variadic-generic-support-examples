from typing import TypeVar, Tuple

T = TypeVar('T')
T1 = TypeVar('T1')

MyType = Tuple[int, T]
MyType1 = MyType[T1]

t: MyType1[str]
expr = t
