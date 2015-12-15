#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
使用 Flask-RESTful 设计 RESTful API
'''

from flask import Flask

from flask.ext.restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

ACTIONS = [
    {
        'datetime': 20151121060606,
        'event': 10
    },
    {
        'datetime': 20151121070606,
        'event': 22
    },
    {
        'datetime': 20151121070609,
        'event': 16
    }
]


def abort_if_todo_doesnt_exist(get_counts):
    # if get_counts not in ACTIONS:
    if len(ACTIONS) < 1:
        abort(404, message="Action {} doesn't exist".format(get_counts))


parser = reqparse.RequestParser()
parser.add_argument('task')


class Action(Resource):
    def get(self, get_counts):
        abort_if_todo_doesnt_exist(get_counts)
        items = []
        for i in range(int(get_counts)):
            items.append(ACTIONS[i])
        return items


class ActionList(Resource):
    def get(self):
        return len(ACTIONS)

##
## Actually setup the Api resource routing here
##
api.add_resource(ActionList, '/actions')
api.add_resource(Action, '/actions/<get_counts>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)