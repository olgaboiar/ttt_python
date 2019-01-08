import unittest
from players.computer import Computer
from board import Board
from test_db import TestDB

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.test_db = TestDB()
        self.computer = Computer('O', self.test_db)
        self.board = Board()

    def test_choose_best_move_when_first_cell_is_taken_on_board(self):
        self.board.spots = ['X', 2, 3, 4, 5, 6, 7, 8, 9]
        move = self.computer.choose_move(self.board)
        self.assertEqual(move, 5)

    def test_move_score_when_last_winning_move_is_computers(self):
        self.board.spots = ['O', 'O', 'O', 'X', 'X', 6, 7, 8, 9]
        score = self.computer.move_score(self.board, 'O', 4)
        self.assertEqual(score, 6)

    def test_move_score_when_last_winning_move_is_not_computers(self):
        self.board.spots = ['X', 'X', 'X', 'O', 'O', 6, 7, 8, 9]
        score = self.computer.move_score(self.board, 'X', 4)
        self.assertEqual(score, -6)

    def test_move_score_when_last_tie_move_is_computers(self):
        self.board.spots = ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O']
        score = self.computer.move_score(self.board, 'O', 4)
        self.assertEqual(score, 0)

    def test_move_score_when_last_tie_move_is_not_computers(self):
        self.board.spots = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        score = self.computer.move_score(self.board, 'X', 4)
        self.assertEqual(score, 0)

    def test_next_player_when_last_was_x(self):
        next_player = self.computer.switch_marker('X')
        self.assertEqual(next_player, 'O')

    def test_next_player_when_last_was_o(self):
        next_player = self.computer.switch_marker('O')
        self.assertEqual(next_player, 'X')

    def test_best_move_when_one_move_away_from_horizontal_win(self):
        self.board.spots = ['X', 'X', 3, 'O', 'O', 6, 7, 8, 9]
        best_move = self.computer.choose_move(self.board)
        self.assertEqual(best_move, 6)

    def test_best_move_when_one_and_nine_are_x(self):
        self.board.spots = ['X', 2, 3, 4, 'O', 6, 7, 8, 'X']
        best_move = self.computer.choose_move(self.board)
        self.assertEqual(best_move, 2)

    def test_best_move_when_human_made_a_move_on_one(self):
        self.board.spots = ['X', 2, 3, 4, 5, 6, 7, 8, 9]
        best_move = self.computer.choose_move(self.board)
        self.assertEqual(best_move, 5)

    def test_best_move_when_human_made_a_move_on_five_and_nine(self):
        self.board.spots = ['O', 2, 3, 4, 'X', 6, 7, 8, 'X']
        best_move = self.computer.choose_move(self.board)
        self.assertEqual(best_move, 3)




    

if __name__ == '__main__':
    unittest.main()
