import pytest
from main import add, subtract, multiply, divide

testdataAdd =[
    (1, 2, 3), (10, -5, 5), (-5, 6, 1)
]


@pytest.mark.parametrize("num1, num2, result", testdataAdd )
def test_Adding(num1, num2, result):
    assert add(num1, num2) == result


testdataSub =[
    (2, 1, 1), (10, -5, 15), (-50, -16, -34)
]


@pytest.mark.parametrize("num1, num2, result", testdataSub )
def test_Subtraction(num1, num2, result):
    assert subtract(num1, num2) == result


testdataSub =[
    (1, 2, 2), (10, 5, 50), (-5, 5, -25)
]


@pytest.mark.parametrize("num1, num2, result", testdataSub )
def test_Multiplication(num1, num2, result):
    assert multiply(num1, num2) == result


testdataSub =[
    (6, 2, 3), (10, -5, -2), (-84, 7, -12)
]


@pytest.mark.parametrize("num1, num2, result", testdataSub )
def test_Division(num1, num2, result):
    assert divide(num1, num2) == result



