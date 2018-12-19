class Board:
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # self.available_spots = [spot for spot in self.board if spot != 'X' or spot != 'O']

    def get_value(self, spot):
        return self.board[spot]

    def insert_value(self, spot, marker):
        self.board[int(spot) - 1] = marker

    def available_spots(self):
        available_spots = [spot for spot in self.board if spot != 'X' and spot != 'O']
        return available_spots

    def all_spots(self):
        all_spots = [spot for spot in self.board]
        return all_spots
