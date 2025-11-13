# https://github.com/asjchat/lab11-AC-BA
# Partner 1: Ananda Chatterjee
# Partner 2: Brayden Allen

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(0, 10), 0)
        self.assertEqual(mul(-10, 10), -100)

    def test_divide(self): # 3 assertions  fill in code
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-50, 5), -10)
        with self.assertRaises(ZeroDivisionError):
            div(1, 0)



    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 10)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(10, -5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
            self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

# Do not touch this
if __name__ == "__main__":
    unittest.main()