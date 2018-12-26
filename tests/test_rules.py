import unittest
from board import Board
from game_rules import GameRules

class RulesTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.rules = GameRules()

    def test_horizontal_win_when_first_row_is_all_x(self):
        self.board.spots = ['X', 'X', 'X', 'O', 'O', 6, 7, 8, 9]
        self.assertEqual(True, self.rules.horizontal_win(self.board))

    def test_horizontal_win_when_second_row_is_all_o(self):
        self.board.spots = ['X', 2, 'X', 'O', 'O', 'O', 'X', 8, 9]
        self.assertEqual(True, self.rules.horizontal_win(self.board))

    def test_horizontal_win_when_third_row_is_all_x(self):
        self.board.spots = [1, 'O', 3, 'O', 'O', 6, 'X', 'X', 'X']
        self.assertEqual(True, self.rules.horizontal_win(self.board))

    def test_vertical_win_when_first_column_is_all_x(self):
        self.board.spots = ['X', 2, 'O', 'X', 'O', 6, 'X', 8, 9]
        self.assertEqual(True, self.rules.vertical_win(self.board))

    def test_vertical_win_when_second_column_is_all_o(self):
        self.board.spots = ['X', 'O', 'X', 4, 'O', 6, 'X', 'O', 9]
        self.assertEqual(True, self.rules.vertical_win(self.board))

    def test_vertical_win_when_third_column_is_all_x(self):
        self.board.spots = [1, 2, 'X', 'O', 'O', 'X', 7, 8, 'X']
        self.assertEqual(True, self.rules.vertical_win(self.board))

    def test_diagonal_win_when_first_diagonal_is_all_x(self):
        self.board.spots = ['X', 'O', 3, 'O', 'X', 6, 7, 8, 'X']
        self.assertEqual(True, self.rules.diagonal_win(self.board))

    def test_diagonal_win_when_second_diagonal_is_all_o(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 6, 'O', 8, 'X']
        self.assertEqual(True, self.rules.diagonal_win(self.board))

    def test_win_when_horizontal_row_is_all_x(self):
        self.board.spots = [1, 'O', 3, 'O', 'O', 6, 'X', 'X', 'X']
        self.assertEqual(True, self.rules.win(self.board))

    def test_win_when_vertical_column_is_all_x(self):
        self.board.spots = ['X', 2, 'O', 'X', 'O', 6, 'X', 8, 9]
        self.assertEqual(True, self.rules.win(self.board))

    def test_win_when_second_diagonal_is_all_o(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 6, 'O', 8, 'X']
        self.assertEqual(True, self.rules.win(self.board))

    def test_win_when_board_is_empty(self):
        self.assertEqual(None, self.rules.win(self.board))

    def test_win_when_board_is_not_empty_but_no_winning_scenario_reached(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 'O', 7, 8, 'X']
        self.assertEqual(None, self.rules.win(self.board))

    def test_win_when_board_is_tie(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(None, self.rules.win(self.board))

    def test_tie_when_board_is_tie(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(True, self.rules.tie(self.board))

    def test_tie_when_board_is_empty(self):
        self.assertEqual(None, self.rules.tie(self.board))

    def test_tie_when_neither_win_nor_tie_is_reached(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 6, 7, 8, 9]
        self.assertEqual(None, self.rules.tie(self.board))

    def test_tie_when_second_diagonal_is_all_o(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 6, 'O', 8, 'X']
        self.assertEqual(None, self.rules.tie(self.board))

    def test_game_over_when_board_is_empty(self):
        self.assertEqual(None, self.rules.game_over(self.board))

    def test_game_over_when_neither_win_nor_tie_is_reached(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 6, 7, 8, 9]
        self.assertEqual(None, self.rules.game_over(self.board))

    def test_game_over_when_board_is_tie(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(True, self.rules.game_over(self.board))

    def test_game_over_when_second_diagonal_is_all_o(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 6, 'O', 8, 'X']
        self.assertEqual(True, self.rules.game_over(self.board))

if __name__ == '__main__':
    unittest.main()
