from unittest import TestCase
import maze


class Test(TestCase):
    def test_move_character_up(self):
        character = [2, 2]
        maze.move_character("w", character)
        actual = character
        expected = [1, 2]
        self.assertEqual(actual, expected)

    def test_move_character_down(self):
        character = [3, 4]
        maze.move_character("s", character)
        actual = character
        expected = [4, 4]
        self.assertEqual(actual, expected)

    def test_move_character_left(self):
        character = [2, 3]
        maze.move_character("a", character)
        actual = character
        expected = [2, 2]
        self.assertEqual(actual, expected)

    def test_move_character_right(self):
        character = [0, 2]
        maze.move_character("d", character)
        actual = character
        expected = [0, 3]
        self.assertEqual(actual, expected)