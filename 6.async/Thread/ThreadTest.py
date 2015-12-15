import threading


class Mesenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = Mesenger(name='send')
y = Mesenger(name='receive')

x.start()
y.start()
