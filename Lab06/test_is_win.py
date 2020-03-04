from unittest import TestCase
import maze


class Test(TestCase):
    def test_is_win_win(self):
        actual = maze.is_win([4, 4])
        expected = True
        self.assertEqual(actual, expected)

    def test_is_win_one_correct(self):
        actual = maze.is_win([0, 4])
        expected = False
        self.assertEqual(actual, expected)

    def test_is_win_neither_correct(self):
        actual = maze.is_win([1, 1])
        expected = False
        self.assertEqual(actual, expected)