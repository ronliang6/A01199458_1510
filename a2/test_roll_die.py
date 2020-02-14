from unittest import TestCase
from unittest.mock import patch

from a2.dnd import roll_die


class Test(TestCase):
    @patch('random.randint', side_effect=[12])
    def test_roll_die_single_roll(self, _):
        expected = 12
        actual = roll_die(1, 20)
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[1, 2, 6])
    def test_roll_die_three_rolls(self, _):
        expected = 9
        actual = roll_die(3, 6)
        self.assertEqual(actual, expected)

    @patch('random.randint', side_effect=[7, 12, 8, 2, 35, 92, 1002, 855, 51])
    def test_roll_die_many_rolls(self, _):
        expected = 2064
        actual = roll_die(9, 2000)
        self.assertEqual(actual, expected)
