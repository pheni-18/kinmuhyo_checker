import argparse
import datetime


def main():
    parser = argparse.ArgumentParser(description='translator')

    parser.add_argument('file_path', help='target excel file')

    now = datetime.datetime.now()

    default_month = now.month
    month_choices = [i for i in range(1, 13)]
    parser.add_argument('-m', '--month', type=int, default=default_month, choices=month_choices, help='target month')

    default_year = now.year
    year_choices = [i for i in range(1970, now.year + 2)]
    parser.add_argument('-y', '--year', type=int, default=default_year, choices=year_choices, help='target year')

    args = parser.parse_args()

    file_path = args.file_path
    month = args.month
    year = args.year

    print(file_path)
    print(month)
    print(year)


if __name__ == '__main__':
    main()
