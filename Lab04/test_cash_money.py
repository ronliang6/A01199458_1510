from unittest import TestCase
from Lab04 import lab04


class Test(TestCase):
    def test_cash_money_no_money(self):
        """Test the function with no money."""

        argument = lab04.cash_money(0.00)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is nothing.")

    def test_cash_money_penny(self):
        """Test the function with the smallest amount of money accepted (a penny, 0.01)."""

        argument = lab04.cash_money(0.01)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        self.assertEqual(argument, expected, "The money is one penny.")

    def test_cash_money_two_penny(self):
        """Test the function with two cents (0.02)."""

        argument = lab04.cash_money(0.02)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
        self.assertEqual(argument, expected, "The money is two pennies.")

    def test_cash_money_nickel(self):
        """Test the function with a nickel (0.05)."""

        argument = lab04.cash_money(0.05)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        self.assertEqual(argument, expected, "The money is one nickel.")

    def test_cash_money_dime(self):
        """Test the function with a dime (0.10)."""

        argument = lab04.cash_money(0.10)
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual(argument, expected, "The money is one dime.")

    def test_cash_money_quarter(self):
        """Test the function with a quarter (0.25)."""

        argument = lab04.cash_money(0.25)
        expected = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one quarter.")

    def test_cash_money_dollar(self):
        """Test the function with a dollar (1.00)."""

        argument = lab04.cash_money(1.00)
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one dollar.")

    def test_cash_money_dollar_and_nickel(self):
        """Test the function with a dollar and a nickel (1.05)."""

        argument = lab04.cash_money(1.05)
        expected = [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
        self.assertEqual(argument, expected, "The money is one dollar and one nickel.")

    def test_cash_money_toonie(self):
        """Test the function with a toonie (2.00)."""

        argument = lab04.cash_money(2.00)
        expected = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one toonie.")

    def test_cash_money_fin(self):
        """Test the function with a fin (5.00)."""

        argument = lab04.cash_money(5.00)
        expected = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one fin.")

    def test_cash_money_bill_ten(self):
        """Test the function with a ten-dollar bill (10.00)."""

        argument = lab04.cash_money(10.00)
        expected = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one ten-dollar bill.")

    def test_cash_money_variety(self):
        """Test the function with money that would require different denominations of change."""

        argument = lab04.cash_money(10.27)
        expected = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2]
        self.assertEqual(argument, expected, "The money is one ten-dollar bill, one quarter, and two pennies.")

    def test_cash_money_bill_twenty(self):
        """Test the function with a twenty-dollar bill (20.00)."""

        argument = lab04.cash_money(20.00)
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one twenty-dollar bill.")

    def test_cash_money_bill_fifty(self):
        """Test the function with a fifty-dollar bill (50.00)."""

        argument = lab04.cash_money(50.00)
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one fifty-dollar bill.")

    def test_cash_money_bill_hundred(self):
        """Test the function with a hundred-dollar bill (100.00)."""

        argument = lab04.cash_money(100.00)
        expected = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(argument, expected, "The money is one hundred-dollar bill.")

    def test_cash_money_large_variety(self):
        """Test the function with a large amount of money that would require different denominations of change."""

        argument = lab04.cash_money(100.57)
        expected = [1, 0, 0, 0, 0, 0, 0, 2, 0, 1, 2]
        self.assertEqual(argument, expected, "The money is one hundred-dollar bill, two quarters, one nickel, "
                                             "and two pennies.")

    def test_cash_money_every_denomination(self):
        """Test the function with money that would require one unit of each denomination."""

        argument = lab04.cash_money(188.41)
        expected = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(argument, expected, "The money requires one of each denomination")
