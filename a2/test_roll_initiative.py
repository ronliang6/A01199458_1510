from unittest import TestCase
from unittest.mock import patch

import dnd


class Test(TestCase):
    @patch('dnd.roll_die', side_effect=[15, 12])
    def test_roll_initiative_first_string_win(self, _):
        actual = dnd.roll_initiative("Chris", "Topher")
        expected = "Chris"
        self.assertEqual(actual, expected)

    @patch('dnd.roll_die', side_effect=[6, 12])
    def test_roll_initiative_second_string_win(self, _):
        actual = dnd.roll_initiative("Chris", "Topher")
        expected = "Topher"
        self.assertEqual(actual, expected)

    @patch('dnd.roll_die', side_effect=[12, 12, 7, 7, 9, 9, 1, 18])
    def test_roll_initiative_three_ties(self, _):
        actual = dnd.roll_initiative("Chris", "Topher")
        expected = "Topher"
        self.assertEqual(actual, expected)
