from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('dnd.generate_syllable', side_effect=["hi"])
    def test_generate_name_short(self, _):
        expected = "Hi"
        actual = dnd.generate_name(1)
        self.assertEqual(expected, actual)

    @patch('dnd.generate_syllable', side_effect=["hi", "yo", "me"])
    def test_generate_name_medium(self, _):
        expected = "Hiyome"
        actual = dnd.generate_name(3)
        self.assertEqual(expected, actual)

    @patch('dnd.generate_syllable', side_effect=["la", "pe", "su", "re", "do", "la", "du", "tu"])
    def test_generate_name_long(self, _):
        expected = "Lapesuredoladutu"
        actual = dnd.generate_name(8)
        self.assertEqual(expected, actual)
