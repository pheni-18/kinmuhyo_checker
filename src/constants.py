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

DAY_OF_WEEK_MAP = {
    '月': 0,
    '火': 1,
    '水': 2,
    '木': 3,
    '金': 4,
    '土': 5,
    '日': 6,
}

MONTH_CELL = (4, 1)
NAME_CELL = (2, 7)
DAY_COLUMN = 1
DAY_OF_WEEK_COLUMN = 2
WORKING_START_COLUMN = 3
WORKING_END_COLUMN = 4
BREAK_TIME_COLUMN = 7
WORKING_HOURS_COLUMN = 8
START_ROW = 5


MESSAGES = {
    'INFO': {
        'SUCCEED': 'Succeed!',
    },
    'CRITICAL': {
        'FILE_NO_EXISTS_ERROR': 'CRITICAL ERROR: ファイルが存在しません',
        'EXTENSION_ERROR': 'CRITICAL ERROR: 拡張子は .xlsx のみ使用できます',
    },
    'VALIDATION': {
        'FILE_NAME_ERROR': 'VALIDATION ERROR: ファイル名が間違っています',
        'YEAR_MONTH_ERROR': 'VALIDATION ERROR: 年月が間違っています',
        'NAME_ERROR': 'VALIDATION ERROR: 名前が入力されていません',
        'DAY_EMPTY_ERROR': 'VALIDATION ERROR: 日付が入力されていません',
        'DAY_NOT_EXISTS_ERROR': 'VALIDATION ERROR: 存在しない日付です',
        'DAY_OF_WEEK_ERROR': 'VALIDATION ERROR: 日付と曜日が一致しません',
        'BREAK_TIME_EMPTY_ERROR': 'VALIDATION ERROR: 休憩時間が入力されていません',
        'BREAK_TIME_OVER_ERROR': 'VALIDATION ERROR: 休みの日に休憩時間が入力されています',
        'HOLIDAY_WARNING': 'VALIDATION WARNING: 休日または祝日に勤務時間が入力されています'
    },
}
