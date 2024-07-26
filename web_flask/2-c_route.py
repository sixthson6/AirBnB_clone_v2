#!/usr/bin/python3
"""
Flask
hello hbnb
hbnb
c is cool
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns hello hbnb
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def replace_text(text):
    """Returns C is <text>
    """
    text_mod = text.replace('_', ' ')
    return "C {}".format(text_mod)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
