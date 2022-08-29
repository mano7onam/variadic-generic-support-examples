from typing import Tuple, Any

from array_declaration import Array, Shape, Batch, Height, Width, Channels


def read_from_file() -> Any:
    ...


y: Array[*Tuple[Any, ...]] = read_from_file()


def expect_variadic_array(
    x: Array[Batch, *Shape]
) -> None: ...


expect_variadic_array(y)  # OK


def expect_precise_array(
    x: Array[Batch, Height, Width, Channels]
) -> None: ...


expect_precise_array(y)  # OK
