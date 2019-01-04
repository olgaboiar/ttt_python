import copy
import records
from players.player import Player
from game_rules import GameRules
from config import config

class Computer(Player):
    def __init__(self, marker):
        Player.__init__(self, marker)
        self.rules = GameRules()
        params = config()
        self.db = records.Database(f"postgresql://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}")

    def choose_move(self, board):
        opponent = self.switch_marker(self.marker)
        board_spots = ''.join(map(str, board.spots))
        computer_marker = self.marker
        query = f"SELECT best_move FROM computer_best_moves WHERE computer_marker='{computer_marker}' AND board_spots='{board_spots}'"
        move = self.db.query(query)

        try:
            print("trying to get it from DB!!!!")
            return move[0].best_move
        except IndexError:
            self.best_move(board, opponent)
            print("I got it from minimax!!!!")
            best_move = self.best_move_var
            self.db.query('INSERT INTO computer_best_moves (board_spots, computer_marker, best_move) VALUES(:board_spots, :computer_marker, :best_move)',
                board_spots=board_spots, computer_marker=computer_marker, best_move=best_move)
            return self.best_move_var

    def move_score(self, board, last_move, depth):
        if self.rules.win(board, last_move) and last_move == self.marker:
            return 10 - depth
        if self.rules.win(board, last_move) and last_move != self.marker:
            return depth - 10
        if self.rules.tie(board):
            return 0

    def best_move(self, board, last_move, depth = 0):
        moves = []
        scores = []
        current_move = None
        if self.rules.game_over(board, last_move):
            return self.move_score(board, last_move, depth)
        
        for spot in board.available_spots():
            potential_board = copy.deepcopy(board)
            initial_value = spot
            current_move = self.switch_marker(last_move)
            potential_board.insert_value(spot, current_move)
            scores.append(self.best_move(potential_board, current_move, depth + 1))
            moves.append(spot)
            potential_board.insert_value(spot, initial_value)
        if current_move == self.marker:
            max_index = scores.index(max(scores))
            self.best_move_var = moves[max_index]
            return scores[max_index]
        else:
            min_index = scores.index(min(scores))
            self.best_move_var = moves[min_index]
            return scores[min_index]
