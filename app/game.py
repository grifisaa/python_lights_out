from app.game_state import GameState
import random

class Game:

    def __init__(self):
        self.state = GameState()
        self.reset()

    def update(self, x, y):
        x_change = [-1, 1]
        y_change = [-1, 1]

        for x_val in x_change:
            self.state.flip(x + x_val, y)

        for y_val in y_change:
            self.state.flip(x, y + y_val)

        self.state.flip(x, y)

    def reset(self):
        for i in range(0, 5):
            for j in range(0, 5):
                self.state.set(i, j, 1 if bool(random.getrandbits(1)) else 0)

        self.state.set_winner(False)

    def check_winner(self):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.state.get(i, j) == 1:
                    return False
        return True

    def get_state(self):
        return self.state
