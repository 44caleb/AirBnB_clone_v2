#!/usr/bin/python3
"""web script that starts a flask web application"""


from models import storage
from models.state import State
from flask import Flask, render_template
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


@app.route("/states_list", strict_slashes=False)
def states():
    """displays list of states"""
    states = storage.all(State).values()
    storage.close()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
