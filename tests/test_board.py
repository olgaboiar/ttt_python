import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_get_spot_value_when_board_is_empty(self):
        board_spot_value = self.board.get_value(0)
        self.assertEqual(board_spot_value, 1)

    def test_get_spot_value_when_the_spot_is_taken(self):
        self.board.insert_value(2, 'X')
        board_spot_value = self.board.get_value(1)
        self.assertEqual(board_spot_value, 'X')

    def test_insert_value(self):
        self.board.insert_value(1, 'X')
        board_spot_value = self.board.get_value(0)
        self.assertEqual(board_spot_value, 'X')

    def test_availale_spots_when_board_is_empty(self):
        available_spots = self.board.available_spots()
        self.assertEqual(available_spots, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_availale_spots_when_board_is_not_empty(self):
        self.board.insert_value(1, 'X')
        available_spots = self.board.available_spots()
        self.assertEqual(available_spots, [2, 3, 4, 5, 6, 7, 8, 9])

    def test_availale_spots_when_board_is_all_taken(self):
        self.board.insert_value(0, 'X')
        self.board.insert_value(1, 'O')
        self.board.insert_value(2, 'X')
        self.board.insert_value(3, 'O')
        self.board.insert_value(4, 'X')
        self.board.insert_value(5, 'O')
        self.board.insert_value(6, 'X')
        self.board.insert_value(7, 'O')
        self.board.insert_value(8, 'X')
        available_spots = self.board.available_spots()
        self.assertEqual(available_spots, [])

    def test_all_spots_when_board_is_empty(self):
        all_spots = self.board.all_spots()
        self.assertEqual(all_spots, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_all_spots_when_board_is_not_empty(self):
        self.board.insert_value(2, 'X')
        all_spots = self.board.all_spots()
        self.assertEqual(all_spots, [1, 'X', 3, 4, 5, 6, 7, 8, 9])

    def test_all_spots_when_board_is_all_taken(self):
        self.board.insert_value(1, 'X')
        self.board.insert_value(2, 'O')
        self.board.insert_value(3, 'X')
        self.board.insert_value(4, 'O')
        self.board.insert_value(5, 'X')
        self.board.insert_value(6, 'O')
        self.board.insert_value(7, 'X')
        self.board.insert_value(8, 'O')
        self.board.insert_value(9, 'X')
        all_spots = self.board.all_spots()
        self.assertEqual(all_spots, ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])


if __name__ == '__main__':
    unittest.main()
