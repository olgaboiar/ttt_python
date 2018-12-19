from player import Player

class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def start(self):
        self.user_interface.greet()
        marker1 = self.user_interface.choose_marker()
        player1 = Player(marker1)
        marker2 = player1.define_marker(marker1)
        print(marker1)
        print(marker2)
        self.user_interface.print_board()
