#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''

'''

import time
from datetime import datetime

import RPi.GPIO as GPIO
from flask import Flask
from flask.ext.restful import Api, Resource, reqparse, abort
from model import ActionHistory

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


def my_callback18(channel):
    new_data = ActionHistory(create=datetime.now(),
                             board_num=18)
    new_data.save()
    # print('Falling edge detected on 18')


def my_callback22(channel):
    new_data = ActionHistory(create=datetime.now(),
                             board_num=22)
    new_data.save()
    # print('Falling edge detected on 18')


def init_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    pins = [16, 12, 18, 22]

    GPIO.setup(pins[0], GPIO.IN)
    GPIO.setup(pins[1], GPIO.IN)
    GPIO.setup(pins[2], GPIO.IN)
    GPIO.setup(pins[3], GPIO.IN)

    GPIO.add_event_detect(
        pins[2],
        GPIO.FALLING,
        callback=my_callback18,
        bouncetime=300)

    GPIO.add_event_detect(
        pins[3],
        GPIO.FALLING,
        callback=my_callback22,
        bouncetime=300)


def abort_if_todo_doesnt_exist(get_counts):
    # if get_counts not in ACTIONS:
    if len(ACTIONS) < 1:
        abort(404, message="Action {} doesn't exist".format(get_counts))


parser = reqparse.RequestParser()
parser.add_argument('target')


class Action(Resource):
    def get(self, get_counts):
        abort_if_todo_doesnt_exist(get_counts)
        items = []
        for i in range(get_counts):
            items.append(ACTIONS[i])
        return items


class ActionList(Resource):
    def get(self):
        return len(ACTIONS)


def sendcmd(id):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(id, GPIO.OUT)
    GPIO.output(id, GPIO.LOW)
    time.sleep(1)
    GPIO.output(id, GPIO.HIGH)


class Output(Resource):
    def put(self, target_id):
        sendcmd(target_id)
        return target_id, 202


##
## Actually setup the Api resource routing here
##
api.add_resource(ActionList, '/actions')
api.add_resource(Action, '/actions/<int:get_counts>')
api.add_resource(Output, '/out/<int:target_id>')

if __name__ == '__main__':
    try:
        init_gpio()
        # host use 0.0.0.0 for externally visible
        app.run(debug=True, host='0.0.0.0', port=5000)
        # app.run(port=5000, debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()

'''
# test action
import requests
r = requests.get('http://localhost:5000/action/x')
r.json()

#test out
r = requests.put('http://localhost:5000/out/x')
r.text
'''
