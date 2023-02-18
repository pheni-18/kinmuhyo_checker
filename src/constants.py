SHEET_NAME = '勤務表'

COLUMN_MAP = {
    1: 'A',
    2: 'B',
    3: 'C',
    4: 'D',
    5: 'E',
    6: 'F',
    7: 'G',
    8: 'H',
    9: 'I',
}

MONTH_CELL = (4, 1)  # A4
NAME_CELL = (2, 7)  # G2


MESSAGES = {
    'INFO': {
        'SUCCEED': 'Succeed!',
    },
    'CRITICAL': {
        'FILE_NO_EXISTS_ERROR': 'CRITICAL ERROR: ファイルが存在しません',
        'EXTENSION_ERROR': 'CRITICAL ERROR: 拡張子は .xlsx のみ使用できます',
    },
    'VALIDATE': {
        'FILE_NAME_ERROR': 'VALIDATE ERROR: ファイル名が間違っています',
        'MONTH_ERROR': 'VALIDATE ERROR: 月が間違っています',
        'NAME_ERROR': 'VALIDATE ERROR: 名前が間違っています',
        'DAY_OF_WEEK_ERROR': 'VALIDATE ERROR: 日付と曜日が一致しません',
        'BREAK_TIME_ERROR': 'VALIDATE ERROR: 休憩時間が入力されていません',
        'HOLIDAY_WORNING': 'VALIDATE WARNING: 休日または祝日に勤務時間が入力されています'
    },
}
