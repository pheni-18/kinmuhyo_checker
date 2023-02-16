from const import SHEET_NAME, NAME_CELL
from openpyxl import load_workbook

import argparse
import datetime
import os


def read_args():
    parser = argparse.ArgumentParser(description='translator')

    parser.add_argument('file_path', help='target excel file')

    now = datetime.datetime.now()

    default_month = now.month
    month_choices = [i for i in range(1, 13)]
    parser.add_argument('-m', '--month', type=int, default=default_month,
        choices=month_choices, help='target month')

    default_year = now.year
    year_choices = [i for i in range(1970, now.year + 2)]
    parser.add_argument('-y', '--year', type=int, default=default_year,
        choices=year_choices, help='target year')

    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.file_path)
    month = args.month
    year = args.year

    return file_path, month, year


def main():
    file_path, month, year = read_args()

    file_name, file_ext = os.path.splitext(os.path.basename(file_path))

    print(file_path)
    print(month)
    print(year)

    print(file_name)
    print(file_ext)

    workbook = load_workbook(file_path)
    sheet = workbook[SHEET_NAME]
    name = sheet.cell(row=NAME_CELL[0], column=NAME_CELL[1]).value
    print(name)


if __name__ == '__main__':
    main()
