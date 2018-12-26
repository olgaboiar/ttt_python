from player_factory import PlayerFactory
from rules import Rules

class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.rules = Rules()
        self.player_factory = PlayerFactory()

    def start(self):
        self.user_interface.greet()

    def play(self, board):
        current_player, current_marker, next_player, next_marker = self.create_players()
        self.user_interface.print_board(board)
        while not self.rules.game_over(board):
            move = current_player.choose_move(board)
            current_player.move(board, move, current_marker)
            self.user_interface.print_board(board)
            current_player, next_player = next_player, current_player
            current_marker, next_marker = next_marker, current_marker
        self.user_interface.game_over()

    def create_players(self):
        marker1 = self.user_interface.choose_marker()
        player1 = self.player_factory.create_player('human', marker1)
        marker2 = player1.define_marker(marker1)
        player2 = self.player_factory.create_player('computer', marker2)
        return player1, marker1, player2, marker2
