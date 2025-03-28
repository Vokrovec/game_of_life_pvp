from flask import Flask

app = Flask("game of life pvp")

#every page is routed in router
from router import * 

if __name__ == "__main__":
    app.run(debug=True)
