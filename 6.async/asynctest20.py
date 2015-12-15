# callback-based async framework
# non-blocking sockets
# callbacks
# event look
# coroutines

import socket
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


def get(path):
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    selector.unregister(s.fileno())

    # s is writable!
    s.send(request.encode())

    chunks = []
    while True:
        selector.register(s.fileno(), EVENT_READ)
        selector.selector()
        selector.unregister(s.fileno())

        chunk = s.recv(1000)
        if chunk:
            chunks.append(chunk)
        else:
            body = (b''.join(chunks)).decode()
            print(body.split('\n')[0])
            return


start = time.time()
get('/foo')
get('/bar')
get('/foo')
get('/bar')
print('took %.1f sec' % (time.time() - start))

