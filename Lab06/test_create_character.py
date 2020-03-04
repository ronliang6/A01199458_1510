from unittest import TestCase
import maze


class Test(TestCase):
    def test_create_character(self):
        actual = maze.create_character()
        expected = [0, 0]
        self.assertEqual(actual, expected)
