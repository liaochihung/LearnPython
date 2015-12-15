# callback-based async framework
# non-blocking sockets
# callbacks
# event look
# coroutines

import socket
import time


def get(path):
    s = socket.socket()
    s.connect(('localhost', 5000))

    s.setblocking(False)
    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    s.send(request.encode())

    chunks = []
    while True:
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

