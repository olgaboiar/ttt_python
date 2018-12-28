import unittest
from players.computer import Computer
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.computer = Computer('O')
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
        next_player = self.computer.next_player('X')
        self.assertEqual(next_player, 'O')

    def test_next_player_when_last_was_o(self):
        next_player = self.computer.next_player('O')
        self.assertEqual(next_player, 'X')

    def test_best_move(self):
        self.board.spots = ['X', 'X', 'X', 'O', 'O', 6, 7, 8, 9]
        spots = self.computer.best_move(self.board, 'X')
        self.assertEqual(spots, -10)




    

if __name__ == '__main__':
    unittest.main()
