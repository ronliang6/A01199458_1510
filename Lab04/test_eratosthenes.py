from unittest import TestCase
from Lab04 import lab04


class Test(TestCase):
    def test_smallest_bound(self):
        """Test the upper bound of one."""

        argument = lab04.eratosthenes(1)
        expected = []
        self.assertEqual(expected, argument, "There are no prime numbers in the list.")

    def test_list_of_one(self):
        """Test the upper bound of two."""

        argument = lab04.eratosthenes(2)
        expected = [2]
        self.assertEqual(expected, argument, "The list contains one prime number.")

    def test_list_of_several(self):
        """Test an upper bound that returns a list of many integers."""

        argument = lab04.eratosthenes(31)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        self.assertEqual(expected, argument, "The list contains eleven prime integers.")

    def test_list_of_many(self):
        """Test an upper bound that returns a list of many integers."""

        argument = lab04.eratosthenes(100)
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expected, argument, "The list contains many prime integers.")
