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
    # CRITICAL
    FILE_NO_EXISTS_ERROR = MESSAGES['CRITICAL']['FILE_NO_EXISTS_ERROR']
    EXTENSION_ERROR = MESSAGES['CRITICAL']['EXTENSION_ERROR']

    # VALIDATE
    FILE_NAME_ERROR = MESSAGES['VALIDATE']['FILE_NAME_ERROR']
