from threading import Thread, Lock
import time
import random

queue = []
lock = Lock()


class ProducerThread(Thread):
    def run(self):
        nums = range(5)  # Will create the list [0, 1, 2, 3, 4]
        global queue
        while True:
            num = random.choice(nums)  # Selects a random number from list [0, 1, 2, 3, 4]
            lock.acquire()
            queue.append(num)
            print
            "Produced", num
            lock.release()
            # time.sleep(random.random())
            time.sleep(1)


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print
                "Nothing in queue, but consumer will try to consume"
            num = queue.pop(0)
            print
            "Consumed", num
            lock.release()
            time.sleep(0.01)


p1 = ProducerThread()
p2 = ProducerThread()
p1.start()
p2.start()

ConsumerThread().start()
