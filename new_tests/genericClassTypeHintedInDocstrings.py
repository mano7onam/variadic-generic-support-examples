from typing import Generic, TypeVar, TypeVarTuple, Tuple

Ts = TypeVarTuple('Ts')

class User1(Generic[*Ts]):
    def __init__(self, x: Tuple[*Ts]):
        self.x = x

    def get(self) -> Tuple[*Ts]:
        return self.x

c = User1((1, '2', 3.3))
expr = c.get()
