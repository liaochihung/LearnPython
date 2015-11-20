# -*- coding: utf-8 -*-

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)

while True:
    GPIO.output(24, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(24, GPIO.LOW)
    time.sleep(1)
