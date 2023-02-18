from constants import MESSAGES

from typing import Any

__all__ = (
    'output_message',
    'Message',
)


def output_message(message: str, extra: Any=None):
    if extra is None:
        print(message)
    else:
        print(f'{message}: {extra}')


class Message:
    # INFO
    SUCCEED = MESSAGES['INFO']['SUCCEED']

    # CRITICAL
    FILE_NO_EXISTS_ERROR = MESSAGES['CRITICAL']['FILE_NO_EXISTS_ERROR']
    EXTENSION_ERROR = MESSAGES['CRITICAL']['EXTENSION_ERROR']

    # VALIDATE
    FILE_NAME_ERROR = MESSAGES['VALIDATE']['FILE_NAME_ERROR']
    YEAR_MONTH_ERROR = MESSAGES['VALIDATE']['YEAR_MONTH_ERROR']
    NAME_ERROR = MESSAGES['VALIDATE']['NAME_ERROR']
    DAY_OF_WEEK_ERROR = MESSAGES['VALIDATE']['DAY_OF_WEEK_ERROR']
    BREAK_TIME_EMPTY_ERROR = MESSAGES['VALIDATE']['BREAK_TIME_EMPTY_ERROR']
    BREAK_TIME_OVER_ERROR = MESSAGES['VALIDATE']['BREAK_TIME_OVER_ERROR']
    HOLIDAY_WARNING = MESSAGES['VALIDATE']['HOLIDAY_WARNING']
