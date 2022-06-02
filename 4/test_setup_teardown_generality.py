import pytest
import json

from main import add, subtract, multiply, divide, GCD


def read_file(string):
    f = open(string + '.json')
    data = json.load(f)
    test_main = data['data']
    f.close()
    return test_main


class SetTearTest:
    @classmethod
    def setup_class_add(cls):
        print('\n----setup add tests----')

    @classmethod
    def teardown_class_add(cls):
        print('\n----teardown add tests----')

    @classmethod
    def setup_class_subtract(cls):
        print('\n----setup subtract tests----')

    @classmethod
    def teardown_class_subtract(cls):
        print('\n----teardown subtract tests----')

    @classmethod
    def setup_class_multiply(cls):
        print('\n----setup multiply tests----')

    @classmethod
    def teardown_class_multiply(cls):
        print('\n----teardown multiply tests----')

    @classmethod
    def setup_class_divide(cls):
        print('\n----setup divide tests----')

    @classmethod
    def teardown_class_divide(cls):
        print('\n----teardown divide tests----')


class NumbersJson:
    test_main = read_file('numbers')

    @pytest.mark.parametrize("a, b", test_main)
    def test_positive(self, a, b):
        assert add(a, b)

    @pytest.mark.parametrize("a, b", test_main)
    def test_negative(self, a, b):
        assert subtract(a, b)

    @pytest.mark.parametrize("a, b", test_main)
    def test_multiplication(self, a, b):
        assert multiply(a, b)

    @pytest.mark.parametrize("a, b", test_main)
    def test_division(self, a, b):
        assert divide(a, b)


class GCDJson:
    test_main = read_file('gcd')

    @pytest.mark.parametrize("a, b", test_main)
    def test_gcd(self, a, b):
        assert GCD(a, b)

    @pytest.mark.parametrize("a, b", [(-1, 45)])
    def test_error_number(self, a, b):
        with pytest.raises(TypeError):
            GCD(a, b)
