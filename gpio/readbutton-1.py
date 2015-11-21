#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin = 12
GPIO.setup(pin, GPIO.IN)

# input("Press Enter when ready\n>")

print('Waiting for button press')

try:
    GPIO.wait_for_edge(pin, GPIO.FALLING)
    print("pressed")
except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()
