import random
import threading
import time

try:
    import Queue
except:
    import queue as Queue


class producer:
    def __init__(self):
        self.food = ["ham", "soup", "salad"]
        self.nexttime = 0

    def run(self):
        global q
        while (time.clock() < 10):
            if (self.nexttime < time.clock()):
                f = self.food[random.randrange(len(self.food))]
                q.put(f)
                print("Adding " + f)
                self.nexttime += random.random()


class consumer:
    def __init__(self):
        self.nexttime = 0

    def run(self):
        global q
        while (time.clock() < 10):
            if (self.nexttime < time.clock() and not q.empty()):
                f = q.get()
                print("Removing " + f)
                self.nexttime += random.random() * 2


if __name__ == '__main__':
    q = Queue.Queue(10)

    p = producer()
    c = consumer()
    pt = threading.Thread(target=p.run, args=())
    ct = threading.Thread(target=c.run, args=())

    pt.start()
    ct.start()
