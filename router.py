from flask import render_template
from main import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html", size=20) #size is number of lines (not number of boxes)
