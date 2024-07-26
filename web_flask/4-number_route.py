#!/usr/bin/python3
"""
Flask
hello
hbnb
c is cool
n is a number
python is cool
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """return hello hbnb
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """return C is <text>
    """
    text_mod = text.replace('_', ' ')
    return "C {}".format(text_mod)


@app.route("/python", strict_slashes=False)
def python_def():
    """Return Python is cool
    """
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    """return Python <text>
    """
    text_mod = text.replace('_', ' ')
    return "Python {}".format(text_mod)


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    """Return n is a number
    """
    n = int(n)
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
