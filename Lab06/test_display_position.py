import io
from unittest import TestCase
from unittest.mock import patch
import maze


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_position_top_left(self, output):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [0, 0]
        maze.display_position(board, character)
        expected = """You are currently here:
C * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_position_middle(self, output):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [2, 2]
        maze.display_position(board, character)
        expected = """You are currently here:
* * * * * 
* * * * * 
* * C * * 
* * * * * 
* * * * * 
"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_position_bottom_right(self, output):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [4, 4]
        maze.display_position(board, character)
        expected = """You are currently here:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * C 
"""
        self.assertEqual(output.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_position_left_middle(self, output):
        board = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        character = [2, 0]
        maze.display_position(board, character)
        expected = """You are currently here:
* * * * * 
* * * * * 
C * * * * 
* * * * * 
* * * * * 
"""
        self.assertEqual(output.getvalue(), expected)
