class Board:
    def __init__(self):
        self.spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_value(self, spot):
        return self.spots[spot]

    def insert_value(self, spot, marker):
        self.spots[int(spot) - 1] = marker

    def available_spots(self):
        available_spots = [spot for spot in self.spots if spot != 'X' and spot != 'O']
        return available_spots

    def all_spots(self):
        return self.spots

    def spots_string(self):
        return ''.join(map(str, self.spots))
