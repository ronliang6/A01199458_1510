from unittest import TestCase
import exceptions


class Test(TestCase):
    def test_find_an_even_one_even(self):
        actual = exceptions.find_an_even([0])
        expected = 0
        self.assertEqual(actual, expected)

    def test_find_an_even_multiple_even(self):
        actual = exceptions.find_an_even([4, 2, 8])
        expected = 4
        self.assertEqual(actual, expected)

    def test_find_an_even_mixed_integers(self):
        actual = exceptions.find_an_even([7, 29, 12, 1, 0])
        expected = 12
        self.assertEqual(actual, expected)

    def test_find_an_even_only_odd_integers(self):
        with self.assertRaises(ValueError):
            exceptions.find_an_even([1, 7, 121])
