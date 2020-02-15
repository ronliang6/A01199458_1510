from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_select_race_tiefling(self, _):
        actual = dnd.select_race()
        expected = "tiefling"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["5"])
    def test_select_race_elf(self, _):
        actual = dnd.select_race()
        expected = "elf"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["9"])
    def test_select_race_half_orc(self, _):
        actual = dnd.select_race()
        expected = "half-orc"
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=["afafawas", "0", "23", "1"])
    def test_select_race_invalid_inputs(self, _):
        actual = dnd.select_race()
        expected = "tiefling"
        self.assertEqual(actual, expected)

