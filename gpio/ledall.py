#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pins = [5, 6, 13, 19, 0, 1, 7, 8]


def setp(n, status='off'):
    if status == 'on':
        GPIO.output(n, GPIO.LOW)
    else:
        GPIO.output(n, GPIO.HIGH)


for i in pins:
    GPIO.setup(i, GPIO.OUT)
    setp(i, 'off')

try:
    for i in pins:
        setp(i, 'on')
except:
    print('except')
    GPIO.cleanup()
