import pytest

from app.model import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    assert calculator.add(1, 2) == 3


def test_subtract(calculator):
    assert calculator.subtract(2, 1) == 1


def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6


def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(5, 2) == 2.5
    assert calculator.divide(1, 0) == "Cannot divide by zero!"