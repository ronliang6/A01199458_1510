from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('dnd.roll_die', side_effect=[7])
    def test_roll_hit_dice_1d12(self, _):
        expected = 7
        actual = dnd.roll_hit_dice("barbarian")
        self.assertEqual(expected, actual)

    @patch('dnd.roll_die', side_effect=[2])
    def test_roll_hit_dice_1d10(self, _):
        expected = 2
        actual = dnd.roll_hit_dice("fighter")
        self.assertEqual(expected, actual)

    @patch('dnd.roll_die', side_effect=[4])
    def test_roll_hit_dice_1d8(self, _):
        expected = 4
        actual = dnd.roll_hit_dice("bard")
        self.assertEqual(expected, actual)

    @patch('dnd.roll_die', side_effect=[1])
    def test_roll_hit_dice_1d1(self, _):
        expected = 1
        actual = dnd.roll_hit_dice("wizard")
        self.assertEqual(expected, actual)
