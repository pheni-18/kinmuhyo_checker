from messages import output_message, Message

import re

__all__ = (
    'Validator',
)


class Validator:
    @staticmethod
    def validate_file_name(file_name: str, year: int, month: int):
        pattern = r'勤務表_.*_[0-9]{6}'
        res = re.fullmatch(pattern, file_name)
        if res is None:
            output_message(Message.FILE_NAME_ERROR)
            return

        yyyymm = file_name.split('_')[2]
        if int(yyyymm[:4]) != year or int(yyyymm[4:]) != month:
            output_message(Message.FILE_NAME_ERROR)
            return
