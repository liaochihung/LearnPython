#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Basic flask app
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True)