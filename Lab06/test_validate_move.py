from unittest import TestCase
import maze


class Test(TestCase):
    def test_validate_move_random_string(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [0, 0]
        direction = "gekkn3 1"
        actual = maze.validate_move(board, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_duplicated_entry(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [0, 0]
        direction = "ss"
        actual = maze.validate_move(board, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_past_edge_of_board(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [0, 0]
        direction = "w"
        actual = maze.validate_move(board, character, direction)
        expected = False
        self.assertEqual(actual, expected)

    def test_validate_move_valid_movement(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [0, 0]
        direction = "s"
        actual = maze.validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_valid_movement_from_middle(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [2, 2]
        direction = "d"
        actual = maze.validate_move(board, character, direction)
        expected = True
        self.assertEqual(actual, expected)

    def test_validate_move_empty_string(self):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [2, 2]
        direction = ""
        actual = maze.validate_move(board, character, direction)
        expected = False
        self.assertEqual(actual, expected)
