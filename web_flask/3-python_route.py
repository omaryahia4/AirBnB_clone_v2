#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """display “Python ”, followed by the value of the text
       - default value : 'is cool'
    """
    text = text.replace("_", " ")
    return 'Python ' + text


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
