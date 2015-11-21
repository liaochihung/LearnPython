#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
使用 Flask-RESTful 设计 RESTful API
尚未完成
'''

from flask.ext.restful import Api, Resource, reqparse

from flask import Flask


app = Flask(__name__)
api = Api(app)


class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')


class TaskListAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="", location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        pass

    def post(self):
        pass


class TaskAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        pass

    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)

    if len(task) == 0:
        abort(404)
    task = task[0]
    args = self.reqparse.parse_args()
    for k, v in args.iteritems():
        if v != None:
            task[k] = v
    return {'task': make_public_task(task)}

    def delete(self, id):
        pass


api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')