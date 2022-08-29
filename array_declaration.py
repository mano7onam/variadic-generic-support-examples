from typing import TypeVarTuple, Generic, NewType, TypeVar

Shape = TypeVarTuple('Shape')


class Array(Generic[*Shape]):
    ...


Height = NewType('Height', int)
Width = NewType('Width', int)
Time = NewType('Time', int)
Batch = NewType('Batch', int)
Channels = NewType('Channels', int)
Env = NewType('Env', int)
T = TypeVar('T')
Ts = TypeVarTuple('Ts')
Ts1 = TypeVarTuple('Ts1')
Ts2 = TypeVarTuple('Ts1')
