import unittest
from players.computer import Computer
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.computer = Computer('O')
        self.board = Board()

    def test_choose_random_move_when_empty_board(self):
        move = self.computer.choose_move(self.board)
        self.assertTrue(move > 0 and move <= 9)

    def test_choose_random_move_when_non_empty_board(self):
        self.board.spots = ['X', 'X', 'O', 4, 'O', 'O', 7, 8, 'X']
        move = self.computer.choose_move(self.board)
        self.assertTrue(move == 4 or move == 7 or move == 8)


    

if __name__ == '__main__':
    unittest.main()
