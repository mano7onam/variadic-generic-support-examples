from typing import Iterator, Generic, Tuple, TypeVarTuple

Ts = TypeVarTuple("Ts")

class Entry(Generic[*Ts]):
    pass

class MyIterator(Iterator[Entry[*Ts]]):
    def __next__(self) -> Entry[*Ts]: ...

def iter_entries(path: Tuple[*Ts]) -> MyIterator[*Ts]: ...

def main() -> None:
    for x in iter_entries(("some path", 1, 1.1)):
        expr = x