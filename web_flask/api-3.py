#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Basic flask app with auth
'''
from flask import Flask, make_response, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'skpt':
        return '0000'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access!'}), 401)


@app.route('/')
@auth.login_required
def index():
    return "Hello, World!"


@app.route('/testauth')
@auth.login_required
def testauth():
    return "Pass auth."


if __name__ == '__main__':
    app.run(debug=True)