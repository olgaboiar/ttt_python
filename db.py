import records
import os
from config import config
from players.computer import Computer
from board import Board

class DB:
    def __init__(self):
        params = self.read_config()
        self.postgres_db = records.Database(f"{params['driver']}://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}")
        self.check_db()

    def read_config(self):
        params = {}
        params['driver'] = os.environ.get('TTT_DB_DRIVER', None)
        if params['driver']:
            params['user'] = os.environ.get('TTT_DB_USER', None)
            params['password'] = os.environ.get('TTT_DB_PASSWORD', None)
            params['host'] = os.environ.get('TTT_DB_HOST', None)
            params['port'] = os.environ.get('TTT_DB_PORT', None)
            params['database'] = os.environ.get('TTT_DB_NAME', None)
        else:
            params = config()
        return params

    def get_best_move_from_db(self, computer_marker, board):
        query = "SELECT best_move FROM computer_best_moves WHERE computer_marker=:computer_marker AND board_spots=:board_spots"
        move = self.postgres_db.query(query, computer_marker=computer_marker, board_spots=board.spots_string())
        if len(move.all()) == 1:
            return move[0].best_move
        else:
            return None

    def insert_best_move_into_db(self, computer_marker, board, best_move):
        self.postgres_db.query('INSERT INTO computer_best_moves (board_spots, computer_marker, best_move) VALUES(:board_spots, :computer_marker, :best_move) ON CONFLICT ON CONSTRAINT game_state DO NOTHING',
                board_spots=board.spots_string(), computer_marker=computer_marker, best_move=best_move)

    def check_db(self):
        rows = self.postgres_db.query("SELECT COUNT(id) FROM computer_best_moves")
        if rows[0].count < 9039:
            self.generate_permutations()

    def generate_permutations(self):
        x_computer = Computer('X', self)
        board = Board()
        x_computer.choose_move(board)
        o_computer = Computer('O', self)
        for i in range(1, 10):
            new_board = Board()
            new_board.insert_value(i, 'X')
            o_computer.choose_move(new_board)
