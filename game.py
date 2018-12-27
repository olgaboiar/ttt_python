from players.player_factory import PlayerFactory
from game_rules import GameRules

class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface
        self.rules = GameRules()
        self.player_factory = PlayerFactory()

    def start(self):
        self.user_interface.greet()

    def play(self, board):
        player1, player2 = self.create_players()
        current_player, current_marker, next_player, next_marker = self.set_current_player(player1, player2)
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
        return player1, player2

    def set_current_player(self, player1, player2):
        if player1.marker == 'X':
            return player1, player1.marker, player2, player2.marker
        return player2, player2.marker, player1, player1.marker
