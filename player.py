
class Player:
    def __init__(self, marker):
        self.marker = marker

    def define_marker(self, marker):
        if marker == 'O':
            other_marker = 'X'
        else:
            other_marker = 'O'
        return other_marker
