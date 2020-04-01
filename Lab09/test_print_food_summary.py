import io
from unittest import TestCase
import refactoring_calories
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_summary_length_three(self, output):
        refactoring_calories.print_food_summary({"ham": 50, "cheese": 20, "carrots": 10})
        expected = "\nFood Items: ['carrots', 'cheese', 'ham']\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_summary_length_zero(self, output):
        refactoring_calories.print_food_summary({})
        expected = "\nFood Items: []\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_summary_length_one(self, output):
        refactoring_calories.print_food_summary({"ham": 50})
        expected = "\nFood Items: ['ham']\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_food_summary_length_many(self, output):
        refactoring_calories.print_food_summary({"ham": 50, "cheese": 20, "carrots": 10, "people": 400, "ice": 0})
        expected = "\nFood Items: ['carrots', 'cheese', 'ham', 'ice', 'people']\n"
        self.assertEqual(output.getvalue(), expected)