from db import DB

class Player:
    def __init__(self, marker):
        self.marker = marker

    def init_db(self):        
        self.db = DB()

    def switch_marker(self, marker):
        if marker == 'O':
            other_marker = 'X'
        else:
            other_marker = 'O'
        return other_marker

    def move(self, board, spot, marker):
        board.insert_value(spot, marker)
