from typing import Tuple
import numpy as np

graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # The index of the tile in the tilesheet
        ("fg", "3B"),
        ("bg", "3B"),
    ]
)

tile_dt = np.dtype(
    [
        ("walkable", bool),
        ("transparent", bool),
        ("dark", graphic_dt),
        ("light", graphic_dt),
    ]
)

def new_tile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)

# SHROUD: Index 0 is usually the top-left tile.
SHROUD = np.array((0, (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

# Floor: Second row (1), last column (7) -> Index 15
floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(15, (100, 100, 100), (0, 0, 0)),
    light=(15, (255, 255, 255), (0, 0, 0)),
)

# Wall: First row (0), last column (7) -> Index 7
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(7, (100, 100, 100), (0, 0, 0)),
    light=(7, (255, 255, 255), (0, 0, 0)),
)

# Down stairs: use '>' character
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord('>'), (100, 100, 100), (0, 0, 0)),
    light=(ord('>'), (255, 255, 0), (0, 0, 0)),
)
