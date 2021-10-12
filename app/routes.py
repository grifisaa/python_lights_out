from app import app
from app import the_game
from flask import request, jsonify
import json

@app.route('/api/state', methods=['GET'])
def state():
    return jsonify(the_game.get_state().to_dict())

@app.route('/api/update', methods=['POST'])
def update():
    post_data = request.get_json()
    print(post_data)
    the_game.update(post_data[0], post_data[1])
    return("OK")

@app.route('/api/reset', methods=['GET'])
def reset():
    the_game.reset()
    return jsonify(the_game.get_state().to_dict())

@app.route('/api/status', methods=['GET'])
def status():
    return "OK"
