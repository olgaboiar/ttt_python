class InputValidator:
    def __init__(self):
        pass

    def valid_marker(self, marker):
        if marker in ('X', 'O'):
            return True
