from flask import Flask

app = Flask(__name__)

from app.game import Game
the_game = Game()

from app import routes
from app.game_state import GameState
