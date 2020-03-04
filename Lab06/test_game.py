import io
from unittest import TestCase
from unittest.mock import patch

import maze


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["d", "d", "d", "d", "s", "s", "s", "s"])
    def test_game_direct_win(self, _, output):
        maze.game()
        self.assertIn("You win!", output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["d", "d", "d", "d", "a", "s", "s", "s", "s", "w", "d", "s"])
    def test_game_indirect_win(self, _, output):
        maze.game()
        self.assertIn("You win!", output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["a", "d", "d", "d", "d", "d", "s", "s", "s", "s"])
    def test_game_move_into_wall_win(self, _, output):
        maze.game()
        self.assertIn("You win!", output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["w", "d", "hello", "dddd", "123123", "go east" "d", "d", "d", "d", "d",
                                          "dda", "" "s", "s", "s", "", "s"])
    def test_game_win_with_all_types_invalid_inputs(self, _, output):
        maze.game()
        self.assertIn("You win!", output.getvalue())
