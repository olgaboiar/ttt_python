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
        current_player = player1
        next_player = player2
        current_marker = marker1
        next_marker = marker2
        while not self.game_over(self.board):
            move = self.user_interface.choose_move(self.board)
            current_player.move(self.board, move, current_marker)
            self.user_interface.print_board(self.board)
            current_player, next_player = next_player, current_player
            current_marker, next_marker = next_marker, current_marker
        self.user_interface.game_over()

    def horizontal_win(self, board):
        if board.spots[0] == board.spots[1] == board.spots[2] or board.spots[3] == board.spots[4] == board.spots[5] or board.spots[6] == board.spots[7] == board.spots[8]:
            return True

    def vertical_win(self, board):
        if board.spots[0] == board.spots[3] == board.spots[6] or board.spots[1] == board.spots[4] == board.spots[7] or board.spots[2] == board.spots[5] == board.spots[8]:
            return True

    def diagonal_win(self, board):
        if board.spots[0] == board.spots[4] == board.spots[8] or board.spots[2] == board.spots[4] == board.spots[6]:
            return True

    def win(self, board):
        if self.horizontal_win(board) or self.vertical_win(board) or self.diagonal_win(board):
            return True

    def tie(self, board):
        available_spots = board.available_spots()
        if not available_spots:
            return True

    def game_over(self, board):
        if self.win(board) or self.tie(board):
            return True
