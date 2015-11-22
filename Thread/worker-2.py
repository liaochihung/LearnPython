#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
import time
import random
from queue import Queue

q = Queue()


class Producer(Thread):
    def run(self):
        nums = range(5)
        global q
        while True:
            num = random.choice(nums)
            q.put(num)
            print('Produced:', num)
            time.sleep(3)


class Consumer(Thread):
    def run(self):
        global q
        while True:
            print('Consumer is waiting data')
            num = q.get()
            q.task_done()
            print('Consumed:', num)
            time.sleep(0.05)


p = Producer()
c = Consumer()

p.start()
c.start()


