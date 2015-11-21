#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask_restful import Resource, Api

from flask import Flask


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
