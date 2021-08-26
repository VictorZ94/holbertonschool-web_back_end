#!/usr/bin/env python3
""" Simple message of welcoming
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ first index template to getting started translate
    """
    title = 'Welcome to Holberton'
    header = 'Hello world'
    greeting = {'title': title, 'header': header}
    return render_template('0-index.html', greeting=greeting)


if __name__ == '__main__':
    app.run('0.0.0.0', '5000')
