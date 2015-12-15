#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
from datetime import datetime
from queue import Queue
from threading import Thread

from flask import Flask
from playhouse.shortcuts import *

import RPi.GPIO as GPIO
from flask.ext.restful import Api, Resource, reqparse
from model import ActionHistory


app = Flask(__name__)
api = Api(app)

# queue for save new event
q = Queue()


def my_callback18(channel):
    global q
    data = [str(datetime.now()), 18]
    q.put(data)


def my_callback22(channel):
    global q
    data = [str(datetime.now()), 22]
    q.put(data)


class SaveToDatabase(Thread):
    def run(self):
        global q
        while True:
            src = q.get()
            obj = ActionHistory(created=src[0], board_num=src[1], mark=False)
            obj.save()
            del obj
            q.task_done()


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


parser = reqparse.RequestParser()
parser.add_argument('target')


class Action(Resource):
    def get(self, get_counts):
        items = ActionHistory().select().where(ActionHistory.mark == False).limit(get_counts)

        # conver to json
        alldata = []
        for item in items:
            json_data = json.dumps(model_to_dict(item))
            alldata.append(json_data)
        return alldata


class ActionList(Resource):
    def get(self):
        num = ActionHistory().select().where(ActionHistory.mark == False).count()
        return num  # len(ACTIONS)


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
        threadSaveDB = SaveToDatabase()
        threadSaveDB.start()

        # host use 0.0.0.0 for externally visible
        app.run(debug=True, host='0.0.0.0', port=5000)
        # app.run(port=5000, debug=True, host='0.0.0.0')
    finally:
        GPIO.cleanup()

'''
# test action
import requests
r = requests.get('http://localhost:5000/actions/x')
r.json()

# get how much record are there
r = requests.get('http://localhost:5000/actions')
r.text

#test out
r = requests.put('http://localhost:5000/out/x')
r.text
'''
