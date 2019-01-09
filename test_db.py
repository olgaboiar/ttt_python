from players.computer import Computer

class TestDB:
    def __init__(self):
        pass
    
    def get_best_move_from_db(self, computer_marker, board):
        computer = Computer(computer_marker, self)
        opponent = computer.switch_marker(computer_marker)
        computer.best_move(board, opponent)
        return computer.best_move_var

    def insert_best_move_into_db(self, computer_marker, board, best_move):
        pass
