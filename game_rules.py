class GameRules:
    def __init__(self):
        pass

    def horizontal_win(self, board, marker):
        return board.spots[0] == board.spots[1] == board.spots[2] == marker or board.spots[3] == board.spots[4] == board.spots[5] == marker or board.spots[6] == board.spots[7] == board.spots[8] == marker

    def vertical_win(self, board, marker):
        return board.spots[0] == board.spots[3] == board.spots[6] == marker or board.spots[1] == board.spots[4] == board.spots[7] == marker or board.spots[2] == board.spots[5] == board.spots[8] == marker

    def diagonal_win(self, board, marker):
        return board.spots[0] == board.spots[4] == board.spots[8] == marker or board.spots[2] == board.spots[4] == board.spots[6] == marker

    def win(self, board, marker):
        return self.horizontal_win(board, marker) or self.vertical_win(board, marker) or self.diagonal_win(board, marker)

    def tie(self, board):
        available_spots = board.available_spots()
        if not available_spots:
            return True

    def game_over(self, board, marker):
        return self.win(board, marker) or self.tie(board)