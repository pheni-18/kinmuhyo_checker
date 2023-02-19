from validator import Validator

from datetime import datetime

import pytest


@pytest.fixture()
def validator() -> Validator:
    return Validator(2023, 2)


class TestValidator:
    def test_validate_file_name(self, validator: Validator):
        assert validator.validate_file_name('勤務表_テスト太郎_202302')
        assert not validator.validate_file_name('勤務表_テスト太郎_2023年2月')
        assert not validator.validate_file_name('勤務表_テスト太郎_202303')

    def test_validate_year_month(self, validator: Validator):
        assert validator.validate_year_month(datetime(2023, 2, 1))
        assert not validator.validate_year_month(datetime(2023, 3, 1))
        assert not validator.validate_year_month(datetime(2022, 2, 1))

    def test_validate_name(self, validator: Validator):
        assert validator.validate_name('テスト太郎')
        assert not validator.validate_name(None)

    def test_validate_day(self, validator: Validator):
        assert validator.validate_day(datetime(2023, 2, 1), (1, 1))
        assert not validator.validate_day(None, (1, 1))
        assert not validator.validate_day(datetime(2023, 1, 31), (1, 1))

    def test_validate_day_of_week(self, validator: Validator):
        assert validator.validate_day_of_week(1, '水', (1, 1))
        assert not validator.validate_day_of_week(1, '日', (1, 1))

    def test_validate_break_time(self, validator: Validator):
        assert validator.validate_break_time(1, 8, (1, 1))
        assert not validator.validate_break_time(None, 8, (1, 1))
        assert not validator.validate_break_time(1, 0, (1, 1))

    def test_validate_holiday(self, validator: Validator):
        assert validator.validate_holiday(1, 8, (1, 1), (1, 2))
        assert not validator.validate_holiday(4, 8, (1, 1), (1, 2))  # saturday
        assert not validator.validate_holiday(5, 8, (1, 1), (1, 2))  # sunday
        assert not validator.validate_holiday(23, 8, (1, 1), (1, 2))  # holiday
