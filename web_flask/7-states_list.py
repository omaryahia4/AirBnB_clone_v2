#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask.templating import render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    state = storage.all("States").values()
    return render_template(
        '6-number_odd_or_even.html', States=state)


@app.teardown_appcontext
def close(self):
    """"""
    self.storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
