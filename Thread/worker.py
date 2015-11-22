from queue import Queue
from threading import Thread

queue = Queue()


def consumer():
    print('comsumer waiting')
    queue.get()
    print('comsumer done')


thread = Thread(target=consumer)
thread.start()

print('producer putting')
queue.put(object())
thread.join()
print('producer done')
