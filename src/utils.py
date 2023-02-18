from constants import COLUMN_MAP

from typing import Tuple

__all__ = (
    'to_cell_name',
)


def to_cell_name(c: Tuple[int, int]) -> str:
    return f'{COLUMN_MAP[c[1]]}{c[0]}'
