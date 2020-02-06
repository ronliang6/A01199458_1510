from unittest import TestCase
from Lab04 import lab04


class Test(TestCase):
    def test_smallest_arguments(self):
        """Test the smallest acceptable parameters."""

        argument = lab04.delete_multiples_of([1], 1)
        expected = [1]
        self.assertEqual(argument, expected, "The list contains one object.")

    def test_typical_arguments(self):
        """Test the function with a list of multiple integers and a number that deletes multiple integers."""

        argument = lab04.delete_multiples_of([2, 3, 4, 5, 6, 7, 8, 9, 10], 2)
        expected = [2, 3, 5, 7, 9]
        self.assertEqual(argument, expected, "The list contains five objects.")

    def test_large_number(self):
        """Test the function with a list of integers and a number that is larger than any of those integers."""

        argument = lab04.delete_multiples_of([1, 4, 7, 12], 72)
        expected = [1, 4, 7, 12]
        self.assertEqual(argument, expected, "The list contains four objects.")

    def test_no_multiples(self):
        """Test the function with a list of integers, none of which are multiples of the number."""

        argument = lab04.delete_multiples_of([2, 6, 7, 212], 5)
        expected = [2, 6, 7, 212]
        self.assertEqual(argument, expected, "The list contains four objects.")

    def test_all_multiples(self):
        """Test the function with a list of integers, all of which are multiples of the number."""

        argument = lab04.delete_multiples_of([10, 15, 20, 25], 5)
        expected = []
        self.assertEqual(argument, expected, "The list is empty.")
