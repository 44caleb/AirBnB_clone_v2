#!/usr/bin/python3
"""web script that starts a flask web application"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """home page of webapp"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """displays c follwed by text in the url"""
    if "_" in text:
        text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """displays Python follwed by text in the url"""
    if "_" in text:
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    return('%d is a number' % n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
