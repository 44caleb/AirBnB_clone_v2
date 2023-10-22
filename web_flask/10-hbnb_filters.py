#!/usr/bin/python3
"""web script that starts a flask web application"""


from models import storage
from models.state import State
from models.amenity import Amenity
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


@app.teardown_appcontext
def close_connection(exception=None):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states():
    """displays list of states"""
    states = storage.all(State).values()
    storage.close()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    state_found = None

    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            state_found = state
            return render_template("9-states.html", state_found=state_found)
    return render_template("9-states.html", state_found=state_found)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """displays filters section of hbnb web_page"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
