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
    'VALIDATE': {
        'FILE_NAME_ERROR': 'VALIDATE ERROR: ファイル名が間違っています',
        'MONTH_ERROR': 'VALIDATE ERROR: 月が間違っています',
        'NAME_ERROR': 'VALIDATE ERROR: 名前が間違っています',
        'DAY_OF_WEEK_ERROR': 'VALIDATE ERROR: 日付と曜日が一致しません',
        'BREAK_TIME_EMPTY_ERROR': 'VALIDATE ERROR: 休憩時間が入力されていません',
        'BREAK_TIME_OVER_ERROR': 'VALIDATE ERROR: 休みの日に休憩時間が入力されています',
        'HOLIDAY_WORNING': 'VALIDATE WARNING: 休日または祝日に勤務時間が入力されています'
    },
}
