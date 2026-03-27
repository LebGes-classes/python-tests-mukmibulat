import unittest

from functions import (
    add,
    subtract,
    multiply,
    divide
)


class TestWorkability(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(-1, 2), 1)
        self.assertEqual(add(-2, -5), -7)
        self.assertEqual(add(1.5, 2.3), 3.8)
        self.assertEqual(add(5, 2.7), 7.7)

        self.assertRaises(TypeError, add, "5", 3)
        self.assertRaises(TypeError, add, None, 10)

    def test_subtract(self):
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(subtract(1, 0), 1)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(5.5, 2.3), 3.2)
        self.assertEqual(subtract(10, 3.5), 6.5)

        self.assertRaises(TypeError, subtract, [1], 2)
        self.assertRaises(TypeError, subtract, 7, "2")

    def test_multiply(self):
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 4), -8)
        self.assertEqual(multiply(-3, -4), 12)
        self.assertEqual(multiply(2.5, 3), 7.5)
        self.assertEqual(multiply(1.5, 2.5), 3.75)

        self.assertRaises(TypeError, multiply, "2", 3)
        self.assertRaises(TypeError, multiply, 4, None)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335)

        self.assertRaises(ZeroDivisionError, divide, 1, 0)

        self.assertRaises(TypeError, divide, "10", 2)
        self.assertRaises(TypeError, divide, 8, "2")


if __name__ == '__main__':
    unittest.main()