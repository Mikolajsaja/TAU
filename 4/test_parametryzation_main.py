import pytest
from main import add, subtract, multiply, divide


class TestAddingFunction:
    def test_positive(self):
        assert add(5, 5) == 10
        assert add(20, -4) == 16

    def test_negative(self):
        assert add(-19, -21) == -40
        assert add(2, -4) == -2

    def test_no_result(self):
        with pytest.raises(TypeError):
            add(0.5, 't')


class TestSubtractionFunction:
    def test_positive(self):
        assert subtract(17, 8) == 9
        assert subtract(20, -4) == 24

    def test_negative(self):
        assert subtract(-23, -21) == -2
        assert subtract(-120, -100) == -20

    def test_no_result(self):
        with pytest.raises(TypeError):
            subtract(-7.1, 'ba')


class TestMultiplicationFunction:
    def test_positive(self):
        assert multiply(-7, -60) == 420
        assert multiply(23, 3) == 69

    def test_negative(self):
        assert multiply(2137, -1) == -2137
        assert multiply(2, -44) == -88

    def test_no_result(self):
        with pytest.raises(TypeError):
            multiply('a', 't')


class TestDivisionFunction:
    def test_positive(self):
        assert divide(5, 5) == 1
        assert divide(-1000, -25) == 40

    def test_negative(self):
        assert divide(24, -6) == -4
        assert divide(-64, 4) == -16

    def test_no_result(self):
        with pytest.raises(TypeError):
            divide(787, '8m')