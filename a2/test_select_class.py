import builtins
from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_select_class_fighter(self, _):
        actual = dnd.select_class()
        expected = "fighter"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["5"])
    def test_select_class_wizard(self, _):
        actual = dnd.select_class()
        expected = "wizard"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["12"])
    def test_select_class_paladin(self, _):
        actual = dnd.select_class()
        expected = "paladin"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["afafawas", "0", "23", "1"])
    def test_select_class_invalid_inputs(self, _):
        actual = dnd.select_class()
        expected = "fighter"
        self.assertEqual(actual, expected)
