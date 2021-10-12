class GameState:

    def __init__(self):
        self.board = [[0]*5]*5
        self.winner = False

    def flip(self, x, y):
        val = self.get(y, x)
        if (val == 0):
            self.set(y, x, 1)
        else:
            self.set(y, x, 0)

    def set(self, y, x, val):
        if (val > 1):
            val = 1
        if (val < 0):
            val = 0
        self.board[y][x] = val

    def set_winner(self, val):
        self.winner = val

    def get(self, y, x):
        return self.board[y][x]

    def valid_location(self, x, y):
        return x >= 0 and x < 5 and y >=0 and y < 5

    def to_dict(self):
        return {
            'board'  : self.board,
            'winner' : self.winner
        }
