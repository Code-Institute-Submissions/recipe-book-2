import os
import json
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


"""
Routing for Index.html
"""


@app.route('/')
def index():
    return "Hello World.....again"


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)