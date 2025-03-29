from flask import render_template
from main import app
GRID_SIDE_SIZE = 20

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html", size=GRID_SIDE_SIZE) #size is number of lines (not number of boxes)

@app.route("/eval-game", methods=["POST"])
def eval_game():
    grid = [0 for _ in range(GRID_SIDE_SIZE**2)]
    return render_template("game_grid.html", grid=grid)
