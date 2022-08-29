from typing import Tuple

from array_declaration import T, Ts


def foo(x: T, y: Tuple[*Ts]):
    print(type(x))
    print(type(y))


def bar(x: T, y: Tuple[*Ts]):
    print(type(x))
    print(type(y))


# it is possible!!!
foo(42, ('42', 12, [1, 2, 3]))
bar('42', ([1, 2, 3], [4, 5, 6]))
