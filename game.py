class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def start(self):
        self.user_interface.greet()
        # create players
          # get symbol
        self.user_interface.print_board()
        # play game
