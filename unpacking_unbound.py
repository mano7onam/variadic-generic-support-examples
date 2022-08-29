from typing import Tuple, Any

from array_declaration import Array, Batch, Channels, Width, Height


def process_batch_channels(
    x: Array[Batch, *Tuple[Any, ...], Channels]
) -> None:
    ...


x: Array[Batch, Height, Width, Channels]
process_batch_channels(x)  # OK
y: Array[Batch, Channels]
process_batch_channels(y)  # OK
z: Array[Batch]
process_batch_channels(z)  # Error: Expected Channels.
