#!/usr/bin/python3
"""Starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Return Hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_with_params(text):
    """Return C followed by the value of the text variable"""

    text_no_underscore = text.replace('_', ' ')
    return "C {}".format(text_no_underscore)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
