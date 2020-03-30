from unittest import TestCase
import recursion


class Test(TestCase):
    def test_factorial_recursive_helper_zero(self):
        actual = recursion.factorial_recursive_helper(0)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_one(self):
        actual = recursion.factorial_recursive_helper(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_two(self):
        actual = recursion.factorial_recursive_helper(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_medium_number(self):

        actual = recursion.factorial_recursive_helper(10)
        expected = 3628800
        self.assertEqual(actual, expected)

    def test_factorial_recursive_helper_large_number(self):
        actual = recursion.factorial_recursive_helper(50)
        expected = 30414093201713378043612608166064768844377641568960512000000000000
        self.assertEqual(actual, expected)
