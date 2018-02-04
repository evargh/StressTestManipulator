#!/usr/bin/python

# this code initializes an HTML page and hosts it

from flask import Flask
from flask import render_template
from tkinter import Tk, Label, Button

app = Flask(__name__)


@app.route('/')
def mypysite(name=None):
    # return the html page i already made
    return render_template('index.html')


if __name__ == "__main__":
    # hosts the site locally
    app.run('0.0.0.0')