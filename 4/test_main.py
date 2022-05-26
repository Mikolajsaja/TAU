import unittest
from main import add
from main import subtract
from main import multiply
from main import divide
from main import GCD


class AddTest(unittest.TestCase):
    def addingTest(self):
        self.assertAlmostEqual(add(5, 5), 10)
        self.assertAlmostEqual(add(-5, -5), -10)

    def addingValueTest(self):
        self.assertRaises(TypeError, add('-5k', 'j'), 5)


class SubtractTest(unittest.TestCase):
    def subtractingTest(self):
        self.assertAlmostEqual(subtract(5, 5), 0)
        self.assertAlmostEqual(subtract(-5, -5), 0)

    def subtractingValueTest(self):
        self.assertRaises(TypeError, subtract('5k', 'j'), -5)


class MultiplyTest(unittest.TestCase):
    def multiplyingTest(self):
        self.assertAlmostEqual(multiply(5, 5), 25)
        self.assertAlmostEqual(multiply(-5, 5), -25)
        self.assertAlmostEqual(multiply(-3, -4), 12)

    def multiplyingValueTest(self):
        self.assertRaises(TypeError, multiply('kot', 'pies'), 'szczur')


class DivideTest(unittest.TestCase):
    def dividingTest(self):
        self.assertAlmostEqual(divide(5, 5), 1)
        self.assertAlmostEqual(subtract(10, -5), -2)
        self.assertAlmostEqual(divide(-20, -4), 5)

    def multiplyingValueTest(self):
        self.assertRaises(TypeError, divide('kot', 'pies'), 'szczur')


class GCDTest(unittest.TestCase):
    def GCDTest(self):
        self.assertAlmostEqual(GCD(25, 5), 5)

    def GCDValueErrorTest(self):
        self.assertRaises(ValueError, GCD(-5, 4), 1)


