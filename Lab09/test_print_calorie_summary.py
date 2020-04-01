import io
from unittest import TestCase
import refactoring_calories
from unittest.mock import patch


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_length_three(self, output):
        refactoring_calories.print_calorie_summary({"ham": 50, "cheese": 20, "carrots": 10})
        expected = "Total Calories: 80 Average Calories: 26.7\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_length_one(self, output):
        refactoring_calories.print_calorie_summary({"ham": 50})
        expected = "Total Calories: 50 Average Calories: 50.0\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_zero_calories(self, output):
        refactoring_calories.print_calorie_summary({"ham": 0, "cheese": 0, "carrots": 0})
        expected = "Total Calories: 0 Average Calories: 0.0\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_many_calories(self, output):
        refactoring_calories.print_calorie_summary({"ham": 50000, "cheese": 20000, "carrots": 10000})
        expected = "Total Calories: 80000 Average Calories: 26666.7\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_length_long(self, output):
        refactoring_calories.print_calorie_summary({"ham": 50, "cheese": 20, "carrots": 10, "people": 400, "ice": 0})
        expected = "Total Calories: 480 Average Calories: 96.0\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_negative_calorie_foods(self, output):
        refactoring_calories.print_calorie_summary({"ham": -50, "cheese": -20, "carrots": -10, "people": 400})
        expected = "Total Calories: 320 Average Calories: 80.0\n\n"
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_calorie_summary_negative_calorie_total(self, output):
        refactoring_calories.print_calorie_summary({"ham": -50, "cheese": -20, "carrots": -10, "people": -400})
        expected = "Total Calories: -480 Average Calories: -120.0\n\n"
        self.assertEqual(output.getvalue(), expected)