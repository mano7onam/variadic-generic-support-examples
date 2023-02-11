from typing import Any, Generic, TypeVarTuple, Tuple

Ts = TypeVarTuple("Ts")

class Box(Generic[*Ts]):
    def get(self) -> Tuple[*Ts]:
        pass

class StrBox(Box[str, int, float]):
    pass

receiver: Any | int | StrBox = ...
expr = receiver.get()
