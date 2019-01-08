import copy
from players.player import Player
from game_rules import GameRules

class Computer(Player):
    def __init__(self, marker, db):
        Player.__init__(self, marker, db)
        self.rules = GameRules()
        self.db = db

    def choose_move(self, board):
        opponent = self.switch_marker(self.marker)
        move = self.db.get_best_move_from_db(self.marker, board)
        if move:
            return move
        self.best_move(board, opponent)
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
            index = scores.index(max(scores))
        else:
            index = scores.index(min(scores))

        self.best_move_var = moves[index]
        self.db.insert_best_move_into_db(self.marker, board, self.best_move_var)
        return scores[index]
