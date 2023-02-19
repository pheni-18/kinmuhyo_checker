# kinmuhyo_checker

## Install

```bash
$ pipenv install --dev
```

## Build

```bash
$ pipenv run pyinstaller --onefile --name kinmuhyo-checker src/main.py
```

## Test

```bash
$ PYTHONPATH=src pipenv run pytest
```
