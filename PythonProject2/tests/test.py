import pytest
from app.calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiple_zero(self):
        assert self.calc.multiply(self, 6, 0) == 0

    def test_division(self):
        assert self.calc.division(self, 3, 5) == 0.6

    def test_subtraction_minus(self):
        assert self.calc.subtraction(self, 5, 10) == -5

    def test_adding_minus(self):
        assert self.calc.adding(self, -20, 5) == -15

    def teardown(self):
        print('Выполнение метода Teardown')
