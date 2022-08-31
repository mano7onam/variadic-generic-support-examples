from typing import TypeVarTuple, Generic, NewType, TypeVar

Height = NewType('Height', int)
Width = NewType('Width', int)
Time = NewType('Time', int)
Batch = NewType('Batch', int)
Channels = NewType('Channels', int)
Env = NewType('Env', int)

Shape = TypeVarTuple('Shape')
Ts = TypeVarTuple('Ts')
Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts1')

T = TypeVar('T')
DType = TypeVar('DType')


class Array(Generic[*Shape]):
    ...

