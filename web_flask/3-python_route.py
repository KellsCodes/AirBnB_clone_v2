#!/usr/bin/python3
"""a flask script to display “Hello HBNB!”"""
from flask import Flask

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
    """a function to return c is fun"""
    return f'C {text.replace("_"," ")}'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_python(text):
    """a function to return python is magic"""
    return f'python {text.replace("_"," ")}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
