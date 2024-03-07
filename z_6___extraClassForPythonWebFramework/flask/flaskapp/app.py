import os
import sys

from flask import Flask

app = Flask(__name__)


@app.route("/")
def helo_world() -> str:
    return "Hello World"


if __name__ == "__main__":
    app.run()
