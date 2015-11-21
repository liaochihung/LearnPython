#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)

pwm = GPIO.PWM(0, 50)
pwm.start(0)
pause_time = 0.01

try:
    while True:
        for i in range(0, 101, 1):
            pwm.ChangeDutyCycle(i)
            time.sleep(pause_time)
        time.sleep(1)
        for i in range(100, -1, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(pause_time)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()

GPIO.cleanup()
