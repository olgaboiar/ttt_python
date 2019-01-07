import records
import os
from config import config

class DB:
    def __init__(self):
        params = self.read_config()
        self.postgres_db = records.Database(f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}")

    def read_config(self):
        params = {}
        params['user'] = os.environ.get('TTT_DB_USER', None)
        if params['user']:
            params['password'] = os.environ.get('TTT_DB_PASSWORD', None)
            params['host'] = os.environ.get('TTT_DB_HOST', None)
            params['port'] = os.environ.get('TTT_DB_PORT', None)
            params['database'] = os.environ.get('TTT_DB_NAME', None)
        else:
            params = config()

        return params

    def get_best_move_from_db(self, computer_marker, board):
        board_spots = ''.join(map(str, board.spots))
        query = "SELECT best_move FROM computer_best_moves WHERE computer_marker=:computer_marker AND board_spots=:board_spots"
        move = self.postgres_db.query(query, computer_marker=computer_marker, board_spots=board_spots)
        return move

    def insert_best_move_into_db(self, computer_marker, board, best_move):
        board_spots = ''.join(map(str, board.spots))
        self.postgres_db.query('INSERT INTO computer_best_moves (board_spots, computer_marker, best_move) VALUES(:board_spots, :computer_marker, :best_move)',
                board_spots=board_spots, computer_marker=computer_marker, best_move=best_move)
