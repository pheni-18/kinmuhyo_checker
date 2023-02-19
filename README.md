# kinmuhyo_checker

## Usage

Simple usage

```bash
$ ./kinmuhyo-checker {YOUR_EXCEL_FILE_PATH}
```

Select month

```bash
$ ./kinmuhyo-checker --month 3 {YOUR_EXCEL_FILE_PATH}
```

Check more

```bash
$ ./kinmuhyo-checker --help
usage: kinmuhyo-checker [-h] [-m {1,2,3,4,5,6,7,8,9,10,11,12}] [-y {2020,2021,2022,2023,2024}] file_path

translator

positional arguments:
  file_path             target excel file

options:
  -h, --help            show this help message and exit
  -m {1,2,3,4,5,6,7,8,9,10,11,12}, --month {1,2,3,4,5,6,7,8,9,10,11,12}
                        target month
  -y {2020,2021,2022,2023,2024}, --year {2020,2021,2022,2023,2024}
                        target year
```


## For Developer

### Install

```bash
$ pipenv install --dev
```

### Build

```bash
$ pipenv run pyinstaller --onefile --name kinmuhyo-checker src/main.py
$
$ cd dist/
$ tar zcvf {OUTPUT_DIR}/kinmuhyo-checker.tar.gz kinmuhyo-checker
```

### Test

```bash
$ PYTHONPATH=src pipenv run pytest
```
