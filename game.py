from player import Player
from board import Board

class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.board = Board()

    def start(self):
        self.user_interface.greet()
        self.user_interface.print_board(self.board)
        
    def play(self):
        marker1 = self.user_interface.choose_marker()
        player1 = Player(marker1)
        marker2 = player1.define_marker(marker1)
        player2 = Player(marker2)
        move1 = self.user_interface.choose_move(self.board)
        player1.move(self.board, move1, marker1)
        self.user_interface.print_board(self.board)
        move2 = self.user_interface.choose_move(self.board)
        player2.move(self.board, move2, marker2)
        self.user_interface.print_board(self.board)

    def win(self, board):
        if self.horizontal_win(board) or self.vertical_win(board) or self.diagonal_win(board):
            return True

    def horizontal_win(self, board):
        if board.spots[0] == board.spots[1] == board.spots[2] or board.spots[3] == board.spots[4] == board.spots[5] or board.spots[6] == board.spots[7] == board.spots[8]:
            return True

    def vertical_win(self, board):
        if board.spots[0] == board.spots[3] == board.spots[6] or board.spots[1] == board.spots[4] == board.spots[7] or board.spots[2] == board.spots[5] == board.spots[8]:
            return True

    def diagonal_win(self, board):
        if board.spots[0] == board.spots[4] == board.spots[8] or board.spots[2] == board.spots[4] == board.spots[6]:
            return True
