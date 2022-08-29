from typing import Tuple

from array_declaration import Ts

x: Tuple[int, *Ts, str, *Ts2]  # Error
y: Tuple[int, *Tuple[int, ...], str, *Tuple[str, ...]]  # Error