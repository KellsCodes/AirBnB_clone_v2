#!/usr/bin/python3
"""a flask script to display “Hello HBNB!”"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """a function to return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """a function to return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def index_c(text):
    """a function to return C is fun"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def a_number(n):
    """displays only when a number is passed on the url"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", p=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
