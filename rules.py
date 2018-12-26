class Rules:
    def __init__(self):
        pass

    def horizontal_win(self, board):
        if board.spots[0] == board.spots[1] == board.spots[2] or board.spots[3] == board.spots[4] == board.spots[5] or board.spots[6] == board.spots[7] == board.spots[8]:
            return True

    def vertical_win(self, board):
        if board.spots[0] == board.spots[3] == board.spots[6] or board.spots[1] == board.spots[4] == board.spots[7] or board.spots[2] == board.spots[5] == board.spots[8]:
            return True

    def diagonal_win(self, board):
        if board.spots[0] == board.spots[4] == board.spots[8] or board.spots[2] == board.spots[4] == board.spots[6]:
            return True

    def win(self, board):
        return self.horizontal_win(board) or self.vertical_win(board) or self.diagonal_win(board)

    def tie(self, board):
        available_spots = board.available_spots()
        if not available_spots:
            return True

    def game_over(self, board):
        if self.win(board) or self.tie(board):
            return True
