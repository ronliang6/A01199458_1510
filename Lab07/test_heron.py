from unittest import TestCase
import exceptions


class Test(TestCase):
    def test_heron_negative(self):
        actual = exceptions.heron(-21)
        expected = -1
        self.assertEqual(actual, expected)

    def test_heron_zero(self):
        actual = exceptions.heron(0)
        expected = 0.0
        self.assertEqual(actual, expected)

    def test_heron_between_zero_and_one(self):
        actual = exceptions.heron(0.25)
        expected = 0.5
        self.assertEqual(actual, expected)

    def test_heron_one(self):
        actual = exceptions.heron(1)
        expected = 1.0
        self.assertEqual(actual, expected)

    def test_heron_root_is_integer(self):
        actual = exceptions.heron(100)
        expected = 10.0
        self.assertEqual(actual, expected)

    def test_heron_root_is_float(self):
        actual = exceptions.heron(1000)
        expected = 31.62
        self.assertEqual(actual, expected)

