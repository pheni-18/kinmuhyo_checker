from constants import MONTH_CELL, NAME_CELL
from messages import output_message, Message
from utils import to_cell_name, to_weekday

from datetime import datetime
from typing import Optional

import calendar
import re

__all__ = (
    'Validator',
)


class Validator:
    '''
    Each validate method return False if a validation error is occured.
    '''

    _year: int
    _month: int

    def __init__(self, year: int, month: int):
        self._year = year
        self._month = month

    @property
    def last_day(self) -> int:
        return calendar.monthrange(self._year, self._month)[1]

    def validate_file_name(self, file_name: str) -> bool:
        pattern = r'勤務表_.*_[0-9]{6}'
        res = re.fullmatch(pattern, file_name)
        if res is None:
            output_message(Message.FILE_NAME_ERROR)
            return False

        yyyymm = file_name.split('_')[2]
        if int(yyyymm[:4]) != self._year or int(yyyymm[4:]) != self._month:
            output_message(Message.FILE_NAME_ERROR)
            return False

        return True

    def validate_month(self, dt: datetime) -> bool:
        if self._year != dt.year or self._month != dt.month:
            output_message(Message.MONTH_ERROR, to_cell_name(MONTH_CELL))
            return False

        return True

    def validate_name(self, name: Optional[str]) -> bool:
        if name is None:
            output_message(Message.NAME_ERROR, to_cell_name(NAME_CELL))
            return False

        return True

    def validate_day_of_week(self, day: int, day_of_week: str, cell: tuple[int, int]) -> bool:
        # TODO: 存在しない日付チェック

        dt = datetime(self._year, self._month, day)
        if dt.weekday() != to_weekday(day_of_week):
            output_message(Message.DAY_OF_WEEK_ERROR, to_cell_name(cell))
            return False

        return True

    def validate_break_time(self, break_time: Optional[int], working_hours: int, cell: tuple[int, int]) -> bool:
        if working_hours > 0 and break_time is None:
            output_message(Message.BREAK_TIME_EMPTY_ERROR, to_cell_name(cell))
            return False

        if break_time is not None and break_time > working_hours:
            output_message(Message.BREAK_TIME_OVER_ERROR, to_cell_name(cell))
            return False

        return True
