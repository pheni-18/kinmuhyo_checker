from constants import MONTH_CELL, NAME_CELL
from messages import output_message, Message
from utils import to_cell_name

from datetime import datetime

import re

__all__ = (
    'Validator',
)


class Validator:
    _year: int
    _month: int

    def __init__(self, year: int, month: int):
        self._year = year
        self._month = month

    def validate_file_name(self, file_name: str):
        pattern = r'勤務表_.*_[0-9]{6}'
        res = re.fullmatch(pattern, file_name)
        if res is None:
            output_message(Message.FILE_NAME_ERROR)
            return

        yyyymm = file_name.split('_')[2]
        if int(yyyymm[:4]) != self._year or int(yyyymm[4:]) != self._month:
            output_message(Message.FILE_NAME_ERROR)
            return

    def validate_month(self, dt: datetime):
        if self._year != dt.year or self._month != dt.month:
            output_message(Message.MONTH_ERROR, to_cell_name(MONTH_CELL))
            return

    def validate_name(self, name: str):
        if name is None:
            output_message(Message.NAME_ERROR, to_cell_name(NAME_CELL))
            return
