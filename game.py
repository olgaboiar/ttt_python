class Game:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def start(self):
        self.user_interface.greet()
        # ui print board
