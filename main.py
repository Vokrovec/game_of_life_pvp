from flask import Flask

app = Flask("game of life pvp")

from router import *

if __name__ == "__main__":
    app.run(debug=True)
