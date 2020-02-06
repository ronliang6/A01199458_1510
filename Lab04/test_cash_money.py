from unittest import TestCase
from Lab04 import lab04


class Test(TestCase):
    def test_least_money(self):
        """Test the function with the smallest amount of money accepted."""

        argument = lab04.cash_money(0.01)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(argument, expected, "The money is one cent.")

    def test_every_denomination(self):
        """Test the function with an amount of money that requires every denomination."""

        argument = lab04.cash_money(188.68)
        expected = [1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 3]
        self.assertEqual(argument, expected, "The money requires many different bills and coins")

    def test_big_money(self):
        """Test the function with a large sum of money."""

        argument = lab04.cash_money(9999999.99)
        expected = [99999, 1, 2, 0, 1, 2, 0, 3, 2, 0, 4]
        self.assertEqual(argument, expected, "The money requires many hundred-dollar bills.")
