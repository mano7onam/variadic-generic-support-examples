from typing import Tuple, Any

from array_declaration import Array, Height, Width, Time


def takes_any_array(arr: Array): ...


# equivalent to:
def takes_any_array(arr: Array[*Tuple[Any, ...]]): ...


x: Array[Height, Width]
takes_any_array(x)  # Valid
y: Array[Time, Height, Width]
takes_any_array(y)  # Also valid


# ------------------------------------------------


def takes_specific_array(arr: Array[Height, Width]): ...


z: Array
# equivalent to Array[*Tuple[Any, ...]]

takes_specific_array(z)
