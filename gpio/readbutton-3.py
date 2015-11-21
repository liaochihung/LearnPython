#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
#import time

def my_callback(channel):
    print('Falling edge detected on 18')

def my_callback2(channel):
    print('Falling edge detected on 22')

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = [16,12,18,22]

GPIO.setup(pins[0], GPIO.IN)
GPIO.setup(pins[1], GPIO.IN)
GPIO.setup(pins[2], GPIO.IN)
GPIO.setup(pins[3], GPIO.IN)

input("Press Enter when ready\n>")
print('Waiting for button press')

GPIO.add_event_detect(
    pins[2],
    GPIO.FALLING, #GPIO.BOTH,
    callback=my_callback,
    bouncetime=300)

GPIO.add_event_detect(
    pins[3],
    GPIO.FALLING, #GPIO.BOTH,
    callback=my_callback2,
    bouncetime=300)

try:
    GPIO.wait_for_edge(pins[1], GPIO.RISING)
    print("pressed")
    #sleep(30)
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
