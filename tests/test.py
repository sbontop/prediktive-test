import unittest

from src.util.constants import DUMMY_EQUIPMENTS
from src.util.exceptions import (
    InvalidDataTypeException,
    InvalidYearException,
    QuantityNotFoundException,
)
from src.util.util import Calculator


class TestCalculation(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator(DUMMY_EQUIPMENTS)
        return super().setUp()

    def test_calculation_model_id_and_year_exists_should_succeed(self):
        actual = {
            "market_value": 0.31,
            "auction_value": 0.18,
        }
        model_id: str = "67352"
        year: str = "2006"
        expected = self.calculator.calculate(model_id, year)
        assert actual == expected

    def test_calculation_model_id_exist_year_and_does_not_should_fail(self):
        self._quantity_does_not_exist("67352", "2022")

    def test_calculation_model_id_does_not_exist_and_year_exist_should_fail(self):
        self._quantity_does_not_exist("1", "2006")

    def test_calculation_model_id_does_not_exist_and_year_does_not_exist(self):
        self._quantity_does_not_exist("1", "1000")

    def _quantity_does_not_exist(self, model_id: str, year: str):
        with self.assertRaises(QuantityNotFoundException):
            self.calculator.calculate(model_id, year)

    def test_calculation_invalid_year_should_fail(self):
        model_id, year = "67352", "1"
        with self.assertRaises(InvalidYearException):
            self.calculator.calculate(model_id, year)

    def test_calculation_invalid_data_type_should_fail_with_invalid_model_id(self):
        model_id, year = 67352, "1"
        with self.assertRaises(InvalidDataTypeException):
            self.calculator.calculate(model_id, year)

    def test_calculation_invalid_data_type_should_fail_with_invalid_year(self):
        model_id, year = "67352", 1
        with self.assertRaises(InvalidDataTypeException):
            self.calculator.calculate(model_id, year)
