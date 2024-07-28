#!/usr/bin/python3
"""
Flask
hello hbnb
hbnb
c is cool
python is fun
n is a number
"""
from flask import Flask, render_template
from werkzeug.exceptions import NotFound

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
    """Python is cool
    """
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is_cool"):
    """Return python is cool
    """
    text_mod = text.replace('_', ' ')
    return "Python {}".format(text_mod)


@app.route("/number/<n>", strict_slashes=False)
def number_n(n):
    """n is a number
    """
    try:
        n = int(n)
        return "{} is a number".format(n)
    except ValueError:
        raise NotFound("The requested URL was not found on the server.\
                        If you entered the URL manually please check your\
                        spelling and try again.")


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """render template
    """
    try:
        n = int(n)
        render_template("5-number.html", n=n)
    except ValueError:
        raise NotFound("The requested URL was not found on the server.\
                        If you entered the URL manually please check your\
                        spelling and try again.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
