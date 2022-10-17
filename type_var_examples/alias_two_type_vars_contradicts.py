from typing import TypeVar, Tuple

T = TypeVar('T')
T1 = TypeVar('T1')

MyType = Tuple[T, T1]
MyType1 = MyType[int, T]
MyType2 = MyType1[str]

t: MyType2
expr = t
