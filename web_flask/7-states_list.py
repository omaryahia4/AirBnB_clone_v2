#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask.templating import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    state = storage.all(State).values()
    state = sorted(state, key=lambda x: x.name)
    return render_template(
        '6-number_odd_or_even.html', State=state)


@app.teardown_appcontext
def close(self):
    """"""
    self.storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
