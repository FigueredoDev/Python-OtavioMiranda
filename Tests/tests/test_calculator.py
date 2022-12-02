try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:     # noqa: E722
    raise

import unittest

from calculator import sum_values


class TestCalculadora(unittest.TestCase):
    def test_sum_10_10_exit_20(self):
        self.assertEqual(sum_values(10, 10), 20)

    def test_sum_various_exits(self):
        x_y_exits = (
            (10, 10, 20),
            (5, 5, 10),
            (50, 1, 51),
            (-20, 30, 10),
        )

        for x_y_exit in x_y_exits:
            with self.subTest(x_y_exit=x_y_exit):
                x, y, exit = x_y_exit
                self.assertEqual(sum_values(x, y), exit)

    def test_sum_x_not_int_or_float_return_AssertionError(self):
        with self.assertRaises(AssertionError):
            sum_values('10', 10)

    def test_sum_y_not_int_or_float_return_AssertionError(self):
        with self.assertRaises(AssertionError):
            sum_values('10', 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
