"""Run with: python -m unittest discover -v"""

import math
import unittest

from integration import simpson, trapezoidal


class TestIntegration(unittest.TestCase):
    def test_simpson_is_exact_for_quadratic(self):
        self.assertAlmostEqual(simpson(lambda x: x**2, 0, 1, 10), 1 / 3)

    def test_trapezoidal_approximates_quadratic(self):
        self.assertAlmostEqual(trapezoidal(lambda x: x**2, 0, 1, 100), 1 / 3, delta=0.00002)

    def test_sine_integral(self):
        self.assertAlmostEqual(simpson(math.sin, 0, math.pi, 100), 2, delta=1e-7)

    def test_reversed_limits(self):
        self.assertAlmostEqual(simpson(lambda x: x**2, 1, 0, 10), -1 / 3)

    def test_equal_limits(self):
        self.assertEqual(trapezoidal(math.exp, 2, 2, 10), 0)
        self.assertEqual(simpson(math.exp, 2, 2, 10), 0)

    def test_invalid_n(self):
        with self.assertRaises(ValueError):
            trapezoidal(math.sin, 0, 1, 0)
        with self.assertRaises(ValueError):
            simpson(math.sin, 0, 1, 3)


if __name__ == "__main__":
    unittest.main()
