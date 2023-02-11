from typing import Generic, TypeVarTuple, Tuple

Ts = TypeVarTuple("Ts")

class Box(Generic[*Ts]):
    pass

class StrBox(Box[str, int]):
    pass

def extract(b: Box[*Ts]) -> Tuple[*Ts]:
    pass

box = StrBox()
expr = extract(box)
