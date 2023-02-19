from constants import COLUMN_MAP, DAY_OF_WEEK_MAP

__all__ = (
    'to_cell_name',
    'to_weekday',
)


def to_cell_name(c: tuple[int, int]) -> str:
    return f'{COLUMN_MAP[c[1]]}{c[0]}'


def to_weekday(day_of_week: str) -> int:
    return DAY_OF_WEEK_MAP[day_of_week]
