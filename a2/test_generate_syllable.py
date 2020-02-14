from unittest import TestCase
from unittest.mock import patch
import dnd


class Test(TestCase):
    @patch('dnd.generate_consonant', side_effect=["h"])
    @patch('dnd.generate_vowel', side_effect=["i"])
    def test_generate_syllable(self, _, __):
        expected = dnd.generate_syllable()
        actual = "hi"
        self.assertEqual(expected, actual)
