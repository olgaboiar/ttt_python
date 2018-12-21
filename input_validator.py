class InputValidator:
    def __init__(self):
        pass

    def valid_marker(self, marker):
        if marker in ('X', 'O'):
            return True

    def valid_move(self, move):
        if int(move) in range(1, 10):
            return True
